# SAKURA

## Data Examples
Here we provide some examples from SAKURA, with the choices omitted for brevity. The entire dataset can be obtained in ``data``.
* Gender

|sub-track|instruction|
|------|-----|
|single-hop|Please identify the gender of the speaker.|
|multi-hop|Who among the options do you think has the same gender as the speaker in the audio?|

* Language


|sub-track|instruction|
|------|-----|
|single-hop|Listen to the speech segment, and choose the language spoken by the speaker. |
|multi-hop|From the listed countries, which one has the audio's spoken language as an official language? |

* Emotion

|sub-track|instruction|
|------|-----|
|single-hop|What emotion is the speaker expressing in the audio?|
|multi-hop|Which sentence best matches the emotional state of others with the same emotion expressed in the audio?|

* Animal

|sub-track|instruction|
|------|-----|
|single-hop|Identify the animal most likely responsible for the sound in this audio clip and choose the most likely one from the options. |
|multi-hop|What physical feature does the animal in the provided audio segment have?|

## Baselines
We included several large audio-language models. The implementations were based on the official ones.

- LTU-AS
    - Joint Audio and Speech Understanding [[arXiv](https://arxiv.org/abs/2309.14405), [GitHub](https://github.com/YuanGongND/ltu)]

- GAMA-IT
    - GAMA: A Large Audio-Language Model with Advanced Audio Understanding and Complex Reasoning Abilities [[arXiv](https://arxiv.org/abs/2406.11768), [GitHub](https://github.com/Sreyan88/GAMA)]

- SALMONN
    - SALMONN: Towards Generic Hearing Abilities for Large Language Models [[arXiv](https://arxiv.org/abs/2310.13289), [GitHub](https://github.com/bytedance/SALMONN)]

- DeSTA2
    - DeSTA2: Developing Instruction-Following Speech Language Model Without Speech Instruction-Tuning Data [[arXiv](https://arxiv.org/abs/2409.20007), [GitHub](https://github.com/kehanlu/DeSTA2)]

- Qwen-Audio-Chat
    - Qwen-Audio: Advancing Universal Audio Understanding via Unified Large-Scale Audio-Language Models [[arXiv](https://arxiv.org/abs/2311.07919), [GitHub](https://github.com/QwenLM/Qwen-Audio)]

- Qwen2-Audio-Instruct
    - Qwen2-Audio Technical Report [[arXiv](https://arxiv.org/abs/2407.10759), [GitHub](https://github.com/QwenLM/Qwen2-Audio)]

- GPT-4o Audio
    - GPT-4o System Card [[arXiv](https://arxiv.org/abs/2410.21276), [website](https://openai.com)]

- Gemini-1.5-flash and Gemini-1.5-pro
    - Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context [[arXiv](https://arxiv.org/abs/2403.05530), [website](https://deepmind.google/technologies/gemini/)]


## Evaluation
We adopted LLM-as-a-judge approach. Please refer to ``evaluation`` for more details.
