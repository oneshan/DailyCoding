/**
    11764 - Jumping Mario
    
    @author oneshan
    @version 1.0 1/19/2017
*/


#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    int nCase;
    cin >> nCase;
    for (int i = 1; i <= nCase; ++i) {
        int nJump, highCount = 0, lowCount = 0, a[2] = {0};
        cin >> nJump;
        cin >> a[nJump & 1];
        while(--nJump){
           cin >> a[nJump & 1];
           if (a[nJump & 1] > a[(nJump + 1) & 1]) highCount++;
           if (a[nJump & 1] < a[(nJump + 1) & 1]) lowCount++;
        }
        cout << "Case " << i << ": " << highCount << " " << lowCount << endl;
    }
    return 0;
}
