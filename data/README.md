# Dataset

Here contains the dataset of all the four tracks of SAKURA.

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