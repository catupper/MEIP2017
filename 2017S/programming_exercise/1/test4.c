#include<stdio.h>

int main(){
  int i, n, x;
  n = 10;
  x = 0;
  for(i = 1;i <= n;i++){
    x = x + i;
  }

  printf("x = %d\n", x);
  return 0;
}
