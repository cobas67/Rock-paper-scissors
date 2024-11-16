# game/rps_game.py


import random
from utils.input_handler import get_user_choice


class RPSGame:
    def __init__(self, user_choice):
        self.user_choice = user_choice
        self.choices = ["가위", "바위", "보"]


    def get_computer_choice(self):
        # 컴퓨터의 선택을 무작위로 반환
        return random.choice(self.choices)


    def determine_winner(self):
        # 컴퓨터의 선택을 가져옵니다.
        computer_choice = self.get_computer_choice()


        # 사용자와 컴퓨터의 선택을 비교하여 결과를 반환
        if self.user_choice == computer_choice:
            return "무승부", self.user_choice, computer_choice
        elif (self.user_choice == "가위" and computer_choice == "보") or \
             (self.user_choice == "바위" and computer_choice == "가위") or \
             (self.user_choice == "보" and computer_choice == "바위"):
            return "승리", self.user_choice, computer_choice
        else:
            return "패배", self.user_choice, computer_choice


    def play_round(self):
        # determine_winner를 호출하여 결과와 선택을 반환
        result, user_choice, computer_choice = self.determine_winner()
        
        print(f"사용자: {user_choice}, 컴퓨터: {computer_choice} → 결과: {result}")
        return result, user_choice, computer_choice