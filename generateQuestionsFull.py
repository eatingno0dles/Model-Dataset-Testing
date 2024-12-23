import google.generativeai as genai
import formatter as formatter
import json

genai.configure(api_key="")
model = genai.GenerativeModel(
    model_name="gemini-exp-1206",
    system_instruction="You are an assistant that creates multiple-choice questions for AP Chemistry. In AP Chemistry there are 9 units, and each has some subunits. Each subunit has 1 or 2 learning objectives and each learning objective has 1-6 essential knowledge statements. A learning objective is denoted like 1.1.A, 1.1. A is the only learning objective for subunit 1.1. An essential knowledge statement is denoted as 1.1.A.1 or 1.1.A.2, both of which are essential knowledges for learning objective 1.1.A. There is also something called Science practices, and there are 5 sections each with a few subsections for MCQs, 1, 2, 4, 5 and 6. A science practice is denoted as 1.A or 1.B, or 5.E or 5.F. Each MCQ should have an essential knowledge statement and science practice tied to it. All of this info and the questions above are from the AP Chemistry Course and Exam Description (CED), which will be attached to the question. The AP Chem CED also has a bunch of sample multiple choice questions to help inspire the questions you generate. An example of the format you should answer in is: 'Context: 1s2 2s2 2p6 3s2 3p6\nQuestion: Which of the following species has the electron configuration shown above?\nAnswer: K+\nExplanation: (explanation would be here)\nOptions:(A) O, (B) Ne, (C) K+, (D) Cl+\nEssential Knowledge: 1.5.A.3, Question SP: 1.A'. Context would be something that would be shown above the question like a graph, table or just a string of text like shown above, or any combination of these. Another example of a question (this one with multiple objects of context) is: 'Context: HCl(aq) + CaCO3(s) → CaCl2(aq) + CO2(g) + H2O(l), The reaction between HCl(aq) and CaCO3(s) is represented by the equation above. Two separate trials were carried out using CaCO3(s) samples of the same mass, but one sample was a single piece of CaCO3(s), and one sample was composed of small pieces of CaCO3(s). The loss of mass of CaCO3(s) as a function of time for both trials is shown in the graph below. ElementDesc[Type: Graph, Specifications: Graph with the y-axis labeled Loss of Mass of CaCO₃(s) (g) and the x-axis labeled Time (s). It shows two curves, labeled X and Y. Curve Y rises steeply at first, then levels off. Curve X rises more gradually and also levels off, but at a lower point than Curve Y.]\nQuestion: Which of the curves, X or Y, represents the reaction with small pieces of CaCO3(s), and why?, Answer: Curve Y, because it takes a shorter time for the reaction to go to completion due to the larger surface area of CaCO3(s)\nExplanation: Small pieces of CaCO₃ have a larger surface area compared to a single large piece of the same mass. A larger surface area increases the rate of reaction because more surface area is available for collisions with HCl molecules. This leads to a faster reaction, as seen in Curve Y, which rises steeply and levels off more quickly, indicating that the reaction reaches completion in a shorter time.\nOptions: (A) Curve X, because it shows that the reaction proceeded at a uniform rate, (B) Curve X, because it takes a shorter time for the reaction to go to completion due to the larger surface area of CaCO3(s), (C) Curve Y, because it shows that the reaction proceeded at a nonuniform rate, (D) Curve Y, because it takes a shorter time for the reaction to go to completion due to the larger surface area of CaCO3(s)\nEssential Knowledge: 5.1.A.3\nQuestion SP: 6.F'. You don't need to provide context if the question does not require it. You will be given a learning objective, essential knowledge statement, and science practice and you will be asked to generate questions. None of the questions should be numbered, even if the user asks to 'generate 5 questions...', there should just be 5 questions. If there is no context there should be 'Context: None' before the question. Nothing should be bolded or anything like that. The sections in the question should always be 'Context, Question, Answer, Explanation, Options, Essential Knowledge, Question SP', and it shouldn't be something like 'Science Practice'."
)
CED = genai.upload_file("ap-chemistry-course-and-exam-description.pdf")
def generate_questions(multiple):
    questions = []
    count = 0
    for i in formatter.data:
        if i.essential_knowledge[0:28].find(":") != -1:
            first_part_essential_knowledge = i.essential_knowledge[0:27]
        else:
            first_part_essential_knowledge = i.essential_knowledge[0:28]
        other_essential_knowledge = []
        for j in formatter.data:
            if j.topic == i.topic:
                if not(i.essential_knowledge == j.essential_knowledge):
                    other_essential_knowledge.append(j.essential_knowledge)
        prompt = f"Create {multiple} multiple choice questions for subunit {i.topic}, {first_part_essential_knowledge}, and {i.recommended_practice[0:20]}. The learning objective is '{i.learning_objective}'. The essential knowledge is '{i.essential_knowledge}'. The science practice is '{i.recommended_practice}'. When crafting the {multiple} multiple choice questions consider the learning objective, essential knowledge, and science practice. Also, your questions can relate to the other essential knowledges in the subunit. For {i.topic}, the other essential knowledge(s) are: '{other_essential_knowledge}'. You can also use any perquisite knowledge of topics done before this topic. This includes the previous topics in this unit, and also all of the topics from the units prior. Some of the learning objectives will relate more than others. You can have questions that require knowledge from other essential knowledges and topics (only topics BEFORE the topic being generated for), but the main focus should be {first_part_essential_knowledge}. You should not have things in the question that are ahead of the learning objectives/topics mentioned.  Each question should have 4 options and an answer. For each of them, provide an explanation for the answer. Your explanation should not involve the essential knowledge, learning objective, or science practice, it should be more of an explanation of why the correct answer is correct. If the question needs some kind of diagram, you may add context. Context is not always needed. It would be like a diagram, graph, or particle diagram that was needed for the problem. Context should usually just be descriptions of diagrams, tables, or graphs. Also, context should not include some kind of prerequisite knowledge about chemistry. If there is some kind of image, graph, or table that is in context, use the shorthand ElementDesc[], filling in the square brackets with the description, to denote the element. Do not confuse context with the question itself, like I said, sometimes context isn't even needed. If context can just be included in the question do not add it. There should not be things like molar masses of elements given in the question, because that is on the periodic table. If you were to write like 'a substance with a molar mass of 16 grams' you can instead just write oxygen, because the person answering the questions will have a periodic table. Create all {multiple} questions, don't stop in the middle. All of the questions need to be generated. The questions should be as difficult as possible, (AP style, and like the ones provided in the system instructions), and they shouldn't be answerable with a quick glance at the Essential Knowledge. The math related ones should use difficult numbers and most of them shouldnt be solvable with mental math. Unless you specify in the question, there should be no questions that try to 'account for error' by having the correct calculated answer in one of the options, and then a different correct answer with the justification that measurement error exists, and the same thing applies with rounding. There should be barely any rounding necessary, the correct answer should just be the correct answer. Add another section before options that is just the correct answer to the question (not a letter). Very important: Include the answer and explanation sections BEFORE the options. Also important: Make sure that one of the options matches the answer provided before the options, directly. Most important of all: make sure that the correct answer provided is actually correct."
        print(f"Generating questions for {i.topic}, {first_part_essential_knowledge}, and {i.recommended_practice[0:20]}")
        response = model.generate_content([prompt, CED])
        print(response.text)
        current_questions = response.text
        with open("final_Questions.json", "w") as file:
            json.dump(current_questions, file, indent=4)
        current_questions = current_questions.replace("\n", "")
        last_question = False
        while(not last_question):
            context = current_questions[9:current_questions.find("Question: ")].rstrip()
            current_questions = current_questions[current_questions.find("Question: "):]
            question = current_questions[10:current_questions.find("Answer: ")].rstrip()
            current_questions = current_questions[current_questions.find("Answer: "):]
            answer = current_questions[8:current_questions.find("Explanation: ")].rstrip()
            current_questions = current_questions[current_questions.find("Explanation: "):]
            explanation = current_questions[13:current_questions.find("Options: ")].rstrip()
            current_questions = current_questions[current_questions.find("Options: ")+8:]
            options = [
             current_questions[current_questions.find("(A) ")+4:current_questions.find("(B) ")],
                current_questions[current_questions.find("(B) ")+4:current_questions.find("(C) ")],
                current_questions[current_questions.find("(C) ")+4:current_questions.find("(D) ")],
                current_questions[current_questions.find("(D) ")+4:current_questions.find("Essential Knowledge: ")]
            ]
            for i in range(len(options)):
                option = options[i]
                if option[-2:] == ", ":
                    options[i] = option[:-3]
                if option[-1:] == " ":
                    options[i] = option[:-2]
            current_questions = current_questions[current_questions.find("Essential Knowledge: "):]
            essential_knowledge = current_questions[20:current_questions.find("Question SP: ")].rstrip()
            current_questions = current_questions[current_questions.find("Question SP: "):]
            if last_question:
                science_practice = current_questions[13:].rstrip()
            else:
                science_practice = current_questions[13:current_questions.find("Context: ")].rstrip()
                current_questions = current_questions[current_questions.find("Context: "):]
            questions.append({"essential_knowledge": essential_knowledge, "science_practice": science_practice, "context": context, "question": question, "options": options, "answer": answer, "explanation": explanation})
            if current_questions.find("Context: ") == -1:
                last_question = True
        count += 1
        if count == 3:
            break
    with open("final_Questions.json", "w") as file:
        json.dump(questions, file, indent=4)
    return f"Generated {len(formatter.data)*multiple} questions"

print(generate_questions(3))