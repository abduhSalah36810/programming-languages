#include <stdio.h>

int binay_serach (int array1[], int number , int l , int r);

int main (void){
    int num ;
    printf("give me a number to search for : ");
    scanf("%d" ,  &num);
    int array[] = {1,2,3,4,5,6,7,8,9};
    int index = binay_serach(array ,num,0,9);
    if(index == -1) 
    {
      printf("not found");
    }else{
    printf("the number is at index : %d" , index);
  }
}

int binay_serach (int array1[], int number , int l , int r){
    int mid = l+ (r-l) / 2 ; 

    if (l>r){
        return -1 ;
    }
    if (array1[mid]==number){
        return mid;
    } else if (array1[mid]>number){
        return binay_serach(array1,number, l , mid-1);
    }else if (array1[mid]<number){
        return binay_serach(array1,number,mid+1,r);
    }

}