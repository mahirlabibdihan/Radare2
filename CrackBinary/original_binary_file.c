
#include <stdio.h>
#include <string.h>

void rot13 (char *s) {
    if (s == NULL)
        return;
    int i;
    for (i = 0; s[i]; i++) {
        if (s[i] >= 'a' && s[i] <= 'm') { s[i] += 13; continue; }
        if (s[i] >= 'A' && s[i] <= 'M') { s[i] += 13; continue; }
        if (s[i] >= 'n' && s[i] <= 'z') { s[i] -= 13; continue; }
        if (s[i] >= 'N' && s[i] <= 'Z') { s[i] -= 13; continue; }
    }
}

int beet(char *name)
{
    char buf[128];
    strcpy(buf, name);
    char string[] = "67xSojib";
    rot13(string);

    return !strcmp(buf, string);
}

int main(int argc, char *argv[])
{
    printf("\n CSE-406 COMPUTER SECURITY \n");
    printf("The password is 67xSojib\n");
    if (argc >= 2 && beet(argv[1]))
    {
        printf("Success!\n\n");
    }
    else
        printf("Wrong password\n\n");

    return 0;
}