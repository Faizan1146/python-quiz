import json
import os
import random
import sys

class Quiz:
    def __init__(self):
        self.quiz = []
        if os.path.exists("question.json"):
            with open("question.json","r") as file:
                self.quiz = json.load(file)
        else:
            q = [
            {
                "id": 1,
                "question": "What does CPU stand for?",
                "answer": "Central Processing Unit",
                "category": "CS",
                "difficulty": "Easy"
            },
            {
                "id": 2,
                "question": "What keyword is used to define a function in Python?",
                "answer": "def",
                "category": "Python",
                "difficulty": "Easy"
            },
            {
                "id": 3,
                "question": "What is the output of 2 ** 3 in Python?",
                "answer": "8",
                "category": "Python",
                "difficulty": "Easy"
            },
            {
                "id": 4,
                "question": "What is the SI unit of force?",
                "answer": "Newton",
                "category": "Physics",
                "difficulty": "Easy"
            },
            {
                "id": 5,
                "question": "What is the acceleration due to gravity on Earth approximately?",
                "answer": "9.8 m/s²",
                "category": "Physics",
                "difficulty": "Medium"
            },
            {
                "id": 6,
                "question": "What data structure stores key-value pairs in Python?",
                "answer": "Dictionary",
                "category": "Python",
                "difficulty": "Medium"
            },
            {
                "id": 7,
                "question": "What does RAM stand for?",
                "answer": "Random Access Memory",
                "category": "CS",
                "difficulty": "Easy"
            },
            {
                "id": 8,
                "question": "Which planet is known as the Red Planet?",
                "answer": "Mars",
                "category": "General Knowledge",
                "difficulty": "Easy"
            },
            {
                "id": 9,
                "question": "What is the time complexity of binary search on a sorted array?",
                "answer": "O(log n)",
                "category": "CS",
                "difficulty": "Hard"
            },
            {
                "id": 10,
                "question": "What is Newton's second law of motion?",
                "answer": "F = ma",
                "category": "Physics",
                "difficulty": "Medium"
            }
            ]  
            
            self.quiz = q
            with open("question.json","w") as file:
                json.dump(self.quiz,file) 

            


    def add_questions(self):
        print("Question cannot be empty.\nAnswer cannot be empty.\nCategory must be valid.\nDifficulty must be Easy, Medium, or Hard.")
        t_dict = {}
        # Id = int(input("Enter ID: "))
        question = input("Enter question: ")
        answer = input("Enter answer: ")
        category = input("Enter category: ")
        difficulty = input("Enter difficulty: ")

        if self.quiz:
            new_id = max(question["id"] for question in self.quiz) + 1
        else:
            new_id = 1
        t_dict["id"] = new_id
        t_dict["question"] = question
        t_dict["answer"] = answer
        t_dict["category"] = category
        t_dict["difficulty"] = difficulty
        self.quiz.append(t_dict)

        with open("question.json", "w") as file:
            json.dump(self.quiz,file)

    def view_questions(self):
        for question_view in self.quiz:
            for key,value in question_view.items():
                print(f"{key} : {value}")
            

    def start_quiz(self,que,category1,difficulty1):
        score = 0
        if category1 == '1':
            try:
                filtered_question = [ q for q in self.quiz if q["difficulty"].lower() == difficulty1.lower() ]
                num_of_q = random.sample(filtered_question , que)
                for q in num_of_q:
                    print(q["question"])
                    ans = input("Enter answer: ")
                    if ans.lower() == q["answer"].lower():
                        print("correct")
                        score +=1
                    else:
                        print("incorrect")
        
                return score

            except ValueError:
                print("The number of questions aren't present")
        else:
            try:
                filtered_question = [ q for q in self.quiz if q["category"].lower() == category1.lower() ]
                filtered_question = [ q for q in filtered_question if q["difficulty"].lower() == difficulty1.lower() ]
                num_of_q= random.sample(filtered_question , que)
                for q in num_of_q:
                    print(q["question"])
                    ans = input("Enter answer: ")
                    if ans.lower() == q["answer"].lower():
                        print("correct")
                        score +=1
                    else:
                        print("incorrect")
        
                return score

            except ValueError:
                print("The number of questions aren't present")

    def delete_question(self):
        found = False
        user_id = int(input("Enter id of the question you want to delete: "))
        for question_del in self.quiz:
            if question_del["id"] == user_id:
                self.quiz.remove(question_del)
                found = True
                with open("question.json","w") as file:
                    json.dump(self.quiz,file)
        if found == False:
            print("ID not Found")

    def search_question(self):
        found = False
        print("===== SEARCH EXPENSES =====")
        print("1. Search by Category\n2. Search by difficulty\n3. Search by Question\n4. Search by Answer\n5. ID")
        ch = int(input("Choose"))
        if ch == 1:
            Category = input("Enter category: ").lower()
            for question_search in  self.quiz:
                if  question_search["category"].lower() == Category:
                    # print(question)
                    found = True
                    for key, value in question_search.items():
                        print(f"{key} : {value}")
            if found == False:
                print("Category not found")

        elif ch == 2:
            Difficulty = input("Enter Difficulty: ").lower()
            for question_search in  self.quiz:
                if  question_search["difficulty"].lower() == Difficulty:
                    # print(question)
                    found = True
                    for key, value in question_search.items():
                        print(f"{key} : {value}")
            if found == False:
                print( "difficulty not found")
        
        elif ch == 3:
            Question = input("Enter question: ").lower()
            for question_search in  self.quiz:
                if  question_search["question"].lower() == Question:
                    # print(question)
                    found = True
                    for key, value in question_search.items():
                        print(f"{key} : {value}")
            if found == False:
                print("Question not found")

        elif ch == 4:
            Answer = input("Enter answer: ").lower()
            for question_search in  self.quiz:
                if  question_search["answer"].lower() == Answer:
                    # print(question)
                    found = True
                    for key, value in question_search.items():
                        print(f"{key} : {value}")
            if found == False:
                print("Answer not found")

        elif ch == 5:
            Id = int(input("Enter id: "))
            for question_search in  self.quiz:
                if Id == question_search["id"]:
                    # print(question)
                    found = True
                    for key, value in question_search.items():
                        print(f"{key} : {value}")
            if found == False:
                print("ID not found")
        
        else:
            print("Choose from the given option")




def main():
    quiz = Quiz()
    while True:
        print("===Main Menu===")
        print("1. Start Quiz\n2. Add Question\n3. View Questions\n4. Delete Question\n5. Search Questions\n6. Exit")
        c = int(input("Choose:"))

        if c == 1:
            ques = int(input("How many questions? "))
            print("Choose category:\nAll\nPython\nCS\nPhysics\nGeneral Knowledge")
            cat = (input("Choose category: "))
            print("Difficulty:\nEasy\nMedium\nHard")
            diff = input("Enter difficulty: ")


            score = quiz.start_quiz(ques,cat,diff)
            print(f"Final score: {score}/{ques}")

        elif c == 2:
            quiz.add_questions()

        elif c == 3:
            quiz.view_questions()

        elif c == 4:
            quiz.delete_question()

        elif c == 5:
            quiz.search_question()

        elif c == 6:
            sys.exit()

        else:
            raise ValueError("Choose from give options")

if __name__ == "__main__":
    main()