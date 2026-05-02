# Simple Public Inworld TTS

Script simples para gerar voz usando os endpoints públicos do site `inworld.ai`, sem cookies, sem login, sem `Authorization`, sem Firebase e sem `.env`.

Arquivo principal:

```text
C:\Users\Larri\Documents\New project 8\simple_public_tts.py
```

## O Que Ele Faz

O script envia um texto para o endpoint público:

```text
POST https://inworld.ai/api/create-speech
```

O site responde em `application/x-ndjson`, ou seja, várias linhas JSON. Cada linha pode trazer um pedaço do áudio em Base64:

```json
{"result":{"audioContent":"...","timestampInfo":null}}
```

O código lê cada linha, pega `result.audioContent`, decodifica o Base64, junta os pedaços e grava o resultado em um arquivo `.wav`.

Para listar vozes, ele usa:

```text
GET https://inworld.ai/api/list-voices
```

## Requisitos

Python 3.10+ e a biblioteca `requests`.

Se precisar instalar:

```powershell
pip install requests
```

## Uso Rápido

Entre na pasta onde o script está:

```powershell
cd "C:\Users\Larri\Documents\New project 8"
```

Gerar áudio com a voz padrão `Beatriz`:

```powershell
python simple_public_tts.py "Olá, isso é um teste de voz."
```

Gerar áudio escolhendo o arquivo de saída:

```powershell
python simple_public_tts.py "Olá, isso é um teste de voz." --output output\meu_audio.wav
```

Trocar a voz:

```powershell
python simple_public_tts.py "Olá, isso é um teste com outra voz." --voice Mariana
```

Listar vozes em português:

```powershell
python simple_public_tts.py --list --lang pt
```

Listar vozes em inglês:

```powershell
python simple_public_tts.py --list --lang en
```

## Como Trocar Voz

Use o parâmetro `--voice` com o ID da voz.

Exemplos:

```powershell
python simple_public_tts.py "Texto em português." --voice Beatriz
python simple_public_tts.py "Texto em português." --voice Heitor
python simple_public_tts.py "Text in English." --voice Luna
python simple_public_tts.py "Texto en español." --voice Sofia
python simple_public_tts.py "Texte en français." --voice Hélène
```

O ID precisa bater exatamente com a coluna `voiceId` abaixo. Alguns nomes têm acento, como `Maitê`, `Hélène` e `Étienne`.

## Parâmetros

```text
text                  Texto que será convertido em áudio.
--voice               Voz usada. Padrão: Beatriz.
--output, -o          Caminho do arquivo de saída. Padrão: output/simple_tts.wav.
--model               Modelo TTS. Padrão: inworld-tts-1.5-max.
--sample-rate         Sample rate em Hz. Padrão: 48000.
--list                Lista as vozes públicas.
--lang                Filtra a lista por idioma. Exemplo: pt, en, es, fr.
```

## Vozes

### Português (`pt`)

| voiceId | Descrição |
|---|---|
| Heitor | Composed Portuguese-speaking male voice with a neutral tone |
| Maitê | Middle-aged Portuguese-speaking female voice |
| Beatriz | A clear, mid-pitched adult female voice with a Brazilian accent, speaking fluently in a quiet indoor environment. |
| Mariana | A young, enthusiastic female speaker with a clear, smooth voice and a Brazilian Portuguese accent, speaking at a moderate pace in a high-quality recording environment. |
| Murilo | A calm and analytical adult male with a clear, standard Brazilian Portuguese accent, speaking at a moderate pace in a quiet environment. |

### Inglês (`en`)

