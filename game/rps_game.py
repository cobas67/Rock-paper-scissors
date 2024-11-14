# game/rps_game.py

import random
from utils.input_handler import get_valid_input

class RPSGame:
    def __init__(self):
        self.choices = ["가위", "바위", "보"]

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "무승부"
        elif (user_choice == "가위" and computer_choice == "보") or \
             (user_choice == "바위" and computer_choice == "가위") or \
             (user_choice == "보" and computer_choice == "바위"):
            return "승리"
        else:
            return "패배"

    def play_round(self):
        user_choice = get_valid_input("가위, 바위, 보 중 하나를 선택하세요: ", self.choices)
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(user_choice, computer_choice)
        
        print(f"사용자: {user_choice}, 컴퓨터: {computer_choice} → 결과: {result}")
        return result
