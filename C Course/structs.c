#include <stdio.h>
#include <string.h>


struct friend {

    char name[20];
    int age;
    double hight ;
    double wieght;
};

int main (void) {

    struct friend friend1 ;
    strcpy(friend1.name, "Abdo atef");
    friend1.age = 18;
    friend1.hight = 180.0;
    friend1.wieght = 98.2;
    printf("%s is %d years old , %f cm and %f kilos" , friend1.name ,friend1.age ,friend1.hight,friend1.wieght);

    return 0 ;
}