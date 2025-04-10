#5명의 학생의 세개의 교과목 (영어, C-언어, 파이썬)에 대하여  키보드로부터 입력받아 총점, 평균, 학점, 등수를 계산하는 프로그램 작성
#평균 : 전체 평균
#학점 : 개인 평균
import os
arr=[]
sum = 0
for i in range(5):
    name = input("학생 이름 :")
    English = float(input("영어 성적 입력 : "))
    C = float(input("C-언어 성적 입력 : "))
    Python = float(input("파이썬 성적 입력 : "))
    arr.append([name, English, C, Python, English+C+Python, (English+C+Python)/3])
    sum += arr[i][5]
arr.sort(key = lambda x : x[5], reverse = True)
print("=================================")
print("전체 평균 : ", f"{sum/5:.2f}")
for i in range(5):
    if(arr[i][5]>=4.0):
        arr[i].append("A")
    elif(arr[i][5]>=3.0):
        arr[i].append("B")
    elif(arr[i][5]>=2.0):
        arr[i].append("C")
    elif(arr[i][5]>=1.0):
        arr[i].append("D")
    else : arr[i].append("F")
print("등수 이름   총점 평균 학점")
for i in range(5):
    print(f"{i+1}등.",arr[i][0], arr[i][4], f"{arr[i][5]:.2f}", arr[i][6])
os.system("pause")