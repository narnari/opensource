##############################################################
# 프로그램명: 성적처리프로그램 (데이터베이스)
# 작성자: 소프트웨어학부 / 이나연
# 작성일: 6ㅇㅇ월 13일
# 프로그램 설명: n명의 학생에 대해 영어, C-언어, 파이썬 점수를 입력받아
#              총점, 평균, 학점, 등수를 계산하고 관리하는 프로그램
##############################################################

import mysql.connector

# MySQL에 연결
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='sql1234',  # ← 네가 설치할 때 설정한 root 비번
    database='mydb'         # 우리가 만든 DB 이름
)

cursor = conn.cursor()

# 학점 계산 함수 (평균 점수 기준)
def calculate_grade(avg):
    if avg >= 90: return 'A'
    elif avg >= 80: return 'B'
    elif avg >= 70: return 'C'
    elif avg >= 60: return 'D'
    else: return 'F'


# 등수 계산 함수
def update_ranks():
    cursor.execute("SELECT student_id, total FROM GradeManager ORDER BY total DESC")
    results = cursor.fetchall()
    for i, (sid, _) in enumerate(results, start=1):
        cursor.execute("UPDATE GradeManager SET `rank` = %s WHERE student_id = %s", (i, sid))
    conn.commit()

# 학생 입력 함수
def insert_student():
    sid = input("학번: ")
    name = input("이름: ")
    eng = int(input("영어 점수: "))
    c = int(input("C언어 점수: "))
    py = int(input("파이썬 점수: "))

    total = eng + c + py
    avg = total / 3
    grade = calculate_grade(avg)

    cursor.execute("""
        INSERT INTO GradeManager (student_id, name, english, c_lang, python, total, average, grade)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (sid, name, eng, c, py, total, avg, grade))
    conn.commit()
    update_ranks()
    print(" 학생 정보 입력 완료!")

# 전체 출력 함수
def show_all():
    cursor.execute("SELECT * FROM GradeManager ORDER BY `rank`")
    for row in cursor.fetchall():
        print(row)

# 삭제 함수
def delete_student():
    sid = input("삭제할 학생의 학번: ")
    cursor.execute("DELETE FROM GradeManager WHERE student_id = %s", (sid,))
    conn.commit()
    update_ranks()
    print(" 삭제 완료!")

# 탐색 함수
def search_student():
    keyword = input("찾을 이름 또는 학번: ")
    cursor.execute("""
        SELECT * FROM GradeManager 
        WHERE student_id = %s OR name = %s
    """, (keyword, keyword))
    for row in cursor.fetchall():
        print(row)

# 정렬 함수 (총점 기준 내림차순)
def sort_by_total():
    cursor.execute("SELECT * FROM GradeManager ORDER BY total DESC")
    for row in cursor.fetchall():
        print(row)

# 80점 이상 학생 수 세기
def count_high_scores():
    cursor.execute("SELECT COUNT(*) FROM GradeManager WHERE average >= 80")
    result = cursor.fetchone()
    print(f" 80점 이상 학생 수: {result[0]}명")

# 메뉴
def menu():
    while True:
        print("\n [성적 관리 시스템]")
        print("1. 학생 입력")
        print("2. 전체 출력")
        print("3. 학생 삭제")
        print("4. 학생 검색")
        print("5. 총점 정렬")
        print("6. 80점 이상 학생 수")
        print("0. 종료\n")
        choice = input("선택 > ")

        if choice == '1': insert_student()
        elif choice == '2': show_all()
        elif choice == '3': delete_student()
        elif choice == '4': search_student()
        elif choice == '5': sort_by_total()
        elif choice == '6': count_high_scores()
        elif choice == '0': break
        else: print("error! 다시 선택해 주세요.")

    cursor.close()
    conn.close()

# 실행
menu()