void counterspell(Spell *spell) {
 if (dynamic_cast<Waterbolt*>(spell) != nullptr) {
        Waterbolt* ptr = dynamic_cast<Waterbolt*>(spell);
        ptr->revealWaterpower();
    }
    else if (dynamic_cast<Thunderstorm*>(spell) != nullptr) {
        Thunderstorm* ptr = dynamic_cast<Thunderstorm*>(spell);
        ptr->revealThunderpower();
    }
    else if (dynamic_cast<Frostbite*>(spell) != nullptr) {
        Frostbite* ptr = dynamic_cast<Frostbite*>(spell);
        ptr->revealFrostpower();
    }
    else if (dynamic_cast<Fireball*>(spell) != nullptr) {
        Fireball* ptr = dynamic_cast<Fireball*>(spell);
        ptr->revealFirepower();
    }
    else {
        string X = spell->revealScrollName();
        string Y = SpellJournal::read();
        int m = X.size();
        int n = Y.size();
        int L[m+1][n+1];
        int i, j;
        for (i = 0; i <= m; i++) {
            for (j = 0; j <= n; j++) {
                if (i == 0 || j == 0)
                    L[i][j] = 0; 
                else if (X[i-1] == Y[j-1])
                    L[i][j] = L[i-1][j-1] + 1;
                else
                    L[i][j] = max(L[i-1][j], L[i][j-1]);
            }
        }
        cout << L[m][n] << endl;
    }
}