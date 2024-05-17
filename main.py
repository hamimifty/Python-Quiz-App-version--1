# main.py
import openpyxl
from openpyxl import Workbook
import os
from pathlib import Path

class Quiz:
    def __init__(self, subject="Geography and General Knowledge"):
        self.subject = subject
        self.filepath = os.path.join(Path.home(), "Desktop", "quiz_results.xlsx")
        self.questions = [
            {"question": "What is the capital of Bangladesh?", "answer": "Dhaka", "options": ["Dhaka", "Sylhet", "Chittagong", "Khulna"]},
            {"question": "Which river flows through Sylhet?", "answer": "Surma", "options": ["Surma", "Padma", "Meghna", "Jamuna"]},
            {"question": "What is the national language of Bangladesh?", "answer": "Bengali", "options": ["Hindi", "Bengali", "English", "Urdu"]},
            {"question": "Which country has the largest population?", "answer": "China", "options": ["India", "USA", "Indonesia", "China"]},
            {"question": "Which is the tallest mountain in the world?", "answer": "Mount Everest", "options": ["K2", "Kangchenjunga", "Mount Everest", "Lhotse"]},
            {"question": "What is the currency of Bangladesh?", "answer": "Taka", "options": ["Rupee", "Taka", "Dollar", "Euro"]},
            {"question": "Which city is known as the 'Tea Capital' of Bangladesh?", "answer": "Sylhet", "options": ["Dhaka", "Chittagong", "Sylhet", "Khulna"]},
            {"question": "Which is the largest ocean in the world?", "answer": "Pacific Ocean", "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"]},
            {"question": "What is the national flower of Bangladesh?", "answer": "Water Lily", "options": ["Rose", "Sunflower", "Marigold", "Water Lily"]},
            {"question": "Which country is known as the Land of the Rising Sun?", "answer": "Japan", "options": ["China", "Japan", "Korea", "Thailand"]},
            {"question": "What is the largest continent by area?", "answer": "Asia", "options": ["Africa", "Europe", "Asia", "Australia"]},
            {"question": "Which city in Sylhet is famous for its shrine?", "answer": "Hazrat Shah Jalal Shrine", "options": ["Hazrat Shah Jalal Shrine", "Baitul Mukarram", "Star Mosque", "Ahsan Manzil"]},
            {"question": "What is the national animal of Bangladesh?", "answer": "Royal Bengal Tiger", "options": ["Lion", "Elephant", "Royal Bengal Tiger", "Deer"]},
            {"question": "Which planet is known as the Red Planet?", "answer": "Mars", "options": ["Venus", "Mars", "Jupiter", "Saturn"]},
            {"question": "What is the main religion in Bangladesh?", "answer": "Islam", "options": ["Christianity", "Hinduism", "Buddhism", "Islam"]}
        ]

    def add_question(self, question, answer, options):
        self.questions.append({"question": question, "answer": answer, "options": options})

    def get_subject(self):
        return self.subject

    def get_questions(self):
        return self.questions

    def save_results(self, student_name, answers, score, percentage):
        # Ensure the file exists and has the correct header
        if not os.path.exists(self.filepath):
            workbook = Workbook()
            sheet = workbook.active
            sheet.title = self.subject
            sheet.append(["Student Name", "Question", "Answer", "Correct Answer", "Score", "Percentage"])
            workbook.save(self.filepath)

        workbook = openpyxl.load_workbook(self.filepath)
        sheet = workbook.active

        for i, question in enumerate(self.questions):
            sheet.append([
                student_name,
                question["question"],
                answers[i] if answers[i] is not None else "",
                question["answer"],
                score if i == 0 else "",  # Only write score once
                f"{percentage:.2f}%" if i == 0 else ""  # Only write percentage once
            ])
        
        workbook.save(self.filepath)

if __name__ == "__main__":
    quiz = Quiz()
    # Print all questions to verify
    for q in quiz.get_questions():
        print(q)
