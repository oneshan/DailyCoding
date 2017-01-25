/**
    725 - Division

    @author oneshan
    @version 1.0 1/24/2017
*/

#include <iostream>
#include <iomanip>
using namespace std;

bool check(int abcde, int fghij)
{
    int used[10] = {0};
    if (fghij < 10000)
        used[0] = 1;
    while (abcde) {
        if (used[abcde % 10]) return false;
        used[abcde % 10] = 1;
        abcde /= 10;
    }
    while (fghij) {
        if (used[fghij % 10]) return false;
        used[fghij % 10] = 1;
        fghij /= 10;
    }
    return true;
}

int main(int argc, char *argv[])
{
    int N, nCase = 0;
    while (cin >> N && N) {
        bool noAns = true;
        if (nCase++) {
            cout << endl;
        }

        for (int num2 = 1234; num2 <= 98765/N; ++num2) {
            int num1 = num2 * N;
            if (num1 < 10000) continue;
            if (check(num1, num2)) {
                noAns = false;
                cout << setw(5) << setfill('0') << num1 << " / ";
                cout << setw(5) << setfill('0') << num2 << " = " << N << endl;
            }
        }
        
        if (noAns) {
            cout << "There are no solutions for " << N << ".\n";
        }
    }
    return 0;
}

