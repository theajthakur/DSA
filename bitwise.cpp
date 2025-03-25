#include <iostream>
using namespace std;

int main()
{
    int a = 4;
    int b = 6;
    cout << "a & b : " << (a & b) << endl;
    cout << "a | b : " << (a | b) << endl;
    cout << "~b : " << (~b) << endl;
    cout << "a ^ b : " << (a ^ b) << endl;
    return 0;
}

// a    = 100
// b    = 110

// a&b  = 100 = 4
// a|b  = 110 = 6
// ~b   = 110 -> 1111001 -> 000110 -> 0111 -> -7
// a^b  = 010 = 2