import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from formula import FORMULAS

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En production : mettre ton domaine
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def generate_wrong_answers(formula_entry, order):
    wrong_answers = []
    generator = formula_entry["formula_order"]

    if generator is None:
        return []

    wrong_answers.append(generator(order + 1))

    if order > 2:
        wrong_answers.append(generator(order - 1))
    else:
        wrong_answers.append(generator(order + 2))

    return wrong_answers

@app.get("/question")
def generate_question():

    formula_entry = random.choice(FORMULAS)
    order = random.randint(2, 6)

    if formula_entry["formula_order"] is not None:
        correct_answer = formula_entry["formula_order"](order)
    else:
        correct_answer = formula_entry["formula"]

    wrong_answers = generate_wrong_answers(formula_entry, order)

    while len(wrong_answers) < 2:
        wrong_answers.append(correct_answer + "+x")

    all_answers = wrong_answers + [correct_answer]
    random.shuffle(all_answers)

    return {
        "question_text": f"Donner le développement limité à l'ordre {order} en 0 de :",
        "question_latex": formula_entry["name"],
        "answers": all_answers,
        "correct_answer": correct_answer
    }