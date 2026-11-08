#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    char str1[] = "Hello";
    char str2[] = "World";
    
    // Allocating memory without space for null terminator '\0'
    char *result = (char *)malloc(strlen(str1) + strlen(str2));
    
    strcpy(result, str1);
    strcat(result, str2);
    
    printf("Result: %s\n", result);
    printf("Length: %lu\n", sizeof(result));
    
    return 0;
}
