#include <stdio.h>
int main (void) {

    char grade ;
    printf("Ennter yout grade : " );
    scanf( " %c" , &grade ) ;
  
    switch (grade)
    {
    case 'A' :
       printf("you did great ");
        break;
    case 'B':
       printf("you did alright ");
        break;
    case 'C' :
       printf("you did well ");
        break;
    case 'D':
       printf("you did poorly");
        break;
    case 'F' :
       printf("you failed ");
        break;     
    default:
       printf("invalid Grade");
        break;
    }
      return 0 ;}

    
    
