# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 문제별 정답을 입력받음
a1 = list(map(int, input().split()))
# 문제별 배점을 입력받음
a2 = list(map(int, input().split()))
# 제출한 답안지를 입력받음
a3 = list(map(int, input().split()))

score = 0
# 문제의 개수만큼 반복
for i in range(len(a1)):
    # 제출한 답안지의 답과 문제별 정답이 같은지 판별
    if a1[i] == a3[i]:
        # 조건을 만족한다면 score에 문제에 해당하는 점수를 더해줌
        score += a2[i]

print(score)

