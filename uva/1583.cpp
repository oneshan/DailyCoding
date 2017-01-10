/**
    1583 - Digit Generator
    
    @author oneshan
    @version 1.0 1/9/2017
*/

#include <iostream>
#define maxn 100001
using namespace std;


int main(int argc, char *argv[])
{
    int count, num, ans[maxn] = {};
    int x, y;
    for (int i = 0; i < maxn; ++i) {
        x = y = i;
        while(x) { y += x % 10; x /= 10;}
        if (!ans[y]) ans[y] = i;
    }

    cin >> count;
    while (count--){
        cin >> num;
        cout << ans[num] << endl;
    }

    return 0;
}
