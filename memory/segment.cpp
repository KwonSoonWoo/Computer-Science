#include <iostream>

// CODE
int add(int a , int b){
  return a + b;
}

int subtract(int a, int b){
  return a - b;
}

// DATA
int global_x = 10;

int main(void){
  //STACK
  int local_x = 20;

  // HEAP
  int * heap_x = (int*)malloc(sizeof(int));
  *heap_x = 30;
  free(heap_x);


  return 0;
}
