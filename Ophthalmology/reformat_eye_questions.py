import csv
import re

with open('Eye orbit and eyelid.docx.txt', 'r') as file:
    lines = file.readlines()

with open('ophthalmology_questions_out.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Question", "Answer_choice", "Correct_or_not"])

    question = ""
    options = []
    for line in lines:
        line = line.strip()

        if re.match(r"^\d+\.", line):
            if question:
                for option in options:
                    writer.writerow([question, option, int(option[0] == answer)])
            question = line
            options = []
        elif re.match(r"^[A-E]\.", line):
            options.append(line)
        elif re.match(r"^Answer:", line):
            answer = line.split(": ")[1]

    for option in options:
        writer.writerow([question, option, int(option[0] == answer)])
