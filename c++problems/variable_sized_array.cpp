
#include <iostream>
#include<vector>
using namespace std ; 

int main() {
  int n, q ;
  cin >> n >> q;
  vector<vector<int>> a(n) ; 
  for (int i =0 ; i < n ; i++){
      int k_size ;
      cin>>k_size;
      
      vector<int> k(k_size); 
      for(int j = 0  ; j <k_size ; j++){
          cin>>k[j];
          }
      a[i] = k;
  }
  for(int z = 0 ; z < q ; z++){
      int c , b;
      cin>> c >>b ;
      cout<< a[c][b] << "\n";
  }

   
}




/*  
  






*/