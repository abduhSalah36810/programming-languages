#include <stdio.h>
int main (void) {
    // an empty array
    char name[20];
    // an array of integers
    int numbers[] = {1,2,3,4,5};
    // modifying an element by its index
    numbers[0]  = 22;
    // accessing an element and printing in on terminal
    printf("%d" , numbers[0]);
}