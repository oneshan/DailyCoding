/**
    12019 - Doom's Day Algorithm
    
    @author oneshan
    @version 1.0 1/23/2017
*/

#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    int nCase;
    int monthday[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    string weekday[7] = {"Monday", "Tuesday", "Wednesday", "Thursday",
                         "Friday", "Saturday", "Sunday"};

    cin >> nCase;
    while (nCase--) {
        int month, day, idx = 4;
        cin >> month >> day;
        
        for (int i = 1; i < month; ++i) {
            idx += monthday[i];
        }
        idx += day;
        cout << weekday[idx % 7] << endl;
    }
    return 0;
}
