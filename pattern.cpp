#include <iostream>
using namespace std;
int main()
{
    int n;
    cin >> n;

    // Counting Pattern
    for (int i = 0; i < n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            cout << n * i + j << "\t";
        }
        cout << "\n";
    }

    return 0;
}