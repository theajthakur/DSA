#include <iostream>
using namespace std;

int main()
{
    int a = cin.get();
    if (a >= 97 + 25 || a < 48)
    {
        cout << "You entered a Symbol Character" << endl;
    }
    else if (a >= 97)
    {
        cout << "You entered a Lowercase Character" << endl;
    }
    else if (a >= 65)
    {
        cout << "You entered a Uppercase Character" << endl;
    }
    else if (a >= 48)
    {
        cout << "You entered a Number" << endl;
    }
    else
    {
        cout << "You entered a Special Character" << endl;
    }

    return 0;
}