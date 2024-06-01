


    #include<iostream>
    #include<string>
    #include<iomanip>
    #include<cmath>
     #include <cctype>


using namespace std;



int main () { 
    int num,countp=0,countn=0, countz=0;
    int num[i];
     for (int i = 0; i < num; i++)
     {
       cin>>num[i];
       if (num[i]>0)
       {
        countp++;
       }
       else if (num[i]<0)
       {
        countn++;
       }
       if (num[i]=0)
       {
        countz++;
       }
     }
     cout<<"The number of positive elements= "<<countp<<endl;
     cout<<"The number of negative elements= "<<countn<<endl;
     cout<<"The number of zeroes= "<<countz<<endl;
}