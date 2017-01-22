/**
    232 - Crossword Answers
    
    @author oneshan
    @version 1.1 1/21/2017
*/


#include <iostream>
#include <iomanip>
#define maxn 12
using namespace std;

struct Point {
    int x;
    int y;
};

int main(int argc, char *argv[])
{
    int nRow, nCol, nCase;
    char puzzle[maxn][maxn];
    Point pid[maxn * maxn];

    for (int i = 0; i<= maxn; ++i) {
        puzzle[i][0] = '*';
        puzzle[0][i] = '*';
    }

    while (cin >> nRow >> nCol) {
        int id = 1;

        for (int i = 1; i <= nRow; ++i) {
            for (int j = 1; j <= nCol; ++j) {
                cin >> puzzle[i][j];
                if (puzzle[i][j] != '*' && (puzzle[i-1][j] == '*' || puzzle[i][j-1] == '*')) {
                    pid[id].x = i;
                    pid[id].y = j;
                    id++;
                }
            }
        }

        if (nCase) cout << endl;
        cout << "puzzle #" << ++nCase << ":\n";

        cout << "Across";
        for (int cnt = 1; cnt < id; cnt++) {
            int i = pid[cnt].x;
            int j = pid[cnt].y;

            if (puzzle[i][j] != '*' && puzzle[i][j-1] == '*') {
                cout << "\n" << setw(3) << cnt << ".";
                while(j <= nCol && puzzle[i][j] != '*')
                    cout << puzzle[i][j++];
            }
        }
        cout << endl;

        cout << "Down";
        for (int cnt = 1; cnt < id; cnt++) {
            int i = pid[cnt].x;
            int j = pid[cnt].y;

            if (puzzle[i][j] != '*' && puzzle[i-1][j] == '*') {
                cout << "\n" << setw(3) << cnt << ".";
                while(i <= nRow && puzzle[i][j] != '*')
                    cout << puzzle[i++][j];
            }
        }
        cout << endl;

    }
    return 0;
}
