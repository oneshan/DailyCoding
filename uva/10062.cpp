/**
    10062 - Tell me the frequencies!
    
    @author oneshan
    @version 1.0 1/26/2017
*/

#include <iostream>
#include <cstring>
using namespace std;

int main(int argc, char *argv[])
{
    int freq[129] = {0}, count = 0;
    char c;
    bool pLn = false;
    while((c = getchar()) != EOF) {
        if (c == '\n') {
            if (pLn) cout << endl;
            for (int i = 1; i <= count; ++i) {
                for (int j = 128; j >= 32; --j)
                    if (i == freq[j])
                        cout << j << " " << freq[j] << endl;
            }
            memset(freq, 0, sizeof(freq));
            count = 0;
            pLn = true;
        }
        freq[(int)c] += 1;
        count++;
    }
    return 0;
}
