

# 주사위 쌓기

# import sys
# sys.stdin = open('test.txt', 'r')
#
# N = int(input())
# dice = [list(map(int, input().split())) for _ in range(N)]
# idx = [5, 3, 4, 1, 2, 0]        # 주사위는 전개도에 따라 반대편이 정해져있으므로 그걸 주어진 전개도에 맞게 설정
# result_list = []                # 최대값을 찾기 위해 후보 선정
# num = 1                         # 첫번째 주사위의 다음 주사위 인덱스 초기값
#
# for bottom in range(6):         # 첫번째 주사위 bottom을 6개 다 설정해 줘서 그 중 어떤게 최대값인지 확인하겠다.
#     num = 1
#     sum_v = 0                      # 6번의 상황마다 각각의 옆면의 합, 매번 초기화
#     basic = [1, 2, 3, 4, 5, 6]      # 주사위 눈
#     max_v = 0
#     basic.remove(dice[0][bottom])   # bottom에 들어간 숫자 옆면 후보에서 제거
#     top = dice[0][idx[bottom]]      # top에 들어간 숫자는 bottom에 따라 정해지므로 이렇게 설정
#     basic.remove(top)               # top에 들어간 숫자 옆면 후보에서 제거
#     for i in basic:                 # top, bottom 고정한 상태로 옆면 돌려가면서 최대 숫자를 찾음
#         if max_v < i:
#             max_v = i
#
#     sum_v += max_v                       # 옆면의 합에 더해준다.
#
#     while num != N:                      # 마지막 주사위가 될 때까지 돈다.
#         max_v = 0                        # 초기화
#         basic = [1, 2, 3, 4, 5, 6]       # 초기화
#         for j in range(6):               # 이전의 주사위를 기준으로 이번 주사위의 bottom, top을 정함
#             if dice[num][j] == top:
#                 bottom = dice[num][j]
#                 top = dice[num][idx[j]]
#                 basic.remove(bottom)
#                 basic.remove(top)
#                 break
#         for i in basic:                  # top, bottom 고정한 상태로 옆면 돌려가면서 최대 숫자를 찾음
#             if max_v < i:
#                 max_v = i
#
#         sum_v += max_v                   # 옆면의 합에 더해준다.
#
#         num += 1                         # 다음 주사위로
#
#     result_list.append(sum_v)            # 마지막 최종 비교를 위해 sum_v를 담아준다.
#
# max_result = 0                           # 최종 최대값
# for i in result_list:                    # 최종 최대값 비교
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
#
# def preorder(n):
#     if n:      # 존재하는 정점이면
#         print(n, end=' ')    # visit(n)
#         preorder(ch1[n])    # 왼쪽 서브트리로 이동
#         preorder(ch2[n])    # 오른쪽 서브트리로 이동
#
#
# V = int(input())
# E = V - 1
# arr = list(map(int, input().split()))
# ch1 = [0] * (V+1)
# ch2 = [0] * (V+1)
# par = [0] * (V+1)
#
# for i in range(E):
#     p, c = arr[i*2], arr[i*2 + 1]
#     if ch1[p] == 0:     # 자식1이 아직 없다면
#         ch1[p] = c
#     else:
#         ch2[p] = c
#
#
#
#     par[c] = p      # 자식을 인덱스로 부모 저장
# # 실제 루트 찾기
# root = 1
# while par[root] != 0:
#     root += 1
#
#
#
# preorder(1)