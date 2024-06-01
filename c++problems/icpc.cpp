    #include<iostream>
    #include<string>
    #include<iomanip>
    #include<cmath>
    #include <cctype>


    using namespace std;

int main ()
{
     
  int resulte = 0 , number , avg  , arr[5] , max ;
    
   for (int i = 0; i < 5; i++)
   {
    cout<<"enter till it stops : " ;
    cin>> number ;
    arr[i]  = number ; 
    resulte += arr[i]; 
    avg = resulte/5;
    max = arr[0];
    if(max < arr[i])
    {
        max = arr[i];
    }
   }
    cout<<"The sum of all the numbers is : " <<resulte <<endl ; 
    cout<<"The avrage is : "<<avg<<endl;
    cout<<"The max number is : "<< max;          
    }