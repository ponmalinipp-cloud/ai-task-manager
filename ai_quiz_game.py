"""
AI Adaptive Quiz Game
----------------------
A simple console-based Python project (no web/database needed).
The "AI" part: the game automatically adjusts question difficulty
based on how the player is performing (rule-based adaptive logic).
"""

import random

QUESTIONS = {
    "easy": [
        {"q": "What is the capital of India?", "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"], "answer": "Delhi"},
        {"q": "2 + 3 = ?", "options": ["4", "5", "6", "7"], "answer": "5"},
        {"q": "Which language runs in a web browser?", "options": ["Python", "Java", "JavaScript", "C++"], "answer": "JavaScript"},
    ],
    "medium": [
        {"q": "Which data structure uses FIFO order?", "options": ["Stack", "Queue", "Tree", "Graph"], "answer": "Queue"},
        {"q": "What does HTML stand for?", "options": ["Hyper Trainer Marking Language", "HyperText Markup Language", "HyperText Markdown Language", "Hyper Text Making Language"], "answer": "HyperText Markup Language"},
        {"q": "Which keyword defines a function in Python?", "options": ["func", "def", "function", "define"], "answer": "def"},
    ],
    "hard": [
        {"q": "What is the time complexity of binary search?", "options": ["O(n)", "O(n^2)", "O(log n)", "O(1)"], "answer": "O(log n)"},
        {"q": "Which of these is NOT a built-in Python data type?", "options": ["list", "dict", "array", "tuple"], "answer": "array"},
        {"q": "In Flask, which decorator defines a route?", "options": ["@app.url", "@app.route", "@app.path", "@app.link"], "answer": "@app.route"},
    ],
}


def ai_adjust_difficulty(current_level, streak):
    """
    Rule-based 'AI' logic (this is the AI feature of the project):
    - 2 correct answers in a row  -> level goes UP
    - 1 wrong answer              -> level goes DOWN
    - otherwise                   -> stays the same
    """
    levels = ["easy", "medium", "hard"]
    index = levels.index(current_level)

    if streak >= 2 and index < len(levels) - 1:
        index += 1
    elif streak <= -1 and index > 0:
        index -= 1

    return levels[index]


def ask_question(level):
    question = random.choice(QUESTIONS[level])
    print(f"\n[{level.upper()}] {question['q']}")
    for i, opt in enumerate(question["options"], 1):
        print(f"  {i}. {opt}")

    try:
        choice = int(input("Your answer (1-4): "))
        selected = question["options"][choice - 1]
    except (ValueError, IndexError):
        selected = None

    return selected == question["answer"], question["answer"]


def main():
    print("=" * 45)
    print(" AI ADAPTIVE QUIZ GAME ")
    print("=" * 45)
    print("Answer correctly to level UP. Answer wrong to level DOWN.\n")

    level = "easy"
    score = 0
    streak = 0
    total_questions = 5

    for round_num in range(1, total_questions + 1):
        print(f"\n--- Question {round_num}/{total_questions} ---")
        correct, answer = ask_question(level)

        if correct:
            print("Correct!")
            score += 1
            streak = max(streak, 0) + 1
        else:
            print(f"Wrong! Correct answer: {answer}")
            streak = min(streak, 0) - 1

        level = ai_adjust_difficulty(level, streak)

    print("\n" + "=" * 45)
    print(f" FINAL SCORE: {score}/{total_questions}")
    print("=" * 45)


if __name__ == "__main__":
    main()
