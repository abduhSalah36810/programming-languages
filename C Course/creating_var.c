#include <stdio.h>
#include <string.h>



typedef struct
{
    string name[] ; 
    string number[];
}
contact;

int main (void) 
{
    contact person[1];

    person[0].name = "abdu";
    person[0].number = 2302312314131 ; 
    printf("hi %s" ,person[0].name);
}

