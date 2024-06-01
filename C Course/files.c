
#include <stdio.h> 
int main(void){
//   FILE * fpionter = fopen("friends.txt" , "a") ; 
//   FILE * fpionter = fopen("friends.txt" , "w") ; 
//   fprintf(fpionter, "\nmostafa : science" );
//   fclose(fpionter);
     char line[255];
     FILE * fpionter = fopen("friends.txt" , "r") ; 
     fgets(line , 255 , fpionter);
     printf("%s" , line);
}