| voiceId | Descrição |
|---|---|
| Loretta | Inviting, folksy Southern female voice, perfect for cooking shows, heartwarming family tales, and cozy radio ads. |
| Darlene | Soothing, comforting Southern female voice, ideal for bedtime stories, family-centered commercials, and nostalgic narrations. |
| Marlene | Friendly, relaxed Southern female voice, ideal for home-style cooking tutorials, community event promotions, and downhome commercials. |
| Hank | Warm, laid-back Southern male voice, ideal for travel documentaries, heritage storytelling, and down-to-earth podcast ads. |
| Evelyn | A gentle and intimate female voice, ideal for personal ASMR content, affirmations, and close, calming conversations. |
| Celeste | Soft, whispery female voice, ideal for ASMR videos, soothing lullabies, and gentle mindfulness sessions. |
| Pippa | Friendly and casual Australian female voice, ideal for relaxed instructional content. |
| Tessa | Upbeat, conversational Australian female voice, perfect for lifestyle vlogs, playful advertisements, and engaging social media content. |
| Liam | Upbeat, motivating Australian male voice, perfect for energizing workout sessions, lively event promotions, and informal lifestyle content. |
| Callum | Casual and friendly Australian male voice, ideal for informal instructional content. |
| Hamish | Friendly and casual Australian male voice, ideal for character-driven roles and upbeat fitness. |
| Abby | Bright, eager American female child voice, ideal for animated characters, upbeat educational content, and lively kids' commercials. |
| Graham | Profound, authoritative British male voice, perfect for historical documentaries, luxury brand advertisements, and educational content. |
| Rupert | Resonant, commanding British male voice, ideal for motivational speeches, epic film trailers, and dynamic corporate presentations. |
| Mortimer | Gravelly, aggressive male character voice, ideal for fantasy villains and high-intensity game dialogue. |
| Snik | Hoarse, cunning male voice, perfect for devious fantasy roles, fantasy heist scenarios, and trickster-themed animations. |
| Anjali | A confident and articulate Indian female voice, ideal for professional training materials. |
| Saanvi | Crisp, articulate Indian female voice, ideal for dynamic e-learning modules, articulate documentary narrations, and vibrant travel vlogs. |
| Arjun | Clear, composed Indian male voice, well-suited for instructional webinars and technology explainers. |
| Claire | Warm, gentle Eastern European female voice, ideal for bedtime stories, relaxation podcasts. |
| Oliver | Neutral and clear male voice, ideal for public announcements and educational information. |
| Simon | Articulate, insightful male voice, perfect for corporate presentations, technical tutorials, and steady news reporting. |
| Elliot | A calm, steady male voice, suitable for nature documentaries, general informational content, and relaxed narrations. |
| James | Vibrant, expressive male voice, perfect for animated video content, lively event hosting, and captivating children's stories. |
| Serena | Soft, nurturing female voice, perfect for mindfulness sessions, nature-inspired visualizations, and gentle wellness podcasts. |
| Gareth | Soothing, gentle male voice, ideal for guided meditations, mindfulness exercises, and relaxation-focused wellness content. |
| Vinny | Gritty, assertive New York male voice, perfect for crime dramas, urban documentaries, and no-nonsense character roles. |
| Lauren | Confident, friendly American female voice, ideal for corporate presentations, upbeat commercials, and engaging podcasts. |
| Jessica | Encouraging, articulate American female voice, perfect for self-help audiobooks, warm customer service messages, and clear e-learning modules. |
| Ethan | Assured, precise male voice, perfect for tech tutorials, detailed gadget overviews, and captivating product demonstrations. |
| Tyler | Authoritative, insightful male voice, ideal for tech explainer videos, in-depth software reviews, and dynamic coding guides. |
| Jason | Lucid, engrossing male voice, ideal for tech tips, creative productivity hacks, and supportive user interface tutorials. |
| Chloe | Thoughtful, introspective youthful female voice, perfect for coming-of-age narratives, personal growth stories, and emotional teen dramas. |
| Veronica | Intimidating, commanding female voice, perfect for ruthless antagonists, high-stakes negotiations, and chilling monologues. |
| Victoria | Silky, cunning British female voice, ideal for narrating intricate plots. |
| Miranda | Menacing, cold-hearted female voice, perfect for strategic villains and mysterious narratives. |
| Sebastian | Intimidating, steely male voice, perfect for ruthless antagonists, strategic power struggles, and chilling monologues. |
| Victor | Ominous, sinister male voice, ideal for dark conspiracies, eerie suspense scenes, and enigmatic villain roles. |
| Malcolm | Authoritative, manipulative male voice, perfect for cunning leaders, intense negotiation scenes, and persuasive villain speeches. |
| Nate | Conversational, sociable male voice, great for customer support and friendly guidance. |
| Brian | Friendly, encouraging American male voice, ideal for educational tutorials, motivational content, and instructional videos. |
| Amina | Warm, inviting West African female voice, ideal for community outreach, cultural storytelling, and educational workshops. |
| Kelsey | Warm, empathetic, reassuring female voice, ideal for phone support, appointment confirmations, and customer success calls. |
| Derek | Steady, professional, composed American male voice, ideal for banking support, account inquiries, and service escalation calls. |
| Evan | Friendly, approachable, easygoing male voice, ideal for onboarding calls, retail assistance, and customer check-ins. |
| Kayla | Enthusiastic, youthful female voice, ideal for reaction videos, trendy product reviews, and energetic lifestyle vlogs. |
| Jake | Amiable, introspective male voice, ideal for motivational talks, personal growth content, and charming interviews. |
| Grant | Calm, attentive, helpful male voice, ideal for insurance claims, troubleshooting walkthroughs, and helpdesk interactions. |
| Tristan | Deliberate, controlled male voice, ideal for documentary narration, polished voiceover campaigns, and clear long-form infomercial storytelling. |
| Nadia | Personable, lively female voice, perfect for tutorial walkthroughs, friendly support messaging, and engaging narration for creator-led product content. |
| Selene | Soft, flirtatious female voice, ideal for companion-style interactions, charming game dialogue, and emotionally playful character-driven story scenes. |
| Marcus | Authoritative, empathetic male voice, great for civic campaigns, community outreach explainers, and trustworthy commercial reads with emotional credibility. |
| Riley | Playful, youthful female voice, perfect for animated storytelling, upbeat game characters, and high-energy kid-focused digital content. |
| Damon | Calm, raspy male voice, suited for moody narration, atmospheric roleplay characters, and grounded meditative reads with subtle tension. |
| Cedric | Crisp, measured male voice, ideal for formal announcements, premium trailer narration, and command-forward presentation scripts. |
| Mia | Youthful, expressive female voice, ideal for adolescent characters, school-age animation dialogue, and bright coming-of-age narrative scenes. |
| Naomi | Warm, grounded female voice, perfect for narrative podcasting, people-first customer guidance, and emotionally real brand storytelling. |
| Jonah | Soothing, calm male voice, great for tutorial guidance, reassuring support flows, and gentle instructional narration with steady pacing. |
| Levi | Measured, ominous male voice, ideal for suspense narration, dark fantasy storytelling, and composed dramatic monologues. |
| Avery | Youthful, performative male voice, suited for gameshow-style hosting, energetic presenter reads, and expressive young character parts. |
| Brandon | Bold, strident male voice, ideal for structured announcements, news-style reads, and direct promotional messaging. |
| Conrad | Gruff, weathered male voice, perfect for detective archetypes, hard-edged audiobook roles, and serious investigative narration. |
| Bianca | Deep, controlled female voice, ideal for serious corporate reads, composed documentary segments, and measured authority-led explainers. |
| Lucian | Brooding, foreboding male voice, suited for villainous character arcs, gothic drama scenes, and dark narrative worldbuilding. |
| Trevor | Punchy, expressive male voice, perfect for energetic promos, announcer-driven reveals, and fast-moving scripted event intros. |
| Alex | Energetic and expressive mid-range male voice, with a mildly nasal quality. |
| Ashley | A warm, natural female voice. |
| Craig | Older British male with a refined and articulate voice. |
| Deborah | Warm, peaceful female voice with a calm tone. |
| Dennis | Middle-aged man with a smooth, calm and friendly voice. |
| Edward | American male with an emphatic, confident and streetwise tone. |
| Elizabeth | Professional middle-aged woman, perfect for narrations and voiceovers. |
| Hades | Commanding and gruff male voice, think an omniscient narrator or castle guard. |
| Julia | Quirky, high-pitched female voice that delivers lines with playful energy. |
| Pixie | High-pitched, childlike female voice with a squeaky quality, great for a cartoon character. |
| Mark | Energetic, expressive man with a rapid-fire delivery. |
| Olivia | Young, British female with a friendly and helpful tone, conveying confidence and efficiency. |
| Priya | Even-toned female voice with an Indian accent. |
| Ronald | Confident, British man with a deep, gravelly voice. |
| Sarah | Fast-talking young adult woman, with a questioning and curious tone. |
| Shaun | Friendly, dynamic male voice great for conversations. |
| Theodore | Gravelly male voice, with a time-worn quality. |
| Timothy | Lively, upbeat American male voice. |
| Wendy | Posh, middle-aged British female voice. |
| Dominus | Robotic, deep male voice with a menacing quality. Perfect for villains. |
| Hana | Bright, expressive young female voice, perfect for storytelling, gaming, and playful content. |
| Clive | British-accented English-language male voice with a calm, cordial quality. |
| Carter | Energetic, mature radio announcer-style male voice, great for storytelling, pep talks, and voiceovers. |
| Blake | Rich, intimate male voice, perfect for audiobooks, romantic content, and reassuring narration. |
| Luna | Calm, relaxing female voice, perfect for meditations, sleep stories, and mindfulness exercises. |
| Reed | Clear, professional American male voice, well-suited for support and training. |
| Duncan | Warm, articulate British male voice for customer support and education. |
| Felix | Calm, friendly British male voice, ideal for help and tutorials. |
| Eleanor | Polished, approachable British female voice for support and learning. |
| Sophie | Friendly British female voice, great for assistance and knowledge sharing. |

