#include <iostream>

using namespace std;

int H, W;
int A[2000][2000];
int SW[2000], SH[2000];

void solve()
{

    for (size_t i = 0; i < H; i++)
    {
        for (size_t j = 0; j < W; j++)
        {
            SW[i] += A[i][j];
            SH[j] += A[i][j];
        }
    }

    for (size_t i = 0; i < H; i++)
    {
        for (size_t j = 0; j < W; j++)
            cout << SW[i] + SH[j] - A[i][j] << ' ';
        cout << endl;
    }
}

int main(void)
{
    cin >> H >> W;

    for (size_t i = 0; i < H; i++)
        for (size_t j = 0; j < W; j++)
            cin >> A[i][j];

    solve();
}
