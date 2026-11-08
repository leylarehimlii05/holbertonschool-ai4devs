#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    char str1[] = "Hello";
    char str2[] = "World";
    
    // Allocate memory with +1 byte for null terminator '\0'
    char *result = (char *)malloc(strlen(str1) + strlen(str2) + 1);
    if (result == NULL) {
        return 1;
    }
    
    strcpy(result, str1);
    strcat(result, str2);
    
    printf("Result string output: %s\n", result);
    printf("Allocated string length: %lu\n", strlen(result));
    
    free(result);
    return 0;
}
