# Dataset

Here contains the dataset of all the four tracks of SAKURA. You can also find our dataset on [HuggingFace](https://huggingface.co/SLLM-multi-hop).

## Data Examples
Here we provide some examples from SAKURA, with the choices omitted for brevity.

<details>
<summary>Gender track</summary>

|sub-track|instruction|
|------|-----|
|single-hop|Please identify the gender of the speaker.|
|multi-hop|Who among the options do you think has the same gender as the speaker in the audio?|

</details>


<details>
<summary>Language track</summary>


|sub-track|instruction|
|------|-----|
|single-hop|Listen to the speech segment, and choose the language spoken by the speaker. |
|multi-hop|From the listed countries, which one has the audio's spoken language as an official language? |

</details>


<details>
<summary>Emotion track</summary>

|sub-track|instruction|
|------|-----|
|single-hop|What emotion is the speaker expressing in the audio?|
|multi-hop|Which sentence best matches the emotional state of others with the same emotion expressed in the audio?|

</details>

<details>
<summary>Animal track</summary>

|sub-track|instruction|
|------|-----|
|single-hop|Identify the animal most likely responsible for the sound in this audio clip and choose the most likely one from the options. |
|multi-hop|What physical feature does the animal in the provided audio segment have?|

</details>

## Structure
### Tracks
SAKURA consists of four tracks: Gender, Language, Emotion, and Animal. The corresponding data are stored in ``Gender/``, ``Language/``, ``Emotion/``, and ``Animal/``, respectively.

### Speech/Audio Data
The speech/audio data of each track are stored in ``audio/`` folder under the tracks' directories. For example, the audio data for the Animal track is in ``Animal/audio/``.

### Instruction and Golden Answers
The metadata, including the instructions and golden answers of the questions in each track, is stored in the ``metadata.csv`` under the track's directory. For instance, the metadata for the Animal track is in ``Animal/metadata.csv``.

There are 6 columns in ``metadata.csv``: ``file``, ``attribute_label``, ``single_instruction``, ``single_answer``, ``multi_instruction``, and ``multi_answer``. 

We briefly introduce their meaning:

- ``file``
    - The file names of the associated speech/audio data. 
    - You can use this column to match the speech/audio in ``audio/`` with corresponding question-answer pair.

- ``attribute_label``
    - The attribute label of the speech/audio data.
    - For instance, the kinds of animals in the Animal track.

- ``single_instruction``
    - The instruction for the associated single-hop questions.

- ``single_answer``
    - The golden answer of the single-hop questions.

- ``multi_instruction``
    - The instruction for the associated multi-hop questions.

- ``multi_answer``
    - The golden answer of the multi-hop questions.