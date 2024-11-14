# utils/input_handler.py

def get_user_choice():
    """
    사용자로부터 입력을 받고, '가위', '바위', '보' 중 하나를 선택할 때까지 반복합니다.
    """
    valid_choices = ["가위", "바위", "보"]
    while True:
        user_input = input("가위, 바위, 보 중 하나를 선택하세요: ").strip()
        if user_input in valid_choices:
            return user_input
        else:
            print("잘못된 입력입니다. '가위', '바위', '보' 중 하나를 입력해주세요.")
