/**
    272 - TEX Quotes

    @author oneshan
    @version 1.0 1/2/2017
*/

#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    bool check = true;
    char c;
    while( (c = getchar()) != EOF){
        if (c == '"'){
            if (check)
                cout << "``";
            else
                cout << "''";
            check = !check;
        }
        else
            cout << c;
    }
    return 0;
}
