/**
    10127 - Ones
    
    @author oneshan
    @version 1.0 1/23/2017

    11 % N = (  10 + 1) % N = [10 * (  1 % N) + 1] % N
   111 % N = ( 110 + 1) % N = [10 * ( 11 % N) + 1] % N
  1111 % N = (1110 + 1) % N = [10 * (111 % N) + 1] % N

*/

#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    int num;
    while (cin >> num) {
        int count = 1, remain = 1;
        while (remain % num) {
            remain = (10 * remain + 1) % num;
            count++;
        }
        cout << count << endl;
    }
    return 0;
}
