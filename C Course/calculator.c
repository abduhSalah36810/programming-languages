#include <stdio.h>

int main (void ) {

    double num1;
    char operator;
    double num2;
    printf("Enter a number : ");
    scanf("%lf", &num1);
    printf("Enter an operator : ");
    scanf(" %c", &operator);
    printf("Enter another number : ");
    scanf("%lf", &num2);
    if (operator =='+'){
        printf("%f" , num1+num2);
    }else if (operator =='-'){
        printf("%f" , num1-num2);
    }else if(operator =='/'){
        printf("%f" , num1/num2);
    }else if (operator =='*'){
        printf("%f" , num1*num2);
    } else {
        printf("invalide operator");
    }
    
}