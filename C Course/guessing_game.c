#include <stdio.h>

int main(void) {

  //guessing game

 int secretnum = 3;
 int guesslimit = 3;
 int guess; 
 int guesscount = 0;
 int outofguesses = 0; 


  while(guess!=secretnum && outofguesses==0 ){
    if (guesscount<guesslimit){
       printf(" guess a fucking number : ") ; 
       scanf("%d", &guess);
       guesscount++;
   } else {
        outofguesses = 1;  }  
  }
  if(outofguesses==1){
       printf("out of guesses");        
  }else {
       printf(" fucking winner");}
     
}        