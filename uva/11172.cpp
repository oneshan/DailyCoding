/**
    11172 - Relational Operator
    
    @author oneshan
    @version 1.0 1/16/2017
*/

#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    int t;
    cin >> t;
    while (t--) {
        int num1, num2;
        cin >> num1 >> num2;
        if (num1 > num2)
            cout << ">\n";
        else if (num1 < num2)
            cout << "<\n";
        else
            cout << "=\n";
    }
    return 0;
}
