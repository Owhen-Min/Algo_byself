def main():
    for _ in range(int(input())):
        n = int(input())
        arr = [a - 1 for a in (map(int, input().split()))]

        # 각 노드의 진입 차수(indegree) 계산
        counts = [0] * n
        for a in arr:
            counts[a] += 1

        # 진입 차수가 0인 노드들을 찾음 (시작점들)
        ends = [i for i, c in enumerate(counts) if c == 0]
        i = 0

        # 위상 정렬 유사 알고리즘
        while i < len(ends):
            x = arr[ends[i]]  # 현재 노드가 가리키는 노드
            i += 1
            counts[x] -= 1    # 진입 차수 감소
            if counts[x] == 0:  # 새로운 진입 차수 0 노드 발견
                ends.append(x)

        # 진입 차수가 0인 노드 수 = 사이클에 포함되지 않은 노드 수
        ans = counts.count(0)
        print(ans)

if __name__ == "__main__":
    main()