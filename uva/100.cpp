/**
    100 - The 3n + 1 problem
    
    @author oneshan
    @version 1.0 1/1/2017
*/

#include <iostream>
#define maxn 1000001
using namespace std;

int cycle[maxn];

int cyclelength(int ori_n){
    if (cycle[ori_n]) return cycle[ori_n];
    int n = ori_n, count = 1;
    while( n != 1){
        if (n & 1)
            n = 3 * n + 1;
        else
            n /= 2;
        count++;
    }
    cycle[ori_n] = count;
    return count;
}

int main(int argc, char *argv[])
{
    int tmp, start, end, maxlen, termlen;
    while(cin>>start>>end){
        cout << start << " " << end << " ";
        if (start > end){ tmp=start; start=end; end=tmp;}
        maxlen = 0;
        for (int n = start; n <= end; ++n) {
            termlen = cyclelength(n);
            if (maxlen < termlen) maxlen = termlen;
        }
        cout << maxlen << endl;
    }
    return 0;
}
