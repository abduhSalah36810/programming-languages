#include<iostream>
#include<sstream>
#include<vector>
using namespace std;


vector<int> parseints(string str)
{
    stringstream s(str);
    vector<int> out ;
    char ch;
    int temp;
    while (s>>temp)
    {
        out.push_back(temp);
        s>>ch;

    }
    return out;
    

}



int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    string str;
    cin>>str;
    vector<int> v1 = parseints(str);
    for(int i = 0 ; i < v1.size() ; i++)
    {
        cout<<v1[i] << "\n" ;   

    }
    return 0;
}
 