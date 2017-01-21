/**
    1225 - Digit Counting

    @author oneshan
    @version 1.0 1/20/2017
*/

#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    int nCase;
    cin >> nCase;
    while(nCase--) {
        int sum[10] = {0};
        int nInput;
        cin >> nInput;

        for (int i = 1; i <= nInput; ++i) {
            int tmp = i;
            while (tmp) { sum[tmp%10]++; tmp/=10;}
        }

        for (int i = 0; i < 9; ++i) {
            cout << sum[i] << " ";
        }
        cout << sum[9] << endl;
    }
    return 0;
}
