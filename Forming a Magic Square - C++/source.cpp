#include <bits/stdc++.h>
#include <cmath>

using namespace std;

// Complete the formingMagicSquare function below.
int formingMagicSquare(vector<vector<int>> s) {
    int magic_squares[8][3][3] = { {{8,1,6},{3,5,7},{4,9,2}},
                                {{6,1,8},{7,5,3},{2,9,4}},
                                {{4,9,2},{3,5,7},{8,1,6}},
                                {{2,9,4},{7,5,3},{6,1,8}},
                                {{8,3,4},{1,5,9},{6,7,2}},
                                {{4,3,8},{9,5,1},{2,7,6}},
                                {{6,7,2},{1,5,9},{8,3,4}},
                                {{2,7,6},{9,5,1},{4,3,8}} };
    int fees[8] = {};
    int counter = 0;
    int minimum = INT_MAX;
    for(int i = 0;i < 8;i++){
        for(int j =0 ;j < 3;j++){
            for(int k = 0;k < 3;k++){
                fees[counter] += abs(magic_squares[i][j][k] - s[j][k]);
            }
        }
        counter++;
    }
    for(int i = 0;i < 8;i++){
        if(fees[i] < minimum){
           minimum = fees[i];
        }
    }
    return minimum;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    vector<vector<int>> s(3);
    for (int i = 0; i < 3; i++) {
        s[i].resize(3);

        for (int j = 0; j < 3; j++) {
            cin >> s[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    int result = formingMagicSquare(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
