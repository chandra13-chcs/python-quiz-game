import tkinter as tk

# ---------------- DATA ----------------
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "If a batsman scores a boundary (4), how many runs are added?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B"
    },
    {
        "question": "If a bowler bowls 6 legal balls, it is called?",
        "options": ["A. Spell", "B. Over", "C. Session", "D. Set"],
        "answer": "B"
    },
    {
        "question": "If all cats are animals and some animals are black, are all cats black?",
        "options": ["A. Yes", "B. No", "C. Maybe", "D. Cannot say"],
        "answer": "D"
    },
    {
        "question": "Which number comes next: 2, 4, 8, 16, ?",
        "options": ["A. 18", "B. 24", "C. 32", "D. 64"],
        "answer": "C"
    },
    {
        "question": "If today is Monday, what day will it be after 10 days?",
        "options": ["A. Wednesday", "B. Thursday", "C. Friday", "D. Saturday"],
        "answer": "B"
    },
    {
        "question": "Which situation gives a batsman out 'LBW'?",
        "options": [
            "A. Ball hits bat first",
            "B. Ball hits pad outside leg stump",
            "C. Ball hits pad in line and would hit stumps",
            "D. Ball hits helmet"
        ],
        "answer": "C"
    },
    {
        "question": "Which language is this quiz written in?",
        "options": ["A. Java", "B. C++", "C. Python", "D. HTML"],
        "answer": "C"
    },
    {
        "question": "What will be the output of: print(2 + 3 * 4)?",
        "options": ["A. 20", "B. 14", "C. 24", "D. 9"],
        "answer": "B"
    },
    {
        "question": "Which condition will run the code inside an if statement?",
        "options": ["A. True", "B. False", "C. None", "D. 0"],
        "answer": "A"
    },
    {
        "question": "What is the result of: 10 // 3?",
        "options": ["A. 3.33", "B. 3", "C. 4", "D. 10"],
        "answer": "B"
    },
    {
        "question": "Which loop is best when you don't know how many times to repeat?",
        "options": ["A. for", "B. while", "C. if", "D. print"],
        "answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Power Unit",
            "C. Central Program Utility",
            "D. Control Processing Unit"
        ],
        "answer": "A"
    }
]

current_question = 0
score = 0

# ---------------- FUNCTIONS ----------------
def load_question():
    question_label.config(text=questions[current_question]["question"])

    for i in range(4):
        option_buttons[i].config(
            text=questions[current_question]["options"][i],
            command=lambda opt=questions[current_question]["options"][i]: check_answer(opt)
        )

def check_answer(selected):
    global score, current_question

    # Get first letter from selected option
    selected_letter = selected[0].upper()
    correct_letter = questions[current_question]["answer"].upper()

    if selected_letter == correct_letter:
        score += 1

    current_question += 1

    if current_question < len(questions):
        load_question()
    else:
        show_result()

def show_result():
    question_label.config(
        text=f"Quiz Finished!\n\nScore: {score}/{len(questions)}"
    )

    for btn in option_buttons:
        btn.pack_forget()

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Quiz App")
root.geometry("400x300")

question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=350)
question_label.pack(pady=20)

option_buttons = []
for i in range(4):
    btn = tk.Button(root, text="", width=30)
    btn.pack(pady=5)
    option_buttons.append(btn)

load_question()
root.mainloop()
