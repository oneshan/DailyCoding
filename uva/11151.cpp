/**
    11151 - Longest Palindrome

    @author oneshan
    @version 1.0 1/27/2017
*/

#include <iostream>
#include <cstring>
#define maxn 1002
using namespace std;

int main(int argc, char *argv[])
{
    int T, lcs[maxn][maxn];
    char s[maxn];
    cin >> T;
    getchar();
    while (T--) {
        int n = 0;
        // empty line is also a valid input which outupt = 0
        while( (s[n++]=getchar()) != '\n');
        n--;
        memset(lcs, 0, sizeof(lcs));

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (s[i] == s[n-1-j])
                    lcs[i+1][j+1] = lcs[i][j] + 1;
                else
                    lcs[i+1][j+1] = max(lcs[i][j+1], lcs[i+1][j]);
            }
        }
        cout << lcs[n][n] << endl;
    }
    return 0;
}
