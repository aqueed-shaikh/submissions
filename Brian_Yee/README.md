strlen
library: string.h
usage: strlen(char*s)
returns: the length of s in the form of an integer
issues: If there is not a null value in s, then strlen will keep running.
example: char s[] = "abc"
	 (strlen s) ==> 3
----------
strcmp
library: string.h
usage: strcmp(char*s1, char*s2)
returns: an integer less than, equal to, or greater than zero as the values in s1 and s2 are compared.
issues: 
example: char s1[] = "12345"
	 char s2[] = "54321"
	 strcmp(s1,s2) ==> -4
----------
strcpy
library: string.h
usage: strcpy(char*dest, char*src)
returns: a pointer to the destination array, which contains a copy of the source array.
issues: the destination array must be large enough to receive a copy of the source array.
example: char s1[] = "12345"
	 char s2[5]
	 strcpy(s2, s1) ==> pointer value to s2, which now has "12345"
----------
strncpy
library: string.h
usage: strncpy(char*dest, char*src, size_t n);
returns: a pointer to the destination array, which contains at most n bytes of the source array.
issues: if there is no null byte in the first n bytes of the source array, then the string in the destination array will not be null-terminated.
example: char s1[] = "12345"
	 char s2[4]
	 strncpy(s2,s1,3) ==> pointer value to s2 which now has "1234"
----------
strcat
library: string.h
usage: strcat(char*dest, char*src)
returns: a pointer to the destination array, which now has the string in the source array appended to it.
issues: the destination array must have enough room to fit the source array.
example: char s1[] = "67890"
	 char s2[10] = "12345"
	 strcat(s2,s1) ==> pointer value to s2, which now has "1234567890"
----------
strncat
library: string.h
usage: strncat(char*dest, char*src, size_t n)
returns: a pointer to the destination array, which now has at most n bytes of the source array appended to it.
issues: the size of the destination array must be able to hold n+1 more bytes. When the source array string is appended, a null byte is also included.
example: char s1[] = "67890"
	 char s2[9] = "12345"
	 strncat(s2,s1,3) ==> pointer value to s2, which now has "12345678"