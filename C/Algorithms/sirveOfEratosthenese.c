#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

#define NUM 100
int main(int argc, char** argv){
	//Variables
	int limit = sqrt(NUM);
	//Loop indeces
	int i = 0, j;
	//pointers
	int * NonPrimes = NULL;
	//Allocating memory to store NonPrimes
	NonPrimes = (int *)malloc(NUM * sizeof(int));
	//Clearing memory of NonPrimes
	memcpy(NonPrimes, &i , NUM*4);
	// printf("Checking memcpy\n");
	// for(i = 0; i < NUM; i++)
	// 	printf("%d\t", NonPrimes[i]);
	
	//Sieve of Eratosthenese Algorithm
	for(i = 2; i < limit; i++){
		printf("\nSieve for %d\n", i);
		for(j = i*i; j < NUM; j += i){
			printf("%d\t", j);
			NonPrimes[j] = -1;
		}
		printf("\n");
	}
	//Printing the result
	j = 0;
	printf("\n\n-----------------Prime Numbers---------------\n");
	for(i = 2; i < NUM; i++){
		if(NonPrimes[i] != -1){
			printf("%d\t", i);
			j++;
			if(j % 5 == 0)
				printf("\n");
		}
	}
	printf("\n---------------------------------------------\n");
}