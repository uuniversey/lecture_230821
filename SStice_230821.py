

# 주사위 쌓기

# import sys
# sys.stdin = open('test.txt', 'r')
#
# N = int(input())
# dice = [list(map(int, input().split())) for _ in range(N)]
# idx = [5, 3, 4, 1, 2, 0]
# result_list = []
# num = 1
#
# for bottom in range(6):
#     result = 0
#     basic = [1, 2, 3, 4, 5, 6]
#     max_v = 0
#     basic.remove(dice[0][bottom])
#     top = dice[0][idx[bottom]]
#     basic.remove(top)
#     for i in basic:
#         if max_v < i:
#             max_v = i
#
#     result += max_v
#
#     while num != N:
#         max_v = 0
#         basic = [1, 2, 3, 4, 5, 6]
#         for j in range(6):
#             if dice[num][j] == dice[num][top]:
#                 top = dice[num][idx[j]]
#                 basic.remove(top)
#                 basic.remove(idx[j])
#         for i in basic:
#             if max_v < i:
#                 max_v = i
#
#         result += max_v
#
#         num += 1
#
#     result_list.append(result)
#
# max_result = 0
# for i in result_list:
#     if max_result < i:
#         max_result = i
#
# print(max_result)


# 참고자료


# def preorder(node):
#     global V
#     if 0 < node <= V:
#         print(node, end=" ")
#         if node != V:
#             preorder(c1[node])
#             preorder(c2[node])
#
#
# V = int(input())
# input_list = list(map(int, input().split()))
#
# c1 = [0] * V
# c2 = [0] * V
#
# for i in range(0, len(input_list), 2):
#     p, c = input_list[i], input_list[i + 1]
#     if not c1[p]:
#         c1[p] = c
#     else:
#         c2[p] = c
#
# preorder(1)


# tree 연습 - 부모를 인덱스로 자식을 저장

def preorder(n):
    if n:      # 존재하는 정점이면
        print(n, end=' ')    # visit(n)
        preorder(ch1[n])    # 왼쪽 서브트리로 이동
        preorder(ch2[n])    # 오른쪽 서브트리로 이동


V = int(input())
E = V - 1
arr = list(map(int, input().split()))
ch1 = [0] * (V+1)
ch2 = [0] * (V+1)
par = [0] * (V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2 + 1]
    if ch1[p] == 0:     # 자식1이 아직 없다면
        ch1[p] = c
    else:
        ch2[p] = c



    par[c] = p      # 자식을 인덱스로 부모 저장
# 실제 루트 찾기
root = 1
while par[root] != 0:
    root += 1



preorder(1)