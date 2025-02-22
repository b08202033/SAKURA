import argparse
import json

def get_args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=str)
    return parser.parse_args()

def read_json_file(file_path):
    """Reads a JSON file and returns the data."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        raise ValueError(f"Error reading JSON file: {e}")

if __name__ == "__main__":
    args = get_args_parser()
    data = read_json_file(args.input)
    
    correct_count = 0
    incorrect_count = 0
    total_count = 0
    for k in data['results']:
        if data['results'][k]['Judgement'].lower().strip() == 'correct':
            correct_count += 1
        elif data['results'][k]['Judgement'].lower().strip() == 'incorrect':
            incorrect_count += 1
        else:
            print(f"Invalid judgement for key: {k}")
        total_count += 1
    
    print(f"Correct count: {correct_count}")
    print(f"Incorrect count: {incorrect_count}")
    print(f"Total count: {total_count}")
    print(f"Accuracy: {(correct_count / total_count)*100:.2f}%")