/**
    465 - Overflow
    
    @author oneshan
    @version 1.0 1/15/2017
*/


#include <iostream>
#define INF 2147483647
using namespace std;

int main(int argc, char *argv[])
{
    char s1[1000], s2[1000];
    char op;
    while (cin >> s1 >> op >> s2) {
        cout << s1 << " " << op << " " << s2 << endl;
        double num1 = atof(s1);
        double num2 = atof(s2);
        if (num1 > INF)
            cout << "first number too big\n";
        if (num2 > INF)
            cout << "second number too big\n";
        if (op == '+' && num1 + num2 > INF)
            cout << "result too big\n";
        if (op == '*' && num1 * num2 > INF)
            cout << "result too big\n";
    }
    return 0;
}