### Espanhol (`es`)

| voiceId | Descrição |
|---|---|
| Diego | Spanish-speaking male voice with a soothing, gentle quality |
| Lupita | Vibrant, energetic young Spanish-speaking female voice |
| Miguel | A calm adult Spanish-speaking male voice, perfect for storytelling |
| Rafael | Middle-aged Spanish-speaking male with a deep, composed voice. Great for narrations |
| Sofia | A fast-paced, clear, and engaging adult female voice with a neutral Latin American Spanish accent, recorded in a high-quality studio environment. |
| Camila | A young female with a smooth, clear voice speaking at a moderate pace in a quiet environment. |
| Mateo | A young adult male with a smooth, clear voice speaking thoughtfully in a quiet studio setting. |
| Mauricio | A serious adult male with a smooth, clear voice speaking slowly and deliberately in a quiet studio environment. |

### Francês (`fr`)

| voiceId | Descrição |
|---|---|
| Alain | Deep, smooth middle-aged male French voice. Composed and calm |
| Hélène | Middle-aged French woman, with a smooth, musical, and graceful voice |
| Mathieu | A French male voice carrying a nasal quality |
| Étienne | Calm young adult French male |

### Italiano (`it`)

| voiceId | Descrição |
|---|---|
| Gianni | Deep, smooth Italian male voice that speaks rapidly |
| Orietta | Calm adult female Italian voice, with a soothing cadence |

