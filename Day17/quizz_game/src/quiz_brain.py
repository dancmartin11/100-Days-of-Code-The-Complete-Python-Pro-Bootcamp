#Create class that will execute the logic of the game
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0 #Initial position
        self.score = 0
        self.question_list = question_list
    
    #Validate if there are more questions
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    #Validate if the user answer is correct and increase score if needed
    def check_answer(self, user_answer, correct_answer):
        if user_answer.strip().lower() == correct_answer.strip().lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong. ")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
    
    #Execute the next question for the user to answer    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False):\n")
        self.check_answer(user_answer, current_question.answer)
    
        