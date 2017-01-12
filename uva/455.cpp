/**
    455 - Periodic Strings 
    
    @author oneshan
    @version 1.0 1/11/2017
*/

#include <iostream>
#include <string>
using namespace std;

int main(int argc, char *argv[])
{
    int count, maxlen, ans;
    string s;
    cin >> count;
    while (count--){
        cin >> s;
        ans = maxlen = s.length();
        for (int i = 1; i < maxlen; ++i) {
            if (maxlen % i) continue;
            int j = i;
            while (j < maxlen && s[j] == s[j % i]) j++;
            if (j == maxlen){
                ans = i;
                break;
            }
        }
        cout << ans << endl;
        if (count) cout << endl;
    }
    return 0;
}
