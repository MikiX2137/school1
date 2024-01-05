/*
Napisz program znajdujacy wyrazy palindromy w zdaniu wpisanym z klawiatury
(niezaleznie od tego, czy w zapisie uzyto malych czy wielkich liter). 
W programie zdefiniuj funkcje sprawdzajaca, czy wyraz jest palindromem.
*/

#include <iostream>
#include <string>
#include <cctype>

using namespace std;

bool Palindrom(string wyraz)
{
    int i = 0, j = wyraz.size()-1;
    bool p = true;

    while(p && i<j)
    {
        if(toupper(wyraz[i])==toupper(wyraz[j]))
        {
            i++;
            j--;
        }
        else
        {
            p = false;
        }
    }

    return p;
}

int main()
{
    int i;
    string wyraz, zdanie;
    cout << "Wpisz zdanie: ";
    getline(cin, zdanie);

    zdanie = zdanie + ' ';

    while(zdanie.size()>0)
    {
        i = zdanie.find(' ');
        if(i > 0)
        {
            wyraz = zdanie.substr(0, i);
            if(Palindrom(wyraz))
            {
                cout << wyraz << endl;
            }
        }
        zdanie.erase(0, i+1);
    }

    return 0;
}
