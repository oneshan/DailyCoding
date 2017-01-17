/**
    1584 - Circular Sequence
    
    @author oneshan
    @version 1.0 1/17/2017
*/


#include <iostream>
#define maxn 101
using namespace std;

int main(int argc, char *argv[])
{
    string s;
    int T;
    cin >> T;
    while (T--) {
        cin >> s;
        int ans = 0, maxlen = s.length();
        for (int i = 0; i < maxlen; ++i) {
            for (int j = 0; j < maxlen; ++j) {
                if (s[(i + j) % maxlen] == s[(ans + j) % maxlen])
                    continue;
                if (s[(i + j) % maxlen] < s[(ans + j) % maxlen])
                    ans = i;
                break;
            }
        }

        for (int i = 0; i < maxlen; ++i) 
            cout << s[(ans + i) % maxlen];
        cout << endl;
    }
    return 0;
}
