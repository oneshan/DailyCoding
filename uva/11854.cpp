/**
    11854 - Egypt
    
    @author oneshan
    @version 1.0 2/2/2017
*/

#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    int a, b, c, sum;
    while (cin >> a >> b >> c && a) {
        a *= a;
        b *= b;
        c *= c;
        sum = (a + b + c) / 2;
        if (sum == a || sum == b || sum == c)
            cout << "right\n";
        else
            cout << "wrong\n";
    }
    return 0;
}
