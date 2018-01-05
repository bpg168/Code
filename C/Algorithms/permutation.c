/*
	This program finds all the permutations of a given 
	string using a recursive approach.

	Author : Guruprasad Bhat
	Date : 17/12/2017
	Time : 7:31
*/
#include <stdio.h>
#include <string.h>

void permuteRec(int, int, char*);
void swapChar(int, int, char*);

int main(int argc, char const *argv[])
{
	char input[20];
	printf("Enter a string (max length 20)\n");
	scanf("%s", input);
	permuteRec(0, strlen(input),input);
	return 0;
}

void swapChar(int x, int y, char* input){
	char temp;
	temp = input[x];
	input[x] = input[y];
	input[y] = temp;
	printf("%s\n", input);
}

void permuteRec(int l, int r, char* input){
	if(l == r)
		return;
	for(int i = l; i < r; i++){
		swapChar(input + i, input + l, input);
		permuteRec(l++, r, input);
		swapChar(input + l, input + i, input);
	}
}