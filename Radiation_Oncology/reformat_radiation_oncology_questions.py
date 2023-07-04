import re
import pandas as pd

filename = 'radiation_oncology_questions.txt'

with open(filename, 'r') as f:
    lines = f.readlines()

formatted_questions = []
answer_choices = []
q_text = None

for line in lines:
    line = line.strip()

    if re.match(r'^\d+\.', line):
        if q_text is not None:
            formatted_questions.append((q_text, answer_choices))
            answer_choices = []
        q_text = line

    elif re.match(r'^[A-E]\.', line):
        answer_choices.append(line)

if q_text is not None and answer_choices:
    formatted_questions.append((q_text, answer_choices))

df = pd.DataFrame(columns=['Question', 'Answer_choice', 'Correct_or_not'])

correct_answers = ['C', 'A', 'B', 'A', 'B', 'D', 'B', 'A', 'C', 'A', 'D', 'A', 'D', 'C', 'A', 'A', 'E', 'C', 'C', 'D', 'D', 'C', 'A', 'A', 'D', 'C', 'B',
                   'D', 'C', 'A', 'D', 'D', 'A', 'B', 'C', 'A', 'D', 'C', 'A', 'C', 'D', 'C', 'A', 'C', 'D', 'B', 'A', 'B', 'C', 'B', 'B', 'D', 'C', 'A', 'C', 'A', 'C', 'B', 'C', 'C',
                   'A', 'D', 'B', 'D', 'A', 'C', 'B', 'B', 'A', 'D', 'C', 'D', 'C', 'C', 'A', 'B', 'D', 'C', 'A', 'B', 'C', 'D', 'C', 'A', 'A', 'B', 'C', 'A', 'D', 'C', 'B', 'C', 'A',
                   'C', 'A', 'A', 'C', 'D', 'C', 'B']

for idx, (q_text, answer_choices) in enumerate(formatted_questions):
    for choice_idx, choice in enumerate(answer_choices):
        correct_or_not = 1 if choice[0] == correct_answers[idx] else 0
        df = df.append({'Question': q_text, 'Answer_choice': choice, 'Correct_or_not': correct_or_not}, ignore_index=True)

print(df)

df.to_csv("radiation_oncology_out.csv", index=False)
