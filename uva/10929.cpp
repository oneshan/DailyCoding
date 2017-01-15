/**
    10929 - You can say 11

    @author oneshan
    @version 1.0 1/14/2017
*/

#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    string s;
    while (cin >> s && s != "0"){
        int sum[2] = {0}; // sum of odd and even
        for (int i = 0; i < s.length(); ++i) {
            sum[i & 1] += (s[i] - '0');
        }
        if ((sum[0] - sum[1]) % 11)
            cout << s << " is not a multiple of 11.\n";
        else
            cout << s << " is a multiple of 11.\n";

    }
    return 0;
}
