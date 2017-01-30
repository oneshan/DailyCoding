/**
    11362 - Phone List
    
    @author oneshan
    @version 1.0 1/29/2017
*/

#include <iostream>
#include <algorithm>
#define maxn 10002
using namespace std;

int main(int argc, char *argv[])
{
    int t, n;
    string s[maxn];
    cin >> t;
    while (t--) {
        cin >> n;
        for (int i = 0; i < n; ++i)
            cin >> s[i];

        sort(s, s+n);

        string ans = "YES";
        for (int i = 0; i < n-1; ++i) {

            if (s[i].length() > s[i+1].length())
                continue;

            bool samePrefix = true;
            for (int j = 0; j < s[i].length(); ++j)
                if (s[i][j] != s[i+1][j]) {
                    samePrefix = false;
                    break;
                }
            if (samePrefix) {
                ans = "NO";
                break;
            }
        }
        cout << ans << endl;
    }
    return 0;
}
