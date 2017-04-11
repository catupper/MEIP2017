#include<stdio.h>

int sum(int n){
  int i, x;
  x = 0;
  for(i = 1;i <= n;i++){
    x = x + i;
  }
  return x;
}

int main(){
  int n, x;
  scanf("%d%", &n);
  x = sum(n);
  printf("x=%d\n",x);
  return 0;
}
