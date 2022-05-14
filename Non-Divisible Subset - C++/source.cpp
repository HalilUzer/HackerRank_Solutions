#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);


inline void set_mods(vector<int>&, vector<int>&, int);
inline int** set_combination(int**, int);
inline void choose_forbiddens(vector<int>&, vector<int>&, int**, int);
int counts(vector<int>&, int);
bool check(int, vector<int>&);
void add_chosens(vector<int>&, vector<int>&, vector<int>&, vector<int>&,int);

void set_mods(vector<int>& set, vector<int>& modded_set, int k) { //vectore  böl çek
    for (int i = 0; i < set.size(); i++) {
        modded_set.push_back(set[i] % k);
    }
}

inline int** set_combination(int** combinations, int k) { // bütün kombinasyonları bul
    combinations = new int* [(k / 2)];
    for (int i = 0; i < (k / 2); i++) {
        combinations[i] = new int[2];
    }
    for (int i = 0; i < k / 2; i++) {
        combinations[i][0] = i + 1;
        combinations[i][1] = k - i - 1;
    }
    return combinations;
}

void inline choose_forbiddens(vector<int>& forbiddens, vector<int>& modded_set, int** combinations, int k) { // iki sayı arasında seçim yap
    int counter_1 = 0;
    int counter_2 = 0;
    int zero = 0;
    int number = k / 2;
    if (k % 2 == 0) {
        for (int i = 0; i < (k / 2); i++) {
            counter_1 = counts(modded_set, combinations[i][0]);
            counter_2 = counts(modded_set, combinations[i][1]);
            if (counter_1 < counter_2) {
                forbiddens.push_back(combinations[i][0]);
            }
            else if (counter_1 >= counter_2) {
                forbiddens.push_back(combinations[i][1]);
            }
        }
        forbiddens.push_back(number);
        forbiddens.push_back(zero);
    }
    else {
        for (int i = 0; i < (k / 2); i++) {
            counter_1 = counts(modded_set, combinations[i][0]);
            counter_2 = counts(modded_set, combinations[i][1]);
            if (counter_1 < counter_2) {
                forbiddens.push_back(combinations[i][0]);
            }
            else if (counter_1 >= counter_2) {
                forbiddens.push_back(combinations[i][1]);
            }
        }
        forbiddens.push_back(zero);
    }
}

int counts(vector<int>& modded_set, int number) { // çıkan sayıları kontrol et
    int counter = 0;
    for (int i = 0; i < modded_set.size(); i++) {
        if (number == modded_set[i]) {
            counter++;
        }
    }
    return counter;
}

bool check(int number, vector<int>& forbiddens) {
    for (int i = 0; i < forbiddens.size(); i++) {
        if (number == forbiddens[i]) {
            return false;
        }
    }
    return true;
}

void add_chosens(vector<int>& set, vector<int>& forbiddens, vector<int>& modded_set, vector <int> & final,int k) {
    if (k % 2 == 0) {
        for (int i = 0; i < modded_set.size(); i++) {
            if (modded_set[i] == 0) {
                final.push_back(set[i]);
                break;
            }
        }
        for (int i = 0; i < modded_set.size(); i++) {
            if (modded_set[i] == k / 2) {
                final.push_back(set[i]);
                break;
            }
        }
        for (int i = 0; i < modded_set.size(); i++) {
            if (check(modded_set[i], forbiddens) == true) {
                final.push_back(set[i]);
            }
        }
    }
    else {
        for (int i = 0; i < modded_set.size(); i++) {
            if (modded_set[i] == 0) {
                final.push_back(set[i]);
                break;
            }
        }
        for (int i = 0; i < modded_set.size(); i++) {
            if (modded_set.size() == k / 2) {
                final.push_back(set[i]);
                break;
            }
        }
        for (int i = 0; i < modded_set.size(); i++) {
            if (check(modded_set[i], forbiddens) == true) {
                final.push_back(set[i]);
            }
        }
    }
}

int nonDivisibleSubset(int k, vector<int> set) {
    int** combinations = nullptr;
    vector<int> modded_set;
    vector <int> forbiddens;
    vector <int> chosen_numbers;
    vector <int> final;
    int counter = 0;
    combinations = set_combination(combinations, k);
    set_mods(set, modded_set, k);
    choose_forbiddens(forbiddens, modded_set, combinations, k);
    add_chosens(set, forbiddens, modded_set, final,k);
    for (int i = 0; i <    final.size(); i++) {
        cout << final[i] << " ";
    }
    return final.size();
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string first_multiple_input_temp;
    getline(cin, first_multiple_input_temp);

    vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

    int n = stoi(first_multiple_input[0]);

    int k = stoi(first_multiple_input[1]);

    string s_temp_temp;
    getline(cin, s_temp_temp);

    vector<string> s_temp = split(rtrim(s_temp_temp));

    vector<int> s(n);

    for (int i = 0; i < n; i++) {
        int s_item = stoi(s_temp[i]);

        s[i] = s_item;
    }

    int result = nonDivisibleSubset(k, s);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
