#include<stdio.h>
#include<string.h>
#include<math.h>

int main(int argc, char* argv[]) {
  char* a = argv[1];
  char* b = argv[3];
  int lena = strlen(a), lenb = strlen(b), j = 0;
  for(j = 0; j < lena; j++) {
    if((int)a[j] > 57 || (int)a[j] < 48) {
      printf("You did not input integers!\n");
      return 0;
    }
  }
  j = 0;
  for(j= 0; j < lenb; j++) {
    if((int)b[j] > 57 || (int)b[j] < 48) {
      printf("You did not input integers!\n");
      return 0;
    }
  }
  if(Check(argc, argv)) {
    Calculate(argc, argv);
  }
  else {
    printf("Try again.\n");
    return 0;
  }
}

int Check(int len, char* args[]) {
  int i = 0;
  for(i; i < len; i++) {
    printf("argv[%d]: %s \n", i, args[i]);
  }
  if(len > 4) {
    printf("Too many arguments.\n");
    return 0;
  }
  if(len < 4) {
    printf("Too few arguments.\n");
    return 0;
  }
  if(strstr(args[1], ".") != NULL || strstr(args[3], ".") != NULL) {
    printf("Input is not an integer.\n");
    return 0;
  }
  return 1;
}

int Calculate(int len, char* args[]) {
  int a = atoi(args[1]), b = atoi(args[3]), c;
  if(strcmp(args[2], "x") == 0) {
    c = a * b;
    printf("%d\n", c);
    return c;
  }
  if(strcmp(args[2], "+") == 0) {
    c = a + b;
    printf("%d\n", c);
    return c;
  }
  if(strcmp(args[2], "-") == 0) {
    c = a - b;
    printf("%d\n", c);
    return c;
  }
  if(!b) { 
    printf("Cannot divide by zero.\n");
    return 0;
  }
  else {
    c = a / b;
    printf("%d\n", c); 
    return c;
  }
}

int Jstrlen(char* a) {
  int len = 0;
  while(a[len] != '\0')
    len++;
  return len;
}

void mystrcpy(char* source,  char* target) {
  int len = Jstrlen(target), i = 0;
  for(i; i < len + 1; i++)
    source[i] = target[i];
  len = Jstrlen(source);
  i = 0;
  for(i; i < len + 1; i++)
    printf("%c\n", source[i]);
}

void mystrcat(char* source, char* target) {
  int len = Jstrlen(target), i = 0, j = Jstrlen(source);
  for(i; i < len + 1; i++) {
    source[j] = target[i];
    j++;
  }
  i = 0;
  for(i; i < j; i++)
    printf("%c\n", source[i]);
}


