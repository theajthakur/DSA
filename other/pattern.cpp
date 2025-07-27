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
    // for (int i = 1; i <= n; i++)
    // {
    //     for (int j = i; j >= 1; j--)
    //     {
    //         cout << j;
    //     }
    //     cout << endl;
    // }

    // Alphabets Increment Pattern
    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < n; j++)
    //     {
    //         int num = i + j;
    //         char ch = num + 65;
    //         cout << ch << "\t";
    //     }
    //     cout << endl;
    // }

    // Alphabets Reverse Triangle Pattern
    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = i; j >= 0; j--)
    //     {
    //         char ch = 65 + n - j - 1;
    //         cout << ch << "\t";
    //     }
    //     cout << endl;
    // }

    // UpDown Count Star Filler pattern

    for (int i = 0; i < n; i++)
    {
        for (int j = 1; j <= n - i; j++)
        {
            cout << j << " ";
        }

        for (int j = 0; j < 2 * i; j++)
        {
            cout << "*" << " ";
        }

        for (int j = n - i; j > 0; j--)
        {
            cout << j << " ";
        }

        cout << endl;
    }

    return 0;
}