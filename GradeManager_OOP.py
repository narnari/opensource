##################
# 프로그램명: 성적처리프로그램 (객체지향 프로그램)
# 작성자: 소프트웨어학부 / 이나연
# 작성일: 4월 13일
# 프로그램 설명: 5명의 학생에 대해 영어, C-언어, 파이썬 점수를 입력받아
#              총점, 평균, 학점, 등수를 계산하고 관리하는 프로그램
##################

import os

# -------------------------------------------------------------
# 학생 한 명의 정보를 나타내는 클래스
# - 점수 입력 시 총점, 평균, 학점 자동 계산
# - 각 학생은 객체로 생성되어 리스트에 저장됨
# -------------------------------------------------------------
class Student:
    def __init__(self, student_id, name, english, c_language, python_score):
        # 학생 기본 정보
        self.student_id = student_id
        self.name = name
        self.english = english
        self.c_language = c_language
        self.python = python_score

        # 계산될 속성들
        self.total = 0
        self.average = 0.0
        self.grade = ''
        self.rank = 0

        # 총점, 평균, 학점 계산 메서드 호출
        self.calculate_scores()

    # 총점과 평균 계산
    def calculate_scores(self):
        self.total = self.english + self.c_language + self.python
        self.average = self.total / 3
        self.calculate_grade()

    # 학점 계산 로직
    def calculate_grade(self):
        if self.total >= 285:
            self.grade = 'A+'
        elif self.total >= 270:
            self.grade = 'A'
        elif self.total >= 255:
            self.grade = 'B+'
        elif self.total >= 240:
            self.grade = 'B'
        elif self.total >= 225:
            self.grade = 'C+'
        elif self.total >= 210:
            self.grade = 'C'
        elif self.total >= 195:
            self.grade = 'D+'
        elif self.total >= 180:
            self.grade = 'D'
        else:
            self.grade = 'F'

# -------------------------------------------------------------
# 학생 목록을 관리하는 클래스
# - 학생 입력, 삭제, 검색, 정렬, 출력, 분석 등 기능 포함
# -------------------------------------------------------------
class StudentManager:
    def __init__(self):
        self.students = []  # 학생 객체 리스트

    # 학생 정보 입력 (5명 입력받음)
    def insert(self):
        for i in range(5):
            print("=" * 80)
            print(f"{i + 1}번째 학생 입력")

            # 사용자 입력
            student_id = int(input("학번: "))
            name = input("이름: ")
            english = int(input("영어: "))
            c_language = int(input("C-언어: "))
            python_score = int(input("파이썬: "))

            # 학생 객체 생성 후 리스트에 추가
            student = Student(student_id, name, english, c_language, python_score)
            self.students.append(student)

        # 입력 후 총점 기준 정렬 및 등수 부여
        self.sort_by_total()

    # 학생 삭제 (학번 기준)
    def delete(self):
        student_id = int(input("삭제할 학번: "))
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"{student_id} {student.name} 성적 삭제 완료")
                return
        print(f"{student_id} 해당 학번은 존재하지 않습니다.")

    # 학생 검색 (학번 기준)
    def search(self):
        student_id = int(input("찾을 학번: "))
        for student in self.students:
            if student.student_id == student_id:
                print(f"{student_id} {student.name}의 학점: {student.grade}")
                return
        print(f"{student_id} 해당 학생이 존재하지 않습니다.")

    # 총점 기준 정렬 + 등수 부여
    def sort_by_total(self):
        self.students.sort(key=lambda x: x.total, reverse=True)
        for i, student in enumerate(self.students, start=1):
            student.rank = i

    # 정렬된 총점 출력
    def print_sorted(self):
        for student in self.students:
            print(student.rank, student.student_id, student.name, student.total)

    # 평균 80점 이상 학생 수 카운트
    def count_high(self):
        count = sum(1 for student in self.students if student.average >= 80)
        print(f"\n평균이 80점 이상인 학생 수: {count}명\n")

    # 전체 성적 출력
    def print_all(self):
        self.sort_by_total()  # 출력 전 정렬 및 등수 최신화
        print("\n                              성적관리 프로그램 ")
        print("=" * 80)
        print(" 학번      이름      영어  C-언어  파이썬  총점  평균  학점  등수 ")
        print("=" * 80)
        for student in self.students:
            print(f" {student.student_id:<8}  {student.name:<5}  {student.english:>5}  {student.c_language:>5}  {student.python:>5}  {student.total:>5}  {student.average:>5.1f}  {student.grade:>2}  {student.rank:>2}")
        print("=" * 80)


# -------------------------------------------------------------
# 프로그램 실행 흐름을 관리하는 메인 함수
# - 사용자 메뉴 입력에 따라 StudentManager 기능 호출
# -------------------------------------------------------------
def main():
    manager = StudentManager()

    while True:
        print("\n                            메뉴 ")
        print("=" * 60)
        print("1. 성적 입력")
        print("2. 성적 삭제")
        print("3. 성적 찾기")
        print("4. 총점 정렬")
        print("5. 80점 이상 학생 수")
        print("6. 전체 성적 출력")
        print("0. 프로그램 종료")
        print("=" * 60)

        choice = input("메뉴를 선택하세요: ")

        if choice == '0':
            break
        elif choice == '1':
            manager.insert()
        elif choice in ['2', '3', '4', '5', '6']:
            if not manager.students:
                print("\n성적 정보가 존재하지 않습니다. 메뉴를 다시 선택해 주세요.\n")
            else:
                if choice == '2':
                    manager.delete()
                elif choice == '3':
                    manager.search()
                elif choice == '4':
                    manager.sort_by_total()
                    manager.print_sorted()
                elif choice == '5':
                    manager.count_high()
                elif choice == '6':
                    manager.print_all()
        else:
            print("올바른 번호를 선택해 주세요.")

    os.system("pause")

# 프로그램 시작점
if __name__ == "__main__":
    main()
