#include <iostream>

using namespace std;

int N;

void solve()
{
    for (int n = 0; n < (1 << N); n++)
    {
        int count = 0;
        for (int i = N - 1; i >= 0; i--)
        {
            if ((n & (1 << i)) == 0)
                count++; // '('
            else
                count--; // ')'
            if (count < 0)
                break;
        }

        if (count == 0)
        {
            for (int i = N - 1; i >= 0; i--)
            {
                if ((n & (1 << i)) == 0)
                    cout << '(';
                else
                    cout << ')';
            }
            cout << endl;
        }
    }
}

int main(void)
{
    cin >> N;

    solve();
}
