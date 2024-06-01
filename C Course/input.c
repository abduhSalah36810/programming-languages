#include<stdio.h> 
int main (void) {

    //in this tautorial we are gonna learn about inputs

   /* 
    int age ; 
    printf("what is your age : ");
    scanf("%d", &age);
    printf("your age is %d" , age); 
    */ 
  
    /*
    double gpa ; 
    printf("what is your gpa : ");
    scanf("%lf", &gpa);
    printf("your age is %f" , gpa);
    */
    
    // mad lib game
    char place[20];
    char someone[20];
    char cloth[20];
    printf("type in a place : ");
    fgets(place, 20 , stdin);
    printf("type in a someone : ");
    fgets(someone, 20 , stdin);
    printf("type in a cloth : ");
    fgets(cloth, 20 , stdin);
    printf("i went with my father to %s" , place);
    printf("we found %s there " , someone);
    printf("he was wearing %s" , cloth);

}
