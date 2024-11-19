# Rock-paper-scissors
<br>

## rps_game 기능 설명
1. 사용자 입력 및 컴퓨터 선택

- 사용자로부터 "가위", "바위", "보" 중 하나를 선택하도록 요청합니다.
- 컴퓨터는 무작위로 가위바위보 중 하나를 선택합니다.

2. 승패 판별
- determine_winner 메서드: 사용자와 컴퓨터의 선택을 비교하여 승리, 패배, 무승부 중 하나의 결과를 반환합니다.

3. 게임 진행
- play_round 메서드: 한 라운드의 게임을 진행하고, 결과를 출력한 후 반환합니다.

<br>

## 프로젝트 구조
<br>
├── game<br>
│   ├── init.py<br>            
│   ├── rps_game.py<br>           
│   ├── score_tracker.py<br>       
│<br>
├── utils/ <br>
│   ├── init.py<br>           
│   ├── input_handler.py<br>       
│<br>
├── LICENSE<br>                    
├── main.py<br>                    
├── README.md<br>                  

<br>

## 설치 방법
<br>
1. 레포지토리 클론<br><br>

```
git clone https://github.com/cobas67/Rock-paper-scissors.git
cd Rock-paper-scissors
```
2. 게임 실행 <br>

```
python main.py
```
<br>

## 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다. 자세한 내용은 LICENSE 파일을 참고하세요