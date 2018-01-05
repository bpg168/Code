/* 	Author 	- 	Guruprasad Bhat
	Date	-	25-11-2017
	Time	-	8.25
	Desc	-	Exercise 1
				Tim Mattson, Intel
*/

#include <omp.h>
#include <stdio.h>

int main(int argc, char **argv){

	#pragma omp parallel 
	{
		int ID = omp_get_thread_num();
		printf("hello(%d)", ID);
		printf("world(%d)\n", ID);
	}
}