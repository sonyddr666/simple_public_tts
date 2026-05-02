#!/usr/bin/env python3
"""
Simple public Inworld TTS client.

No cookies, no Authorization header, no Firebase token.

Examples:
  python simple_public_tts.py "Ola, isso e um teste."
  python simple_public_tts.py "Ola, isso e um teste." --voice Mariana
  python simple_public_tts.py --list --lang pt
"""

from __future__ import annotations

import argparse
import base64
import json
import sys
from pathlib import Path
from typing import Any

import requests


BASE_URL = "https://inworld.ai"
LIST_VOICES_URL = f"{BASE_URL}/api/list-voices"
CREATE_SPEECH_URL = f"{BASE_URL}/api/create-speech"

DEFAULT_HEADERS = {
    "Accept": "*/*",
    "Content-Type": "application/json",
    "Origin": BASE_URL,
    "Referer": f"{BASE_URL}/",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/147.0.0.0 Safari/537.36"
    ),
}


def fetch_voices() -> list[dict[str, Any]]:
    response = requests.get(
        LIST_VOICES_URL,
        headers={k: v for k, v in DEFAULT_HEADERS.items() if k != "Content-Type"},
        timeout=30,
    )
    response.raise_for_status()
    return response.json().get("voices", [])


def print_voices(lang: str | None = None) -> None:
    voices = fetch_voices()
    if lang:
        voices = [v for v in voices if lang in v.get("languages", [])]

    for voice in voices:
        voice_id = voice.get("voiceId", "")
        languages = ",".join(voice.get("languages", []))
        description = (voice.get("description") or "").strip()
        print(f"{voice_id:18} {languages:8} {description}")


def iter_audio_chunks(response: requests.Response) -> bytes:
    audio = bytearray()

    for raw_line in response.iter_lines(decode_unicode=True):
        if not raw_line:
            continue

        try:
            event = json.loads(raw_line)
        except json.JSONDecodeError:
            continue

        chunk_b64 = event.get("result", {}).get("audioContent")
        if chunk_b64:
            audio.extend(base64.b64decode(chunk_b64))

    return bytes(audio)


def generate_tts(
    text: str,
    voice_id: str,
    output_path: Path,
    model_id: str = "inworld-tts-1.5-max",
    sample_rate: int = 48000,
) -> Path:
    payload = {
        "text": text,
        "voiceId": voice_id,
        "modelId": model_id,
        "audioConfig": {
            "audioEncoding": "LINEAR16",
            "sampleRateHertz": sample_rate,
        },
    }

    response = requests.post(
        CREATE_SPEECH_URL,
        headers=DEFAULT_HEADERS,
        json=payload,
        stream=True,
        timeout=120,
    )
    response.raise_for_status()

    audio = iter_audio_chunks(response)
    if not audio:
        raise RuntimeError("The API returned no audio chunks.")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(audio)
    return output_path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate TTS with public inworld.ai endpoints.")
    parser.add_argument("text", nargs="?", help="Text to synthesize.")
    parser.add_argument("--voice", default="Beatriz", help="Voice ID. Example: Beatriz, Mariana, Heitor.")
    parser.add_argument("--output", "-o", default="output/simple_tts.wav", help="Output WAV path.")
    parser.add_argument("--model", default="inworld-tts-1.5-max", help="Model ID.")
    parser.add_argument("--sample-rate", type=int, default=48000, help="Sample rate in Hz.")
    parser.add_argument("--list", action="store_true", help="List public voices and exit.")
    parser.add_argument("--lang", help="Filter voices by language when using --list. Example: pt, en, es.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.list:
        print_voices(args.lang)
        return 0

    if not args.text:
        parser.error("text is required unless --list is used")

    try:
        output = generate_tts(
            text=args.text,
            voice_id=args.voice,
            output_path=Path(args.output),
            model_id=args.model,
            sample_rate=args.sample_rate,
        )
    except requests.HTTPError as exc:
        print(f"HTTP error: {exc}", file=sys.stderr)
        if exc.response is not None:
            print(exc.response.text[:1000], file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(f"Saved: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
