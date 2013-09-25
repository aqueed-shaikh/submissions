#include <stdlib.h>
#include <stdio.h>

long long int fibb(int n) {
	int now = 0, next = 1, a;
	while(--n>0){
		a = now + next;
		now = next;
		next = a;
		}
		return fnow;	
}

int main() {
  int ans = 0;
  int i = 0;
  int current = 0;
  while (current < 4000000)
  {
  if ((fib(i)) % 2 == 0)
  {
  ans = ans + fib(i);
  }
  i = i + 1;
  current = fib(i);
  }
}
