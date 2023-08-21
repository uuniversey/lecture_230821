

# 18544. 전위 순회

# import sys
# sys.stdin = open('input_18544.txt', 'r')
#
#
# def pre_rot(node):
#     global V
#     if 0 < node <= V:
#         print(node, end=' ')
#         if node != V:
#             pre_rot(left[node])
#             pre_rot(right[node])
#
#
# V = int(input())
# tree = list(map(int, input().split()))
# left = [0] * V
# right = [0] * V
#
# for i in range(len(tree)//2):
#     idx, line = tree[2*i], tree[2*i + 1]
#     if left[idx] == 0:
#         left[idx] = line
#     else:
#         right[idx] = line
#
# pre_rot(1)


# 1231. 중위 순회

# import sys
# sys.stdin = open('input_1231.txt', 'r')
#
#
# def mid_rot(n):                # 중위 순회 함수
#     global my_str
#     if n:
#         mid_rot(left[n])
#         my_str += my_dic[n]     # dic에 들은 정보를 str에 붙여준다.
#         mid_rot(right[n])
#
#
# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [input().split() for _ in range(N)]
#     left = [0] * (N+1)          # tree의 왼쪽
#     right = [0] * (N+1)         # tree의 오른쪽
#     my_dic = {}
#     my_str = ''
#     for j in range(N):          # dic에 숫자를 키값으로 낱말을 밸류값으로 넣는다.
#         my_dic[int(arr[j][0])] = arr[j][1]
#
#     for i in range(N):
#         if len(arr[i]) == 4:    # 정보 4개 일때 처리
#             left[int(arr[i][0])] = int(arr[i][2])
#             right[int(arr[i][0])] = int(arr[i][3])
#         elif len(arr[i]) == 3:  # 정보 3개 일때 처리
#             left[int(arr[i][0])] = int(arr[i][2])
#             # 정보 2개 일때는 자식 노드가 없기 때문에 처리해줄 필요 없다.
#
#     mid_rot(1)
#
#     print(f'#{tc} {my_str}')


# 5174. subtree

import sys
sys.stdin = open('input_5174.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = [[] for _ in range(E+2)]
    num = 1

    for i in range(E):
        tree[arr[2*i]].append(arr[2*i + 1])