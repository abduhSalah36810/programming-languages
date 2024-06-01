#include <stdio.h>

/*
if statments is what adds intlligence to our program.
*/


int max (int num1 , int num2 , int num3) 
{
    int resulte;
    if (num1>=num2 && num1>=num3){
        resulte = num1;
    } else if (num2>=num1 && num2>=num3) {
        resulte= num2;
    }else{
        resulte = num3;
    }
    return resulte;
}

int main(void) {
   printf("%d", max(1,2,3));
}
