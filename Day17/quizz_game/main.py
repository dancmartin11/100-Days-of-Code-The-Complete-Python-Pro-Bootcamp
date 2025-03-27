#Import created objects and modules
from src.question_model import Question
from data.game_data import question_data
from src.quiz_brain import QuizBrain

#Empty list with question bank
question_bank = []

#Iterate over question data to fill in bank
for i in question_data:
    q = Question(text = i['text'],  answer = i['answer'])
    question_bank.append(q)

#Initialize the quiz game
quiz = QuizBrain(question_bank)

#Execute questions and validate score
while quiz.still_has_questions():    
    quiz.next_question()

#Get final score and print results
print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")