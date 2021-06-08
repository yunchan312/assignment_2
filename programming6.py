# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
class DoubleHashing:
    def __init__(self, size):
        self.M = size
        self.a = [None]*size #key값을 저장하는 함수
        self.d = [None]*size #data를 저장하는 함수
        self.N = 0

    def hash(self, key): #초기 해시값을 구하는 함수
        return key % self.M

    def put(self, key, data): #해시테이블에 추가하는 함수
        initialPos = self.hash(key) #초기 해시값을 설정
        i = initialPos
        d = 7 - (key % 7) #이중해싱을 위한 두번째 해시
        j = 0
        while True:
            if self.a[i] == None: #key값에 해당하는 자료가 없다면
                self.a[i] = key #key값을 저장
                self.d[i] = data #value값을 저장
                self.N += 1 #자료의 개수에 +1 해줌
                return
            if self.a[i] == key: #key값이 있다면
                print('error1') #오류를 출력
                return

    def get(self, key): #key값에 해당하는 data를 출력하는 함수
        initialPos = self.hash(key) #초기 해시값 설정
        i = initialPos
        d = 7 - (key % 7) #점프를 위한 두번째 해싱
        j = 0
        while self.a[i] is not None: #key값이 None이 아닌 동안만 검사
            if self.a[i] == key: #key값이 key리스트에 존재한다면
                print(self.d[i]) #key값에 해당하는 data 출력
                return
            j += 1
            i = (initialPos + j*d) % self.M #두번째 해시값을 이용해서 점프를 해서 해시테이블 내에서 다음으로 넘어감
            if i == initialPos: #처음과 같은 값이 나온다면
                print('error2') #에러를 출력함
                return

    def fix(self, key, data): #수정하는 함수
        initialPos = self.hash(key) #초기 해시값 설정
        i = initialPos
        while True:
            if self.a[i] == None: #key값이 저장되어 있지 않다면
                print('error2') #에러를 출력
                return
            if self.a[i] == key: #key값이 저장되어 있다면
                self.d[i] = data #data를 출력
                return

def ListToAscii(list): #영어단어 각 알파벳에 해당하는 ASCII코드를 더하여 key값을 설정하는 함수
    sum = 0
    for x in list:
        sum += ord(x) #ASCII코드로 변환하여 더하는 반복문
    return sum #더한 값을 출력


t = DoubleHashing(16777)
while True:
    D = list(input().split()) #명령어를 입력받음
    if D[0] == '단어삽입': #명령어가 '단어삽입'인 경우
        key = ListToAscii(D[1]) #key값을 생성함
        t.put(key, D[2]) #put함수를 통해 단어를 삽입한다.
    elif D[0] == '단어뜻수정': #명령어가 '단어뜻수정'인 경우
        key = ListToAscii(D[1]) #key값을 생성함
        t.fix(key, D[2]) #fix함수를 통해 단어를 수정한다.ㅏ
    elif D[0] == '단어검색': #명령어가 '단어검색'인 경우
        key = ListToAscii(D[1]) #key값을 설정
        t.get(key) #get함수를 통해 단어를 가지고온다.
    elif D[0] == '종료': #명령어가 종료인 경우
        break #반목문을 멈춘다.
