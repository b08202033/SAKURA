# Evaluation
Here is the code for our LLM-based evaluation.

## Usage
``llm_judge.py`` contains the evaluation pipeline, and ``calculate_acc.py`` contains the script to compute the accuracy based on the judgement. Here, we briefly describe how to use it.

### Step 0: Setup
Make sure you have installed the following packages:
```
pip install tqdm==4.66.4
pip install openai==1.33.0
```
In addition, please fill in your OpenAI API key in the line 85:
```
openai_api_key = "<your_openai_api_key>"
```

### Step 1: Run Your Own Model
Run your own model on SAKURA and save the model response in ``<model_name>.json`` with the following format:
```
{
    "attribute": "<the attribute of the track>",
    "type": "<the sub-track you run, either single or multi>",
    "results": {
        "<file path of audio 1>":{
            "instruction": "<the original instruction>",
            "response": "<the model response>",
            "label": "<the golden answer>"
        },
        "<file path of audio 2>":{
            "instruction": "<the original instruction>",
            "response": "<the model response>",
            "label": "<the golden answer>"
        },
        ...
    }
}
```

Especially, the ``instruction`` and ``label`` will be used as the input to the LLM evaluator, so it will be more convenient if they are also saved when during the inference of your model.

### Step 2: Run the LLM-based Evaluator
Run the evaluation script:
```
python llm_judge.py -i <model_name>.json -o <the output directory you want>
```
The script will return a file ``<model_name>_judgements.json`` in the entered output directory, with the following format:

```
{
    "judge_model": "<the judge model used>",
    "temperature": <the temperature used>,
    "top_p": <the top_p parameter used>,
    "max_tokens": <the max_token parameter used>,
    "results": {
        "<file path of audio 1>":{
            "Explanation": "<the explanation of the judgement>",
            "Judgement": "<the final judgement, ideally either correct or incorrect>"
            "instruction": "<the original instruction>",
            "response": "<the model response>",
            "label": "<the golden answer>"
        },
        "<file path of audio 2>":{
            "instruction": "<the original instruction>",
            "response": "<the model response>",
            "label": "<the golden answer>"
        },
        ...
    }
}
```

Please note that if the evaluator does not follow the evaluation guidelines such that we cannot parse the explanation or the judgement, the corresponding value will be "No extracted explanation" and "No extracted judgement". 

If this is the case, manual verification on the model response will be necessary.

### Step 3: Compute the Accuracy
Run ``calculate_acc.py`` to compute the accuracy:
```
python calculate_acc.py -i <model_name>_judgements.json
```

The final accuracy will be printed.

Please note that if the "Judgement" values not "correct" or "incorrect", the script will print the corresponding audio file name, and manual check will be required to fix it. 

If you encounter this problem, the final accuracy should be computed again by running ``calculate_acc.py`` after you fix the judgements.