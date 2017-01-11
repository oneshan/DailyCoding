/**
    10042 - Smith Numbers
    
    @author oneshan
    @version 1.0 1/10/2017
*/

#include <iostream>
#include <cmath>
using namespace std;

int sumDigits(int num){
    int sum = 0;
    while (num){
        sum += num % 10;
        num /= 10;
    }
    return sum;
}

int main(int argc, char *argv[])
{
    int n, num;
    cin >> n;
    while (n--){
        cin >> num;
        while (true){
            num++;
            int sum_of_num = sumDigits(num);
            int sum_of_prime = 0;
            int tmp = num;
            for (int i = 2; i <= sqrt(tmp * 1.0); ++i) {
                while (tmp % i == 0){
                    sum_of_prime += sumDigits(i);
                    tmp /= i;
                }
            }
            if (tmp == num) continue; // num is Prime
            if (tmp != 1) sum_of_prime += sumDigits(tmp);
            if (sum_of_num == sum_of_prime) break;
        }
        cout << num << endl;
    }
    return 0;
}
