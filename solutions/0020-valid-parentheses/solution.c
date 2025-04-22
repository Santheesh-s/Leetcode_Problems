#include <stdio.h>
#include <string.h>
#include <stdbool.h>
char stack[10000];
int top = -1;

void push(char c) {
    stack[++top] = c;
}

void pop() {
    if (top >= 0) top--;
}

bool isValid(char* s) {
    top = -1;
    int l = strlen(s);

    for (int i = 0; i < l; i++) {
        if (s[i] == '{' || s[i] == '[' || s[i] == '(') {
            push(s[i]);            
        } else {
            if (top < 0) return false;

            if (s[i] == '}' && stack[top] == '{') {
                pop();
            } else if (s[i] == ']' && stack[top] == '[') {
                pop();
            } else if (s[i] == ')' && stack[top] == '(') {
                pop();
            } else {
                return false;
            }
        }
    }
    return top == -1;
}

