# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

#문항별 정답 입력받음
answer = list(map(int, input().split()))
#문항별 배점 입력받음
point = list(map(int, input().split()))
#제출한 답안지 수 입력받음
n = input()
#점수를 저장할 딕셔너리 선언
temp = []
#제출한 답안지 수만큼 채점하는 for문을 선언
for i in range(int(n)):
	#답안지 입력받음
	space = list(map(int, input().split()))
	score = 0
	#답안지 채점 및 점수 계산
	for j in range(len(space)):
		if space[j] == answer[j]:
			score += point[j]
			temp.append(score)

print(min(temp), max(temp))