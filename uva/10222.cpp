/**
    10222 - Decode the Mad man

    @author oneshan
    @version 1.0 1/28/2017
*/

#include <iostream>
using namespace std;

const char keyboard[] = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./";

int main(int argc, char *argv[])
{
    char c;
    while((c=getchar()) != EOF){
        c = tolower(c);
        if (c == ' ' || c == '\n')
            cout << c;
        for (int i = 0; keyboard[i]; ++i) {
            if (c == keyboard[i])
                cout << keyboard[i-2];
        }
    }
    return 0;
}
