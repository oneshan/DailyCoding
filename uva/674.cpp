/**
    674 - Coin Change
    
    @author oneshan
    @version 1.0 1/13/2017
*/


#include <iostream>
#define maxn 7490
using namespace std;


int main(int argc, char *argv[])
{
    int ans[maxn] = {0};
    int coins[5] = {1, 5, 10, 25, 50};
    ans[0] = 1;
    for (int i = 0; i < 5; ++i) {
        for (int j = coins[i]; j <= maxn; ++j) {
            ans[j] += ans[j-coins[i]];
        }
    }
    int n;
    while (cin >> n){
        cout << ans[n] << endl;
    }
    return 0;
}
