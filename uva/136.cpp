/**
    136 - Ugly Numbers

    @author oneshan
    @version 1.0 1/6/2017
*/

#include <iostream>
#include <algorithm>
using namespace std;

int main(int argc, char *argv[])
{
    long long ugly[1501];
    int n2 = 1, n3 = 1, n5 = 1;
    ugly[1] = 1;
    for (int i = 2; i < 1501; ++i) {
        while(ugly[n2] * 2 <= ugly[i-1]) n2++;
        while(ugly[n3] * 3 <= ugly[i-1]) n3++;
        while(ugly[n5] * 5 <= ugly[i-1]) n5++;
        ugly[i] = min(ugly[n2]*2, min(ugly[n3]*3, ugly[n5]*5));
    }
    cout << "The 1500'th ugly number is " << ugly[1500] << ".\n";
    return 0;
}
