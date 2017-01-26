/**
    574 - Sum It Up
    
    @author oneshan
    @version 1.0 1/25/2017
*/


#include <iostream>
#include <set>
#define maxn 12
using namespace std;

set<string> ansList;
int value[maxn];

void dfs(string str, int remain, int idx) {
    if (remain == 0) {
        ansList.insert(str);
        return;
    }

    if (idx == 0) {
        return;
    }

    if (remain - value[idx] >= 0) {
        string new_s = str;
        if (str.length()) new_s = "+" + new_s;
        char temp[5];
        sprintf(temp, "%d", value[idx]);
        new_s = temp + new_s;
        dfs(new_s, remain - value[idx], idx - 1); 
    }
    
    dfs(str, remain, idx - 1);
}

int main(int argc, char *argv[])
{
    int total, nlist;

    while (cin >> total >> nlist && total) {

        for (int i = 1; i <= nlist; ++i) {
            cin >> value[i];
        }
        ansList.clear();
        dfs("", total, nlist);

        cout << "Sums of " << total << ":\n";
        if (ansList.empty()) {
            cout << "NONE\n";
        }
        for(set<string>::reverse_iterator iter = ansList.rbegin(); iter != ansList.rend() ; ++iter) {
            cout<<(*iter)<<endl;
        }
    }
    return 0;
}
