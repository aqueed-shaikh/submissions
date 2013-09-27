#strlen()#
	*library:* string.h
	*usage:* strlen(char *s)
	*returns:* an integer representing the length of s
	*note:* if s does not end with a null, it will keep going until a null is found in memory (or a seg fault happens)
	*example:* char s[] = "abc";
		 strlen(s);
		 > 3


#strcmp()#
	*library:* string.h
	*usage:* strcmp(char *s1, char *s2)
	*returns:* strcmp() returns an integer greater than, equal to, or less than 0, according as the string s1 is greater than, equal to, or less than the string s2.  The comparison is done using unsigned characters, so that `\200' is greater than `\0'.
	*note:* strings should be null terminated
	*example:* char s1[] = "aaa";
		 char s2[] = "bbb";
		 strcmp(s1, s2);
		 > -1

#strcpy()#
	library: string.h
	usage: strcpy(char *dest, char *src)
	returns: dest, having copied src to dest
	note: strings should be null terminated
	example: char chararray[];
		 strncpy(chararray, "abc");
		 > abc

#strncpy()#
	*library:* string.h
	*usage:* strncpy(char *restrict s1, const char *restrict s2, size_t n)
	*returns:* s1
	*note:* copies n characters of s2 to s1. null terminates if there's more space in the array.
	*example:*
	 The following sets chararray to ``abc\0\0\0'':

           char chararray[6];

           strncpy(chararray, "abc", sizeof(chararray));

	 The following sets chararray to ``abcdef'':

           char chararray[6];

           strncpy(chararray, "abcdefgh", sizeof(chararray));

#strcat()#
	*library:* string.h
	*usage:* strcat(char *restrict s1, const char *restrict s2)
	*returns:* s1, having appended a copy of null terminated s2 to null terminated s1
	*note:* s1 must have enough space to hold the result
	*example:* char s1[15] = "abcde";
		   strcat(s1, "fgh");
		   > "abcdefgh" // null terminated

#strncat()#
	*library:* string.h
	*usage:* strncat(char *restrict s1, const char *restrict s2, size_t n)
	*returns:* s1, having appended a copy of not more than n characters of s2 to s1
	*note:* adds terminating null
	*example:* char s1[15] = "abcde";
		   strncat(s1, "fgh", 2);
		   > "abcdefg" // null terminated

