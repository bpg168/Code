/* 	Author 	-	Guruprasad Bhat
	date	- 	25-11-2017
	Time	- 	11.21
	Desc	-	Exercise 2
				Tim Mattson, Intel
*/

/* The "Hello World" program of parallel programming */
#include <stdio.h>
#include <omp.h>

int main(int argc, char ** argv){
	int i = 0;
	long STRIPS = 10;
	double STRIPWIDTH = 1 / (double)STRIPS;
	double midPoint, hieghtTotal = 0.0, hieght;

	
	double intialTime = omp_get_wtime();
	omp_set_num_threads(32);
	#pragma omp parallel for private(i) reduction(+ : hieghtTotal)
	for(i = 0; i < STRIPS; i++){
		midPoint = (i + 0.5) * STRIPWIDTH;
		hieght = 4 / (1 + midPoint * midPoint);
		hieghtTotal += hieght;
	}
	double totalTime = omp_get_wtime() - intialTime;
	double totalArea = STRIPWIDTH * hieghtTotal;
	printf("%0.10lf\t:\t%.10lf\n", totalArea, totalTime);
	return 0;
}