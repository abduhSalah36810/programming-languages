#include<iostream>
#include<string>
using namespace std;

int main()
{
int t ;
cin>> t ;
string c = "codeforces";

for (int i = 0; i < t ; i++)
{
    char x ; 
    cin>> x ;
    cout << (c.find(x) != -1) ? "YES\n" : "NO\n";


}

}