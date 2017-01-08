#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    int numVessel, numContainer;
    int c[1000001];

    while(cin >> numVessel >> numContainer){
        // Binary Search: max(c[i]) ~ sum(c[i])
        int left = 0, right = 0, mid;
        for (int i = 0; i < numVessel; ++i) {
            cin >> c[i];
            if (left < c[i]) left = c[i];
            right += c[i];
        }

        while (left < right){
            mid = left + (right - left) / 2;
            int sum = 0, count = 0;
            for (int i = 0; i < numVessel; ++i) {
                sum += c[i];
                if (sum > mid){
                    count++;
                    sum = c[i];
                } else if (sum == mid){
                    count++;
                    sum = 0;
                }
            }
            if (sum) count++;

            if (count <= numContainer){
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        cout << right << endl;
    }
    return 0;
}
