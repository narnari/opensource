###################################
# 전공 : 소프트웨어학부
# 학번 : 2024042003
# 이름 : 이나연
# 프로그램 : 틱택토
###################################

import os
import time
import random

print("틱택토 게임 시작!!")

# 틱택토 보드 크기
BOARD_SIZE = 3

# 틱택토 보드 초기화
board = [[0 for i in range(BOARD_SIZE)] for i in range(BOARD_SIZE)]
print("좌표를 입력하세요 (EX 3 2)")

# 승리 조건 확인 함수
def check_victory(x, y, player):
    global board
    global BOARD_SIZE
    win_conditions = []  # 승리 조건을 저장할 리스트
    count = 0  # 연속된 같은 플레이어의 수를 셀 변수

    # 대각선 (오른쪽 위 → 왼쪽 아래)
    for i in range(BOARD_SIZE):
        if board[i][BOARD_SIZE - i - 1] == player:
            count += 1
        else:
            break
    win_conditions.append(count)

    # 대각선 (왼쪽 위 → 오른쪽 아래)
    count = 0
    for i in range(BOARD_SIZE):
        if board[i][i] == player:
            count += 1
        else:
            break
    win_conditions.append(count)

    # 가로줄 확인
    for i in range(BOARD_SIZE):
        count = 0
        for j in range(BOARD_SIZE):
            if board[i][j] == player:
                count += 1
            else:
                break
        win_conditions.append(count)

    # 세로줄 확인
    for i in range(BOARD_SIZE):
        count = 0
        for j in range(BOARD_SIZE):
            if board[j][i] == player:
                count += 1
            else:
                break
        win_conditions.append(count)

    time.sleep(1)
    # 승리 조건 중 하나라도 보드 크기와 같으면 승리
    if BOARD_SIZE in win_conditions:
        return True
    else:
        return False

# 빈 칸 찾기 함수
def find_empty_cells():
    global board
    empty_cells = []
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == 0:
                empty_cells.append([i, j])
    return empty_cells

# 보드 출력 함수
def draw_board():
    for i in range(BOARD_SIZE):
        print("===" * BOARD_SIZE)
        for j in range(BOARD_SIZE):
            if board[i][j] == 0:
                print("ㅒ ", end="")
            elif board[i][j] == 1:
                print("ㅒO", end="")
            else:
                print("ㅒX", end="")
        print("ㅒ")
    print("===" * BOARD_SIZE)

# 게임 라운드
current_round = 0

# 메인 함수
def main():
    global BOARD_SIZE
    global current_round
    global board

    # 플레이어 순서 결정 (1: O, 2: X)
    player_turn = random.randrange(1, 3)

    while True:
        current_round += 1
        draw_board()

        while True:
            if current_round % 2 == player_turn - 1:
                print(("O " if current_round % 2 == 1 else "X ") + "입력하세요(종료: -1 -1)")
            else:
                print("컴퓨터 입력")

            try:
                x = 0
                y = 0

                if current_round % 2 == player_turn - 1:
                    # 플레이어 입력
                    x, y = map(int, input().split())
                else:
                    # 컴퓨터 입력
                    empty_cells = find_empty_cells()
                    selected_cell = empty_cells[random.randrange(0, len(empty_cells))]
                    x = selected_cell[1]
                    y = selected_cell[0]
                    print(x, y)

                # 입력된 좌표에 플레이어 마크 설정
                board[y - 1][x - 1] = 1 if current_round % 2 == 1 else 2

                # 승리 조건 확인
                if check_victory(x, y, 1 if current_round % 2 == 1 else 2):
                    os.system("cls")
                    draw_board()
                    print(("O " if current_round % 2 == 1 else "X ") + "승리")
                    return

                # 종료 조건
                if x == -1 and y == -1:
                    return

                # 이미 채워진 칸이면 다시 입력
                if board[y - 1][x - 1] != 1 and board[y - 1][x - 1] != 2:
                    continue

                break
            except:
                continue

        os.system("cls")

main()
os.system("pause")