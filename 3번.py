# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 회문여부를 판별하는 함수
def IsPalindrome(string):
    for i in range(len(string)//2):
            if string[i] != string[-1-i]:
                return False
    return True

 # 문자열을 입력받는다. 이때 대소문자 구별을 하지 않기 위해 다 소문자로 변환
string = list(input().lower())
DSub = []

#이중 for문을 사용하여 슬라이싱을 통해 모든 경우의 부문자열을 구한다.
for i in range(len(string)):
    for j in range(1, len(string)+1):
        if i<j:
        #그 부문자열이 회문인지 판별, 회문이라면 리스트에 추가
            if IsPalindrome(string[i:j]) == True:
                S = "".join(string[i:j])
                DSub.append(S)

# 리스트를 집합으로 바꾸어 중복을 제거한 후, 다시 리스트로 변환
DSub = list(set(DSub))
# 리스트를 사전식으로 재배열
DSub.sort(reverse=False)
# 이후 리스트를 출력
for v in DSub:
    print(v," ", end='')


