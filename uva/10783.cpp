/**
    10783 - Odd Sum

    @author oneshan
    @version 1.0 1/18/2017
*/

#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    int nCase;
    cin >> nCase;
    for (int i = 1; i <= nCase; ++i) {
        int a, b, sum;
        cin >> a >> b;
        a = a / 2;
        b = (b + 1) / 2;
        sum = b * b - a * a;
        cout << "Case " << i << ": " << sum << endl;
    }
    return 0;
}
