/*
	Name	:	Dynamic memory allocation for a 2D array in C
	Author	:	bpg168
	Date	:	Nov, 30, 2017
	Time	:	7-32am
	Project	:	Testing
*/
#include <stdio.h>
#include <stdlib.h>

#define ROWS 10
#define COLUMNS 10

int main(int argc, char **argv){
	int** twoDArray, i, j;
//------------------Memory Allocation for 2D Array--------------------------------//
	twoDArray = (int **)malloc(ROWS * sizeof(int *)); //Allocate memory to ROWS number of pointers
	for(i = 0; i < ROWS; i++)
		//Allocate memory for each row, i.e. assign pointer to COLUMNS no. of blocks to each row
		twoDArray[i] = (int *)malloc(COLUMNS * sizeof(int));

//-------------------------Test the Array-----------------------------------------//
	//Populate the Array
	for(i = 0; i < ROWS; i++)
		for(j = 0; j < COLUMNS; j++)
			twoDArray[i][j] = rand()%100;

	//Print the Array
	for(i = 0; i < ROWS; i++){
		for(j = 0; j < COLUMNS; j++)
			printf("%d\t", twoDArray[i][j]);
		printf("\n");
	}
	return 0;
}