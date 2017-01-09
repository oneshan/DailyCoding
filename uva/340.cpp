/**
    340 - Master-Mind Hints
    
    @author oneshan
    @version 1.0 1/8/2017
*/

#include <iostream>
#define maxn 1001
using namespace std;

int main(int argc, char *argv[])
{
    int length, count = 0;
    int ans[maxn], guess[maxn];
    while(cin >> length && length){
        cout << "Game " << ++count << ":\n";
        for (int i = 0; i < length; ++i) {
            cin >> ans[i];        
        }

        while(true){
            int a = 0, b = 0;
            for (int i = 0; i < length; ++i) {
                cin >> guess[i];
                if (ans[i] == guess[i]) a++;
            }
            if (guess[0] == 0) break;

            for (int d = 1; d < 10; ++d) {
                int c1 = 0, c2 = 0;
                for (int i = 0; i < length; ++i) {
                    if (d == ans[i]) c1++;
                    if (d == guess[i]) c2++;
                }
                b += c1 < c2 ? c1 : c2;
            }
            printf("    (%d,%d)\n", a, b-a);
        }
    }
    return 0;
}
