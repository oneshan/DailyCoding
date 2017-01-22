/**
    232 - Crossword Answers
    
    @author oneshan
    @version 1.0 1/21/2017
*/


#include <iostream>
#include <iomanip>
#define maxn 12
using namespace std;

int main(int argc, char *argv[])
{
    int nRow, nCol, nCase;
    char puzzle[maxn][maxn];

    for (int i = 0; i<= maxn; ++i) {
        puzzle[i][0] = '*';
        puzzle[0][i] = '*';
    }

    while (cin >> nRow >> nCol) {
        int id = 1;
        int pid[maxn][maxn] = {0};

        for (int i = 1; i <= nRow; ++i) {
            for (int j = 1; j <= nCol; ++j) {
                cin >> puzzle[i][j];
                if (puzzle[i][j] != '*' && (puzzle[i-1][j] == '*' || puzzle[i][j-1] == '*'))
                    pid[i][j] = id++;
            }
        }

        if (nCase) cout << endl;
        cout << "puzzle #" << ++nCase << ":\n";

        cout << "Across";
        for (int i = 1; i <= nRow; ++i) {
            for (int j = 1; j <= nCol; ++j) {
                if (puzzle[i][j] != '*' && puzzle[i][j-1] == '*') {
                    cout << "\n" << setw(3) << pid[i][j] << ".";
                    int k = j;
                    while(k <= nCol && puzzle[i][k] != '*')
                        cout << puzzle[i][k++];
                }
            }
        }
        cout << endl;

        cout << "Down";
        for (int i = 1; i <= nRow; ++i) {
            for (int j = 1; j <= nCol; ++j) {
                if (puzzle[i][j] != '*' && puzzle[i-1][j] == '*') {
                    cout << "\n" << setw(3) << pid[i][j] << ".";
                    int k = i;
                    while(k <= nRow && puzzle[k][j] != '*')
                        cout << puzzle[k++][j];
                }
            }
        }
        cout << endl;

    }
    return 0;
}
