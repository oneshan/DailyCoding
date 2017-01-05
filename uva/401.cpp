/**
    401 - Palindromes

    @author oneshan
    @version 1.0 1/4/2017
*/

#include <iostream>
#include <cstring>
using namespace std;

char r[] = "A   3  HIL JM O   2TUVWXY51SE Z  8 ";
char reverse(char ch){
    if (ch - 'A' >= 0)
        return r[ch-'A'];
    return r[ch-'0' + 25];
}

int main(int argc, char *argv[])
{
    char s[25];
    while (scanf("%s", s) == 1){
        int len = strlen(s);
        int isPalindrome = 1, isMorrored = 1;
        for (int i = 0; i < (len+1)/2; ++i) {
            if (s[i] != s[len-1-i]) isPalindrome = 0;
            if (reverse(s[i]) != s[len-1-i]) isMorrored = 0;
        }
        cout << s << " -- is ";
        if (isMorrored && isPalindrome) cout << "a mirrored palindrome.\n\n";
        else if (isMorrored) cout << "a mirrored string.\n\n";
        else if (isPalindrome) cout << "a regular palindrome.\n\n";
        else cout << "not a palindrome.\n\n";
    }
    return 0;
}
