#class User:
#    def __init__(self, user_id, username):
#        self.id = user_id
#        self.username = username
#        self.followers = 0
#        self.following = 0
#        print("new user")
#    def follow(self, user):
#        user.followers += 1
#        self.following += 1
#
#
#
#user_1 = User("001", "angela")
#user_2 = User("002", "jack")
#user_1.follow(user_2)
#print(user_1.followers)
#print(user_1.following)
#print(user_2.followers)
#print(user_2.following)
from question_model import Question
from data import question_data
from quiz_brain import Quizbrain
question_bank = []
for question_for_bank in question_data:
     question_bank.append(Question(question_for_bank["question"], question_for_bank["correct_answer"]))


quiz = Quizbrain(question_bank)
while quiz.still_has_questions():
     quiz.next_question()
print("You've completed the queiz")
print(f"Your final score was: {quiz.score}/ {len(question_bank)}")


