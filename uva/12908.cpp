/**
    12908 - The book thief

    @author oneshan
    @version 1.0 2/1/2017
*/
#include <iostream>
#define maxn 14150
using namespace std;

int main(int argc, char *argv[])
{
    int sum_p;
    int sum[maxn];

    sum[0] = 0;
    for (int i = 1; i < maxn; ++i) {
        sum[i] = sum[i-1] + i;
    }

    while (cin >> sum_p && sum_p) {
        int left = 0, right = maxn-1, mid;
        while (left < right) {
            mid = (left + right) / 2;
            if (sum[mid] > sum_p)
                right = mid;
            else
                left = mid+1;
        }
        if (sum[left] - sum_p > left)
            left--;
        cout << sum[left] - sum_p << " " << left << endl; 
    }
    return 0;
}
