#include <stdio.h>

int main(){
//variable initiation, condition checking, increment
//this creates 8 lines
  for (int i = 0; i < 9 ; i++)
  {
//creates #s in each line
      for (int j = 0 ; j < i ; j++)
      {
      printf("#");
      }
  printf("\n");
  }
}
