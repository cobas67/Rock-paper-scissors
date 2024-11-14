# -*- coding: utf-8 -*-
# main.py

from game.rps_game import RPSGame
from game.score_tracker import ScoreTracker
from utils.input_handler import get_user_choice

def main():
    print("가위바위보 게임에 오신 것을 환영합니다!")
    print("종료하려면 '종료'라고 입력하세요.")

    # ScoreTracker 인스턴스를 생성하여 점수를 기록합니다.
    score_tracker = ScoreTracker()
    while True:
        user_choice = get_user_choice()

        if user_choice is None:
            print("게임을 종료합니다.")
            break

        # RPSGame 객체를 생성하고 play_round 메서드를 호출하여 결과를 얻습니다.
        game = RPSGame(user_choice)
        result, user_choice, computer_choice = game.play_round()

        # 결과에 따라 score_tracker의 update_score 메서드에 사용자와 컴퓨터의 선택을 전달합니다.
        score_tracker.update_score(user_choice, computer_choice)

    
           

        # 현재까지의 점수를 출력합니다.
        score_tracker.display_scores()

    # 최종 결과를 출력합니다.
    print("\n최종 결과")
    score_tracker.display_final_result()

if __name__ == "__main__":
    main()