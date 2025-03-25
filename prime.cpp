#include <iostream>

using namespace std;

int main()
{
    int n;
    cout << "Enter a number: ";
    cin >> n;
    int i;
    int isPrime = 1;
    for (i = 2; i < n / 2; i++)
    {
        if (n % i == 0)
        {
            isPrime = 0;
            break;
        }
    }
    if (isPrime)
    {
        cout << "Prime Number" << endl;
    }
    else
    {
        cout << "Not a Prime Number" << endl;
    }
    return 0;
}