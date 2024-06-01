#include <stdio.h>

/*
to craeat a function :
1- define the return statment type like(void, int, double, char ...)
2- define the name of the function . 
3- define the prameters . 
4- type in the code that does fuctions work .
5- call fucntion . 
*/

// note : if we want to define the functio after the int we need to add 
// frist the proto type wich is .. int cube(int number)
int cube(int number) {
    return number* number * number ;
}
int main(void) {
    printf("%d" , cube(3));
    return 0 ; 
}
