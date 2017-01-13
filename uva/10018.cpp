/**
    10018 - Reverse and Add
    
    @author oneshan
    @version 1.0 1/12/2017
*/


#include <iostream>
using namespace std;

long reverse(long P){
    long rev = 0;
    while(P){
        rev *= 10;
        rev += P % 10;
        P /= 10;
    }
    return rev;
}

int main(int argc, char *argv[])
{
    int N;
    long P;
    cin >> N;
    while (N--){
        cin >> P;
        int count = 0;
        long rev = reverse(P);
        while(P != rev){
            P += rev;
            count++;
            rev = reverse(P);
        }
        cout << count << " " << P << endl;
    }
    return 0;
}
