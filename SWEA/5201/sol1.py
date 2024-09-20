T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    cargo_ls = sorted(list(map(int,input().split())),reverse=True)      # 화물을 크키가 큰 순서대로 받아오기
    truck_ls = sorted(list(map(int,input().split())),reverse=True)      # 트럭의 용량도 큰 순서대로 받아오기
    taken = [0] * N         # 다른 차가 화물을 챙겨갔는지 체크하기 위한 리스트
    overall_cargo = 0       # 총 화물 무게 합을 위한 변수
    for truck in truck_ls:  # truck마다 받아오는데
        for i in range(N):
            if truck >= cargo_ls[i] and not taken[i]:       # truck이 화물의 무게보다 많이 들수 있고, 화물이 가져가지지 않았다면
                overall_cargo += cargo_ls[i]                # 전체 화물 무게에 더해주고
                taken[i] = 1                                # 가져갔다고 체크한다.
                break                                       # 다른 화물은 가져가지 않을 수 있도록 break 해준다.
    print(f'#{tc} {overall_cargo}')