# 4-2_2인용_끝말잇기.py

import random

def AI_공격_단어고르기(앞글자):
#일단 file 읽고 비교하면서 끝말잇기가 되는 앞글자를 지닌 단어를 찾는다
    가능한_단어집=[]
  #사전주머니 사전에서 일일이 읽으면서 하나 하나 찾아야되는데
    for 단어 in 사전주머니:
        if 단어[0]== 앞글자: 
            가능한_단어집.append(단어)
    랜덤index =random.randint(0, len(가능한_단어집)-1)  
    AI_선택_단어 =가능한_단어집[랜덤index]

    return AI_선택_단어


""" 기능 """
def 낱말끈_보여주기_화살표():
    지금까지낱말끈길이 = len(지금까지낱말끈)
    예쁜낱말끈 = []
    예쁜낱말끈 = 지금까지낱말끈[0]
    for 낱말번호 in range(1, 지금까지낱말끈길이):
        예쁜낱말끈 = 예쁜낱말끈 + "->" + 지금까지낱말끈[낱말번호]
    print(예쁜낱말끈)


def 새낱말_입력():
    print("새낱말을 입력하세요.")
    새낱말 = input()
    return 새낱말



""" 규칙 """
def 사전_확인하기():
    사전에있는가 = False
    for 사전번호 in range(0, 사전개수):
        if 사전주머니[사전번호] == 새낱말 + "\n":
            사전에있는가 = True
            break
    return 사전에있는가


def 중복_확인하기():
    # 나온낱말인가의 이름의 범위는 어디까지인가?
    # global 나온낱말인가  # 메인프로그램의 나온낱말인가를 사용하겠다.
    중복 = False
    for 낱말번호 in range(0, len(지금까지낱말끈)):
        if 새낱말 == 지금까지낱말끈[낱말번호]:
            중복 = True
            break
    return 중복


# 사전 불러오기
한글사전파일 = open("korean_noun.txt", 'r', encoding='utf-8')
사전주머니 = 한글사전파일.readlines()
사전개수 = len(사전주머니)
한글사전파일.close()


"""메인프로그램"""
지금까지낱말끈 = []

# 시작 낱말 받기
print("시작낱말을 입력하세요.")
시작낱말 = input()
지금까지낱말끈.append(시작낱말)
마지막낱말 = 시작낱말

for 반복 in range(0, 9999999):
    print("*******")  # 반복될때 마다 표시
    낱말끈_보여주기_화살표()

    ##########################################
    # 바뀐부분
    ##########################################
    if 반복 % 2 == 0:
        print("플레이어 1 차례입니다.")
        새낱말 = 새낱말_입력()
    else:
        print("플레이어 2 차례입니다.")
        새낱말 =AI_공격_단어고르기(마지막낱말[len(마지막낱말) - 1])   
    ##########################################

    # 끝말잇기기가 되는가? ********************************************
    새낱말_첫글자 = 새낱말[0]
    지금까지낱말끈길이 = len(지금까지낱말끈)
    마지막낱말 = 지금까지낱말끈[지금까지낱말끈길이 - 1]
    마지막낱말_마지막글자 = 마지막낱말[len(마지막낱말) - 1]

    이어지는가 = (새낱말_첫글자 == 마지막낱말_마지막글자)
    if 이어지는가 == False:
        print("땡!! 끝말잇기가 아닙니다.")
        break


    # 중복단어인가? ***************************************************
    나온낱말인가 = 중복_확인하기()  # 중복확인()의 return을 받는다
    if 나온낱말인가 == True:
        print("땡!!!! 이미 나온 단어입니다.")
        break



    #사전에 있는가? ***************************************************
    사전에있는가 = 사전_확인하기()
    if 사전에있는가 == False:
        print("'%s'는 없는 단어입니다" %새낱말)
        print("이를 낱말로 인정 하시겠습니까? (네/아니오)")
        is_gameover = False #다중반복문을 탈출하는 방법 여기서는 if, while
        while True:
            대답 = input()

            if 대답 == '아니오' or 대답 == '아니요':
                is_gameover = True
                break
            elif 대답 == '네':
                # 사전 불러오기
                한글사전파일 = open("korean_noun.txt", 'a', encoding='utf-8') #open (w,a,r) 차이점 생각.
                
                #이제 여기서 단어를 추가한다. append와는 달리 file에 추가는 다름 방법이다
                한글사전파일.write(새낱말+ '\n' )
                한글사전파일.close()
                break
            else:
                print("다시 대답해주세요")
        if is_gameover == True:
            break

    마지막낱말 = 새낱말
    지금까지낱말끈.append(새낱말)