### Chinês (`zh`)

| voiceId | Descrição |
|---|---|
| Yichen | A calm, flat young adult male Chinese voice |
| Xiaoyin | A youthful Chinese female voice with a gentle, sweet voice |
| Xinyi | A Chinese woman with a neutral tone, perfect for narrations |
| Jing | An energetic, fast-paced young Chinese female |
| Mei | A young female with a smooth, clear voice and standard Mandarin accent, speaking at a moderate pace in a quiet studio environment. |
| Ming | A young adult male with a smooth, clear voice speaking slowly and deliberately in a quiet environment. |

### Japonês (`ja`)

| voiceId | Descrição |
|---|---|
| Asuka | Friendly, young adult Japanese female voice |
| Satoshi | Dramatic, expressive male Japanese voice filled with energy |
| Hina | A young adult female with a smooth, clear voice speaking in a formal, narrative tone. |
| Haruto | A slow, deliberate, and gravelly old male voice speaking in a reminiscent tone. |

## Observações

Esse fluxo usa endpoint público do site `inworld.ai`. Ele funcionou sem credenciais no teste feito aqui, mas pode mudar, ter limite, bloquear por região ou alterar formato de resposta no futuro.

Se a API voltar erro, tente primeiro:

```powershell
python simple_public_tts.py --list --lang pt
```

Se a listagem funcionar e a geração falhar, o problema provavelmente está no texto, na voz escolhida ou em limite temporário do endpoint.
