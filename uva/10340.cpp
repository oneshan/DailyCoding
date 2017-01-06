/**
    10340 - All in All

    @author oneshan
    @version 1.0 1/5/2017
*/

#include <iostream>
#include <string>
using namespace std;

int main(int argc, char *argv[])
{
    string s1, s2;
    while(cin>>s1>>s2){
        int idx = 0, maxlen = s1.length();
        for (int i = 0; i < s2.length(); ++i){
            if (s1[idx] == s2[i]) ++idx;
            if (idx == maxlen) break;
        }
        if (idx == maxlen)
            cout << "Yes\n";
        else
            cout << "No\n";
    }
    return 0;
}
