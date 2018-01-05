#include <stdio.h>

int main(int argc, char** argv){
	printf("%d", '\0');
	int *testing = NULL;
	free(testing);
	return 0;
}