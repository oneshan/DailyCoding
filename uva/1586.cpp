/**
    1586 - Molar mass
    
    @author oneshan
    @version 1.0 1/20/2017
*/


#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    int T;
    cin >> T;
    while (T--) {
        int count = 0;
        float weight = 0, mass = 0;
        string s;
        cin >> s;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] > 'A') {
                mass += weight * ((count > 0) ? count: 1);
                count = 0;
                if (s[i] == 'C') weight = 12.01;
                else if (s[i] == 'H') weight = 1.008;
                else if (s[i] == 'O') weight = 16.00;
                else weight = 14.01; 
            } else {
                count *= 10;
                count += (s[i]-'0');
            }
        }
        mass += weight * ((count > 0) ? count: 1);
        printf("%.3f\n", mass);
    }
    return 0;
}
