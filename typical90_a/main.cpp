#include <iostream>

using namespace std;

int N, L, K;
int A[100000];

bool check(int m) {
    int count = 0;
    int prev  = 0;
    for (int i = 0; i < N; i++) {
        if (A[i] - prev >= m && L - A[i] >= m) {
            count++;
            prev = A[i];
        }
    }
    return count >= K;
}

void solve() {
    int ok = -1;
    int ng = L + 1;

    int mid;
    while (abs(ok - ng) > 1) {
        mid = (ok + ng) / 2;
        if (check(mid)) {
            ok = mid;
        } else {
            ng = mid;
        }
    }
    cout << ok << endl;
}

int main(void) {
    cin >> N >> L >> K;
    for (int i = 0; i < N; i++)
        cin >> A[i];

    solve();
}
