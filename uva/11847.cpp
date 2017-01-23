/**
    11847 - Cut the Silver Bar
    
    @author oneshan
    @version 1.0 1/22/2017
*/

#include <iostream>
#include <cmath>
using namespace std;

int main(int argc, char *argv[])
{
    int n;
    while (cin >> n && n) {
        cout << (int)log2(n) << endl;
    }
    return 0;
}
