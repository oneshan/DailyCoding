/**
    1585 - Score
    
    @author oneshan
    @version 1.0 1/17/2017
*/

#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    int T;
    cin >> T;
    while (T--) {
        int nCorrect = 0, sum = 0;
        string s;
        cin >> s;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == 'X')
                nCorrect = 0;
            else
                nCorrect++;
            sum += nCorrect;
        }
        cout << sum << endl;
    }
    return 0;
}
