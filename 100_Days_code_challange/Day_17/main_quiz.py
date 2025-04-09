from quiz_brain import QBrain
from Question_model import Question
from data import question_data

question_bank = []

for dict_ in question_data:
    question = dict_['text']
    answer = dict_['answer']
    q_obj = Question(question, answer)
    question_bank.append(q_obj)


quiz = QBrain (question_bank) 

while(quiz.still_que()):
    quiz.next_que()
