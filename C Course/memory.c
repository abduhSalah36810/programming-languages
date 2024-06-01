#include <stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<string.h>
#include <stdbool.h>

typedef struct node{
    int number ;
    struct node *left ; 
    struct node *right;
}
node;

bool search (node *tree , int number);
void print_tree (node*root);
void free_tree (node*root);
int main (void)
{
    node *tree = NULL;

    // add a number to list
    node *n = malloc(sizeof(node));

    if (n==NULL)
    {
        return -1;
    }

    n->number = 2 ; 
    n->right = NULL;
    n->left  = NULL;
    tree = n;

    // add a number to list

    n = malloc(sizeof(node));
    if (n== NULL) {

    
        return 1 ; 
    }

    n->number = 1; 
    n->right = NULL;
    n->left = NULL;
    tree->left = n;
    
    // add number to list 
    n = malloc(sizeof(node));
    if (n==NULL){
        return 1;
    }

    n->number = 3;
    n->left=NULL;
    n-> right = NULL;
    tree -> right = n;


    // searching in a tree
    search(tree,2);
    // print tree
    print_tree(tree);
    // freeing tree
    free_tree(tree);
   
    
}

bool search(node *tree , int number)
{
    if (tree==NULL){
        return false;
    } else if( number < tree->number){
        return search(tree->left , number);
    } else if (number > tree->number){
        return search(tree->right,number);
    }else{
        return true;
    }
}
void print_tree (node*root)
{
    if (root== NULL)
    {
        return ;
    }
    print_tree(root->left);
    printf("%i\n" , root->number);
    print_tree(root->right);
}

void free_tree (node*root)
{
    if (root== NULL)
    {
        return ;
    }

    free_tree(root->left);
    free_tree(root->right);
    free(root);
}


