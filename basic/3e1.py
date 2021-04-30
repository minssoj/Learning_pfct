# [그리디] 거스름돈
#========== input ===========
# n : 거스름돈 금액
#========== output ==========
# result : 금액에 해당되는 최소의 동전 개수
# 풀이 : 가장 큰 동전부터, 거스를 수 있을 만큼 거슬러 주기

n = int(input())
result = 0

coin_list = [500, 100, 50, 10]

for coin in coin_list:
    result += n//coin
    n %= coin

print(result)
