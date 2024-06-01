#include <stdio.h>

int linear_search (int arr[] , int size , int value );

int main (void)
{
  int num ;
  printf("give me a number to search for : ");
  scanf("%d" ,  &num);
  int arr1 [7] = {3,4,5,6,8,3,7};
  int index = linear_search(arr1 , 7 , num);
  if(index == -1) 
  {
     printf("not found");
  }else{
    printf("the number is at index : %d" , index);
  }

  return 0 ;
}
  
int linear_search (int arr[], int size , int value )
{
    int i ;
    for(i=0 ; i < size ; i++){
        if (arr[i] == value){
            return i;
        }
    }
    return -1;
}