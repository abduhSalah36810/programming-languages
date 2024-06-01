// it's where our variables are stores in RAM while ecxcuting 
// the program .  

#include <stdio.h>

int main (void) {

    int age = 18 ;
     // make a pointer 
    int * pAge = &age;
    double gpa= 3.5;
     // make a pointer 
    double* pGpa = &gpa;
    char letter = 'w';
     // make a pointer 
    char * pLetter = &letter;
    // accessing the memory address . 
    printf("age : %p \ngpa : %p \nletter : %p " , &age , &gpa , &letter);
    // dereferencig the memory address 
    printf("%d", *&age);
}