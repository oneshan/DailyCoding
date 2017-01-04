/**
    10082 - WERTYU 

    @author oneshan
    @version 1.0 1/3/2017
*/
#include <iostream>

int main(int argc, char *argv[])
{
    char s[] = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./";
    int i, c;
    while((c = getchar()) != EOF){
        for (i = 1; s[i] && s[i] != c ; ++i);
        if (s[i]) c = s[i-1];
        putchar(c);
    }
    return 0;
}
