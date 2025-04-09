class QBrain:
    def __init__(self, q_list):
        self.q_num = 0
        self.q_list = q_list
        self.score = 0

    def still_que(self):
        if self.q_num < len(self.q_list):
            return True

    def next_que(self):
        self.q_num +=1
        current_que = self.q_list[self.q_num-1]
        user_input = input(f'Q.{self.q_num}:{current_que.text} (True/False): ')
        self.check_ans(user_input,current_que.answer)
        # self.q_num +=1

    def check_ans(self, user_ans, correct_answer):
        if user_ans.lower() == correct_answer.lower():
            print('CORRECT')
            self.score +=1
            
        else:
            print('WRONG')
            print(f'Correct answer is : {correct_answer}')
            print(f'Score: {self.score}/{self.q_num}')
            self.q_num = len(self.q_list)


