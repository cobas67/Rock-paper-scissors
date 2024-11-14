# game/score_tracker.py
class ScoreTracker:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0

    def update_score(self, user_choice, computer_choice):
        
        #승자를 결정하고 점수 업데이트
    
        if user_choice == computer_choice:
            print("무승부!")
            return "무승부"
        elif (user_choice == "가위" and computer_choice == "보") or \
             (user_choice == "바위" and computer_choice == "가위") or \
             (user_choice == "보" and computer_choice == "바위"):
            print("사용자 승리!")
            self.user_score += 1
            return "사용자"
        else:
            print("컴퓨터 승리!")
            self.computer_score += 1
            return "컴퓨터"

    def display_scores(self):
        
        #현재 점수 출력
        
        print(f"현재 점수 -> 사용자: {self.user_score}, 컴퓨터: {self.computer_score}")

    def is_game_over(self, max_wins):
        #게임 종료 조건 확인
        
        return self.user_score >= max_wins or self.computer_score >= max_wins

    def display_final_result(self):
        
        #최종 결과 출력

        if self.user_score > self.computer_score:
            print("축하합니다! 사용자가 최종 승리했습니다.")
        elif self.user_score < self.computer_score:
            print("컴퓨터가 최종 승리했습니다. 다음 기회에!")
        else:
            print("최종적으로 무승부입니다.")
