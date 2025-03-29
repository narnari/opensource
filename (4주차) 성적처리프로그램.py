###################################
# 전공 : 소프트웨어학부
# 학번 : 2024042003
# 이름 : 이나연
# 프로그램 : 성적관리 프로그램
###################################

import os

# 학생 정보를 저장할 리스트 전역 변수로 생성
students = []

# 입력 합수
def insert():
    # 전역 리스트 사용
    global students
    # 5명의 학생 정보를 입력
    for i in range(5):
        student = {}  # 학생 개별 정보 저장을 위한 딕셔너리
        print("="*80)
        print(f"{i+1}번 째 학생 성적 입력.")
        
        # 학번, 이름, 점수 입력받기
        student['id'] = int(input("학번: "))
        student['name'] = input("이름: ")
        student['english'] = int(input("영어: "))
        student['c_language'] = int(input("C-언어: "))
        student['python'] = int(input("파이썬: "))
        
        # 총점과 평균 계산
        average(student)
        
        # 학점 계산
        grade(student)
        
        # 학생 정보를 리스트에 추가
        students.append(student)

        # 총점 정렬
        total_sort(students)

    return students

# 총점/평균 계산 함수
def average(student):
    # 총점 계산
    student['total'] = student['english'] + student['c_language'] + student['python']
    # 평균 계산
    student['average'] = student['total'] / 3

# 학점 계산 함수
def grade(student):
    # 총점에 따른 학점 계산
    if student['total'] >= 270:
        student['grade'] = 'A+'
    elif student['total'] >= 255:
        student['grade'] = 'A'
    elif student['total'] >= 240:
        student['grade'] = 'B+'
    elif student['total'] >= 225:
        student['grade'] = 'B'
    elif student['total'] >= 210:
        student['grade'] = 'C+'
    elif student['total'] >= 195:
        student['grade'] = 'C'
    else:
        student['grade'] = 'F'

# 성적 삭제 함수
def delete():
    student_id=int(input("성적을 삭제할 학생의 학번을 입력하세요 : "))
    for student in students:
        if student['id']==student_id:
            student_name = student['name']
            students.remove(student)
            print(f"{student_id} {student_name} 성적 삭제")
            return
    print(f"{student_id} {student_name} 성적이 존재하지 않습니다.")

# 학생 성적 찾기
def search():
    student_id=int(input("성적을 찾을 학생의 학번을 입력하세요 : "))
    for student in students:
        if student['id']==student_id:
            student_name = student['name']
            print(f"{student_id} {student_name}의 학점 : {student['grade']}")
            return
    print(f"{student_id} 성적이 존재하지 않습니다.")

def total_sort(student):
    # 총점을 기준으로 내림차순 정렬하여 등수 계산
    students.sort(key=lambda x: x['total'], reverse=True)
    for student in students:
        print(student['id'], student['name'], student['total'])

# 80점 이상 학생 수 카운트 함수
def check_80(student):
    count = 0
    for student in students:
        if student['average']>=80:
            count+=1
    print(f"\n80점 이상인 학생 수는 {count} 명 입니다.\n")

def prints(students):
    for i, student in enumerate(students, start=1):
        student['rank'] = i
    # 출력 형식
    print("\n                              성적관리 프로그램 ")
    print("=" * 80)
    print(" 학번      이름      영어  C-언어  파이썬  총점  평균  학점  등수 ")
    print("=" * 80)
    
    # 학생별 성적 출력
    for student in students:
        print(f" {student['id']:<8}  {student['name']:<5}  {student['english']:>5}  {student['c_language']:>5}  {student['python']:>5}  {student['total']:>5}  {student['average']:>5.1f}  {student['grade']:>2}  {student['rank']:>2}")
    
    print("=" * 80)

# 프로그램 실행
while True:
    print("                            메뉴 ")
    print("="*60)
    print("1. 성적 입력")
    print("2. 성적 삭제")
    print("3. 성적 찾기")
    print("4. 총점 정렬")
    print("5. 80점 이상")
    print("6. 성적 출력")
    print("="*60)
    print("0 을 입력하면 프로그램이 종료됩니다.\n")

    # 메뉴 선택
    menu=int(input("메뉴를 선택하세요 : "))
    # 프로그램 종료
    if(menu==0):
        break
    # 성적 입력
    if(menu==1):
        students = insert()
    # 성적 삭제
    elif(menu==2):
        if(len(students)==0):
            print("\n성적 정보가 존재하지 않습니다. 메뉴를 다시 선택해 주세요.\n")
        else:
            delete()
    # 성적 찾기
    elif(menu==3):
        if(len(students)==0):
            print("\n성적 정보가 존재하지 않습니다. 메뉴를 다시 선택해 주세요.\n")
        else:
            search()
    # 총점 정렬
    elif(menu==4):
        if(len(students)==0):
            print("\n성적 정보가 존재하지 않습니다. 메뉴를 다시 선택해 주세요.\n")
        else:
            total_sort(students)
    # 80점 이상 계산
    elif(menu==5):
        if(len(students)==0):
            print("\n성적 정보가 존재하지 않습니다. 메뉴를 다시 선택해 주세요.\n")
        else:
            check_80(students)
    # 성적 출력
    elif(menu==6):
        if(len(students)==0):
            print("\n성적 정보가 존재하지 않습니다. 메뉴를 다시 선택해 주세요.\n")
        else:
            prints(students)

os.system("pause")