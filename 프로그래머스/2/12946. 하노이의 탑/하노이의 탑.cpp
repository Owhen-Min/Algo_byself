#include <vector>
using namespace std;

void hanoi(int n, int start, int end, int temp, vector<vector<int>>& result) {
    if (n == 1) {
        result.push_back({start, end});
        return;
    }
    
    hanoi(n - 1, start, temp, end, result);
    result.push_back({start, end});
    hanoi(n - 1, temp, end, start, result);
}

vector<vector<int>> solution(int n) {
    vector<vector<int>> answer;
    answer.reserve((1 << n) - 1);  // 2^n - 1 크기로 미리 할당
    hanoi(n, 1, 3, 2, answer);
    return answer;
}
