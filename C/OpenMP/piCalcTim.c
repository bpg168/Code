/* 	Author	-	Guruprasad Bhat
	Date 	-	25-11-2017
	Time	-	19:40
	Desc	-	Exercise 2
				Tim Mattson, Intel
*/

/* The "Hello World" program of parallel programming */
#include <stdio.h>
#include <omp.h>

#define NO_OF_STRIPS 	1000000
#define NO_OF_THREADS	8

int main(int argc, char **argv){
	double sum[NO_OF_THREADS], criticalSum = 0.0; int actualThreads = 0;
	double startTime, endTime, Pi = 0.0;
	double stripLength = 1.0 / (double)NO_OF_STRIPS;
	omp_set_num_threads(atoi(argv[0]));	
	startTime = omp_get_wtime();
	#pragma omp parallel
	{
		int id, numThreads;
		double midPoint, height;
		id = omp_get_thread_num();
		numThreads = omp_get_num_threads();
		sum[id] = 0.0;
		if(id == 0)
			actualThreads = numThreads;
		for(int i = id; i < NO_OF_STRIPS; i += numThreads){
			midPoint = (i + 0.5) * stripLength;
			height = 4.0 / (1.0 + midPoint * midPoint);
			sum[id] += height;
			#pragma omp critical
			{
				criticalSum += height; 
			}
		}
	}
	printf("%d\n", actualThreads);
	for (int i = 0; i < actualThreads; ++i)
	{
		Pi += sum[i];
	}
	endTime = omp_get_wtime();
	printf("%lf\t:%lf\n", Pi, endTime - startTime);
	printf("%lf\n", criticalSum);
	return 0;	
}