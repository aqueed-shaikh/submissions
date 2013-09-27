strlen
    library: string.h
    usage: strlen(char *s)
    returns: an integer representing the length of s
    issues: If s does not end with null, it will keep going until a null is found in memory (or a set fault occurs).
    example: char s[] = "abc"
            (strlen s) ==> 3

strcmp
    library: stdio.h
    usage: strcmp(char *string1, char *string2)
    returns: an integer (>0 if string1's length > string2's length, 0 if the strings are equal length, <0 if string1's length is shorter than string2's)
    issues: If a string does not end with null, it will keep going until a null is found in memory (or a set fault occurs)
    example: char s[] = "abc", char s2[] = "abcd"
            strcmp(s, s2) ==> int > 0


strcpy
    library: string.h
    usage: strcpy(char *dest, const char *src)
    returns: *dest with a copy of #src
    issues: If a string does not end with null, it will keep going until a null is found in memory (or a set fault occurs)
    example: strcpy(dest, src); returns dest containing src


strncpy
    library: string.h
    usage: strncpy(char *dest, const char *src, size_t n)
    returns: *dest containing a copy of the string *src up to n
    issues:
    example:strcpy(src, "This is tutorialspoint.com");
            strncpy(dest, src, 10);
            returns "This is tu"

strcat
    library: string.h
    usage: strcat(char *dest, const char *src)
    returns: Returns a pointer to the resulting string dest of the 2 strings concatnated 
    issues: src is appended so dest must be big enough to add the string
    example:strcpy(src,  "This is source");
            strcpy(dest, "This is destination");
            strcat(dest, src);
            Returns "This is destinationThis is source"


strncat
    library: string.h
    usage: strncat(char *dest, const char *src, size_t n)
    returns: n characters from src appended to dest (returns a pointer to dest)
    issues: src is appended so dest must be big enough to add the string
    example: 
    strcpy(src,  "This is source");
    strcpy(dest, "This is destination");
    strncat(dest, src, 15);
    Returns "This is destinationThis is source"