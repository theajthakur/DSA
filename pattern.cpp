#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;

    // Counting Pattern
    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 1; j <= n; j++)
    //     {
    //         cout << n * i + j << "\t";
    //     }
    //     cout << "\n";
    // }

    // Descending Count from Row number
    for (int i = 1; i <= n; i++)
    {
        for (int j = i; j >= 1; j--)
        {
            cout << j;
        }
        cout << endl;
    }

    return 0;
}