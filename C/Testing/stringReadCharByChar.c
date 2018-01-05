/*
	Name	:	Reading a string character by character in C
	Author	:	bpg168
	Date	:	Nov, 30, 2017
	Time	:	7-02am
	Project	:	Testing
*/
#include <stdio.h>

int main(int argc, char** argv){
	char myString[20], ch;
	int i = 0;
	printf("Enter a string for testing\n");
	scanf("%c", &myString[i++]); //Read each character and store them in i th pos, and increment i
	//String ends with a new-line character
	while(myString[i-1] != '\n'){
		scanf("%c", &myString[i++]);
	}
	//Overwrite the new-line character with null character to make it a proper string
	myString[i-1] = '\0';
	printf("%s\n", myString);
	return 0;
}