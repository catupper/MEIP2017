#include<stdio.h>

int sq_sum(int n){
  int ans, i;

  ans = 0;
  for(i = 1;i <= n;i++){
    ans = ans + i*i;
  }

  return ans;
}

int main(){
  int n;
  scanf("%d", &n);
  printf("%d\n", sq_sum(n));
  return 0;
}
