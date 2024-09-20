def nodesum(target):
    if target:          # 타겟 노드가 0이 아니라면
        if values[target]:          # 타겟 노드에 값이 있다면
            return values[target]   # 타겟 노드의 값을 반환
        else:                       # 아니라면 left와 right의 값의 합을 반환
            return nodesum(left[target]) + nodesum(right[target])
    else: return 0      # 타겟 노드가 0이라면(자식이 없었다면 0을 반환)


T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int,input().split())
    # 전체 노드의 수 N, 리프 노드의 수 M, 타겟숫자 L
    left = [0] * (N+1)
    right = [0] * (N+1)

    i = 2
    while i <= N:
        if i%2 : right[i//2]=i
        else : left[i//2]=i
        i += 1
    # 완전 이진 트리 작성
    
    values = [0] * (N+1)
    # 이진 트리의 값을 담을 리스트 values
    
    for _ in range(M):
        node, number = map(int,input().split())
        values[node] = number
    # 리프 노드에 숫자 입력

    print(f'#{tc} {nodesum(L)}')