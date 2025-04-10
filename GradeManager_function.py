# 성적관리 프로그램(함수)
# 5명의 학생의 세개의 교과목 (영어, C-언어, 파이썬)에 대하여 
# 키보드로부터 학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 입력받아 총점, 평균, 학점, 등수를 계산하는 프로그램 작성
import os

def insert():
    # 학생 정보를 저장할 리스트 생성
    students = []
    
    # 5명의 학생 정보를 입력
    for i in range(5):
        student = {}  # 학생 개별 정보 저장을 위한 딕셔너리
        print("="*80)
        print(f"성적 관리를 위한 {i+1}번 째 학생 성적 입력.")
        
        # 학번, 이름, 점수 입력받기
        student['id'] = input("학번: ")
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
    
    return students

def average(student):
    # 총점 계산
    student['total'] = student['english'] + student['c_language'] + student['python']
    # 평균 계산
    student['average'] = student['total'] / 3

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

def prints(students):
    # 총점을 기준으로 내림차순 정렬하여 등수 계산
    students.sort(key=lambda x: x['total'], reverse=True)
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
students = insert()
prints(students)
os.system("pause")