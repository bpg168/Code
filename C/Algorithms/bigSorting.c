#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct node{
	char String[1000000];
	long len;
	struct node *front;
	struct node *rear;
};

struct node *first;
int flag = 0;

void insert_new(struct node *pos, char* String, long len){
	struct node* temp = (struct node *)malloc(sizeof(struct node));
	if(flag == 0){
		// printf("chaing first\n");
		temp->front = pos;
		pos->rear = temp;
		temp->rear = NULL;
		first = temp;
	}
	else{
		temp->front = pos->front;
		temp->rear = pos;
		pos->front = temp;
	}
	strcpy(temp->String, String);
	temp->len = len;
}

struct node* pos_finder(struct node* first, char* String, long len){
	struct node* temp = first;
	long storedNum, stringNum;
	flag = 0;
	int runner = 0;
	first = (struct node *)malloc(sizeof(struct node));
	while(temp->len < len && temp->front != NULL){
		temp = temp->front;
		flag = 1; 
	}

	if(temp->len == len){
		while(temp->len == len){
			storedNum = atol(temp->String);
			stringNum = atol(String);
			if(storedNum < stringNum && temp->front != NULL){
				temp = temp->front;
				flag = 1;
			}
			else{
				// printf("%s\t%s", temp->String, temp->rear->String);
				temp = temp->rear;
				break;
			}
		}
	}

	// if(temp->len > len){
	// 	flag = 1;
	// }
	return temp;
}

void printer(struct node *first){
	printf("printing\n");
	while(first!=NULL){
		printf("%s\n", first->String);
		first = first->front;
		free(first->rear);
	}
}

int main(int argc, char** argv){
	struct node *temp;
	long n, i = 0, len;
	char String[1000000];
	char* null = '\0';
	first = (struct node *)malloc(sizeof(struct node));
	first->rear = NULL;
	first->front = NULL;
	
	scanf("%ld", &n);
	memset(String, 0, strlen(String));
	scanf("%s", String);
	strcpy(first->String, String);
	len = strlen(String);
	first->len = len;
	for(i = 1; i < n; i++){
		memset(String, 0, strlen(String));
		scanf("%s", String);
		len = strlen(String);
		temp = pos_finder(first, String, len);
		insert_new(temp, String, len);
	}
	printer(first);
}