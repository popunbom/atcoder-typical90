#include <iostream>
#include <queue>
#include <tuple>
#include <vector>

using namespace std;

int         N;
int         C[100001];
vector<int> G[100001];

void get_max_dist(const int start_i_, int &max_i_, int &max_C_) {
    // Step-1: 頂点1からの最短経路を求める
    queue<int> Q;

    for (int i = 0; i <= N; i++)
        C[i] = -1;

    Q.push(start_i_);
    C[start_i_] = 0;

    int max_C = -1, max_i = -1;
    while (!Q.empty()) {
        int a = Q.front();
        Q.pop();

        for (const int b : G[a]) {
            if (C[b] == -1) {
                Q.push(b);
                C[b] = C[a] + 1;
                if (C[b] > max_C) {
                    max_C = C[b];
                    max_i = b;
                }
            }
        }
    }

    // for (int i = 1; i <= N; i++)
    //     cout << "C[" << i << "] = " << C[i] << endl;
    // cout << "max_C = " << max_C << ", max_i = " << max_i << endl;

    max_i_ = max_i;
    max_C_ = max_C;

    return;
}

void solve() {
    int max_i, max_C, _;
    get_max_dist(1, max_i, _);
    get_max_dist(max_i, _, max_C);
    cout << max_C + 1 << endl;
}

int main(void) {
    cin >> N;

    for (int i = 1; i <= N - 1; i++) {
        int a, b;
        cin >> a >> b;
        G[a].push_back(b);
        G[b].push_back(a);
    }

    // for (int i = 1; i <= N - 1; i++) {
    //     cout << "G[" << i << "] = {";
    //     for (const int g : G[i])
    //         cout << g << ", ";
    //     cout << "}" << endl;
    // }

    solve();
}
