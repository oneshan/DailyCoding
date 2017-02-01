/**
    11364 - Parking
    
    @author oneshan
    @version 1.0 1/31/2017
*/

#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    int nCase, nStore;
    cin >> nCase;
    while (nCase--) {
        cin >> nStore;
        int pos, min = 100, max = -1;
        while (nStore--) {
            cin >> pos;
            if (pos < min)
                min = pos;
            if (pos > max)
                max = pos;
        }
        cout << 2 * (max - min) << endl;
    }
    return 0;
}
