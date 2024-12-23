import json

questions_not_split = {}

with open("batchResults.jsonl", "r") as file:
    for line in file:
        record = json.loads(line)
        key = record.get("id")
        questions_not_split[key] = record

questions = []
for key, record in questions_not_split.items():
    current_questions = record.get('response', {}).get('body', {}).get('choices', [])[0].get('message', {}).get('content', "")
    current_questions = current_questions.replace("\n", "")
    last_question = False
    while(not last_question):
        context = current_questions[current_questions.find("Context: ")+9:current_questions.find("Question: ")].rstrip()
        current_questions = current_questions[current_questions.find("Question: "):]
        question = current_questions[current_questions.find("Question: ")+10:current_questions.find("Options: ")].rstrip()
        current_questions = current_questions[current_questions.find("Options: ")+8:]
        options = [
            current_questions[current_questions.find("(A) ")+4:current_questions.find("(B) ")],
            current_questions[current_questions.find("(B) ")+4:current_questions.find("(C) ")],
            current_questions[current_questions.find("(C) ")+4:current_questions.find("(D) ")],
            current_questions[current_questions.find("(D) ")+4:current_questions.find("Answer: ")]
        ]
        for i in range(len(options)):
            option = options[i]
            if option[-2:] == ", ":
                options[i] = option[:-3]
            if option[-1:] == " ":
                options[i] = option[:-2]
        current_questions = current_questions[current_questions.find("Answer: "):]
        answer = current_questions[current_questions.find("Answer: (")+9:current_questions.find(")")]
        if answer == "A":
            answer = 1
        elif answer == "B":
            answer = 2
        elif answer == "C":
            answer = 3
        elif answer == "D":
            answer = 4
        current_questions = current_questions[current_questions.find("Explanation: "):]
        explanation = current_questions[current_questions.find("Explanation: ")+13:current_questions.find("Context: ")].rstrip()
        questions.append({"ek_sp_key": record.get("custom_id"), "context": context, "question": question, "options": options, "answer": answer, "explanation": explanation})
        if current_questions.find("Context: ") == -1:
            last_question = True
with open("finalQuestions.json", "w") as file:
    json.dump(questions, file, indent=4)