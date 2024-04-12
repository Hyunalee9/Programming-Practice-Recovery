# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.
import sys
length = int(input())
result = [int(j) for j in input().split()]
search = int(input())
cnt = 0

for i in result:
    if i == search:
        cnt += 1
print(cnt)


