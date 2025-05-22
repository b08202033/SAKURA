# 🌸 SAKURA: On the Multi-hop Reasoning of Large Audio-Language Models Based on Speech and Audio Information

### The official GitHub page of the paper "SAKURA: On the Multi-hop Reasoning of Large Audio-Language Models Based on Speech and Audio Information"
- Authors: Chih-Kai Yang, Neo S. Ho*, Yen-Ting Piao*, Hung-yi Lee (*Equal Contribution)
- Affiliation: National Taiwan University
- Accepted to **Interspeech 2025**
- Paper link: https://arxiv.org/abs/2505.13237

## Overview
<div style="text-align: center;">
  <div style="display: flex; align-items: center; justify-content: center;">
    <img src="figures/sakura_overview.png" alt="logo" style="width: 1000px; margin-right: 10px;">
  </div>
</div>

## Abstract

**TL;DR: We propose SAKURA, a benchmark for LALM multi-hop reasoning, and reveal their deficiency of such reasoning skills.**

Large audio-language models (LALMs) extend the large language models with multimodal understanding in speech, audio, etc. While their performances on speech and audio-processing tasks are extensively studied, their reasoning abilities remain underexplored. Particularly, their multi-hop reasoning, the ability to recall and integrate multiple facts, lacks systematic evaluation. Existing benchmarks focus on general speech and audio-processing tasks, conversational abilities, and fairness but overlook this aspect. To bridge this gap, we introduce SAKURA, a benchmark assessing LALMs’ multi-hop reasoning based on speech and audio information. Results show that LALMs struggle to integrate speech/audio representations for multi-hop reasoning, even when they extract the relevant information correctly, highlighting a fundamental challenge in multimodal reasoning. Our findings expose a critical limitation in LALMs, offering insights and resources for future research.

## News
- [2025.05.19] Our paper is accepted to Interspeech 2025! See you in Rotterdam!
- [2025.05.22] Our paper is now available on [arXiv](https://arxiv.org/abs/2505.13237)

## Data Examples
Here we provide some examples from SAKURA, with the choices omitted for brevity. The entire dataset can be obtained in ``data/``.
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
Here are the baseline models we included in the paper. The implementations were based on the official ones.

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
We adopted LLM-as-a-judge approach for automatic evaluation in SAKURA. Please refer to ``evaluation/`` for more details.
