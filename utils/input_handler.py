# utils/input_handler.py

def get_user_choice(prompt="가위, 바위, 보 중 하나를 선택하세요: ", choices=["가위", "바위", "보",]):
    while True:
        user_input = input(prompt)
        if user_input in choices:
            return user_input
        if user_input == "종료":
            return None
        print("잘못된 입력입니다. 다시 시도해주세요.")

