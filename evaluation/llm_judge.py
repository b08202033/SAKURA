import os
import re
import json
from openai import OpenAI
from tqdm import tqdm
import argparse

def get_args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=str, help="Input file path")
    parser.add_argument('--output_dir', '-o', type=str)
    return parser.parse_args()

def read_json_file(file_path):
    """Reads a JSON file and returns the data."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        raise ValueError(f"Error reading JSON file: {e}")

def save_dict_to_json(dictionary, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(dictionary, json_file, ensure_ascii=False, indent=4)
        print(f"Saved: {file_path}")
    except Exception as e:
        print(f"Failed: {e}")

def check_and_create_folder(folder_path):
    """
    Check if a folder exists, and create it if it doesn't.

    Args:
        folder_path (str): The path to the folder to check or create.
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created.")
    else:
        print(f"Folder '{folder_path}' already exists.")

def query_llm(client, user_prompt, model_name="gpt-4o-2024-11-20", temperature=0.0, top_p=1.0):

    system_prompt = '''You are a good judge. You will be given a question with list of possible options, a ground truth answer and a model generated response. 
                       You have to determine whether the model generated answer is correct.'''

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            }
        ],
        model=model_name,
        temperature=temperature,
        top_p=top_p
    )

    return chat_completion.choices[0].message.content

def extract_judgement(text):
    pattern = r"Explanation: (.*?)\nJudgement: (.*?)(?:\n\n|$)"
    match = re.search(pattern, text, re.DOTALL)

    if match:
        explanation = match.group(1)
        judgement = match.group(2)
    else:
        explanation = "No extracted explanation"
        judgement = "No extracted judgement"
    
    results = {"Explanation": explanation, "Judgement": judgement}
    return results

if __name__ == "__main__":
    args = get_args_parser()
    check_and_create_folder(args.output_dir)
    
    openai_api_key = "<your_openai_api_key>"
    client = OpenAI(api_key=openai_api_key)

    # the parameter setting used in the original paper
    model_name = "gpt-4o-2024-11-20"
    temperature = 0.0
    top_p = 0.9
    max_tokens = 1024

    user_prompt_template = '''
    You will be given a question with list of possible options, a ground truth answer and a model generated response. Determine whether the model generated response is correct based on the following criteria:
    1. Since there is one and only one corect answer, it should be judged incorrect if the model do not choose any option from the option list or it choose more than one option.
    2. If the model choose one option from the option list, it should be judged correct if the chosen option aligns with the ground truth answer, otherwise it should be judged incorrect.
    3. Read the question, options, ground truth answer and model generated response carefully before making a decision.

    Considering the following examples:
    Question: What is the capital of France? (a) Paris (b) London (c) Berlin (d) Madrid
    Ground truth answer: (a) Paris
    If the model generated response is: "The capital of France is Tokyo.", it should be judged incorrect since it does not choose any option from the option list.
    If the model generated response is: "The capital of France is Paris and London.", it should be judged incorrect since it chooses more than one option from the option list.
    If the model generated response is: "The capital of France is London.", it should be judged incorrect since it chooses one option from the option list but the chosen option does not align with the ground truth answer.
    If the model generated response is: "The capital of France is Paris.", it should be judged correct since it chooses one option from the option list and the chosen option aligns with the ground truth answer.
    Another Question: What is the underlying emotion of the speaker? (a) Happy (b) Sad (c) Angry (d) Neutral
    Ground truth answer: (a) Happy
    If the model generated response is: "The speaker is happy.", it should be judged correct since it chooses one option from the option list and the chosen option aligns with the ground truth answer.
    If the model generated response is: "The speaker expresses happiness.", it should be judged correct since "happiness" aligns with the ground truth answer "happy", and they are just different part of speech of the same word.
    If the model generated response is: "Happiness," it should be judged correct since it is also a valid derivative of the ground truth answer "happy".
    
    Now here is the question and the model generated response for you to judge:
    Question: [QUESTION]
    Ground truth answer: [GROUND_TRUTH_ANSWER]
    Model generated response: [MODEL_GENERATED_RESPONSE]

    Carefully make your decision based on the above criteria. Return your judgement with the following format:
    Explanation: <Your explanation on your judgement>
    Judgement: <Your judgement, either "correct" or "incorrect">
    '''

    model_responses = read_json_file(args.input)
    judgements = {}
    judgements['judge_model'] = model_name
    judgements['temperature'] = temperature
    judgements['top_p'] = top_p
    judgements['max_tokens'] = max_tokens
    judgements['results'] = {}
    
    for wav_file in tqdm(model_responses['results'].keys()):
        question = model_responses['results'][wav_file]['instruction']
        response = model_responses['results'][wav_file]['response']
        ground_truth_answer = model_responses['results'][wav_file]['label']
        user_prompt = user_prompt_template.replace("[QUESTION]", question).replace("[MODEL_GENERATED_RESPONSE]", response).replace("[GROUND_TRUTH_ANSWER]", ground_truth_answer)

        judgement = query_llm(client, user_prompt, model_name=model_name, temperature=temperature, top_p=top_p)
        results = extract_judgement(judgement)

        results['instruction'] = question
        results['model_response'] = response
        results['label'] = ground_truth_answer
        judgements['results'][wav_file] = results
    
    save_dict_to_json(judgements, os.path.join(args.output_dir, os.path.basename(args.input).replace(".json", "_judgements.json")))