#include <stdio.h>
int main(void) {

// creating a two dimintional array
    int nums[4][3]  ={
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9},
            {10, 11, 12}
            
    };
// looping throw each element using a nested loop
   int i , j ;
   for (i = 0; i<4 ; i++){
     for ( j = 0; j < 3; j++)
        {
              printf("%d" , nums[i][j]);
        }
        printf("\n");
    }
 return 0;
}