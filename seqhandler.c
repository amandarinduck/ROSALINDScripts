#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void dnacount() {
	//upper limit for input sequence is 5 kb
	char DNA[5000];
	int A = 0;
	int T = 0;
	int C = 0;
	int G = 0;
	printf("Enter DNA sequence: \n");
	scanf("%s", DNA);

	for (int i = 0; i < strlen(DNA); i++){
		if (DNA[i] == 65 || DNA[i] == 97){
			A++;
		} else if (DNA[i] == 84 || DNA[i] == 116){
			T++;
		} else if (DNA[i] == 67 || DNA[i] == 99){
			C++;
		} else if (DNA[i] == 71 || DNA[i] == 103){
			G++;
		} else{
			printf("invalid character in sequence, please provide only ATCG\n");
			exit(1);
		}

	}
	printf("Sequence Length of %zu\n", strlen(DNA));
	printf("A's in sequence %d\n",A);
	printf("T's in sequence %d\n",T);
	printf("C's in sequence %d\n",C);
	printf("G's in sequence %d\n",G);
	return;

}

void GC(){
	char DNA[5000];
	int G = 0;
	int C = 0;
	printf("Enter DNA sequence: \n");
	scanf("%s", DNA);
	for (int i = 0; i < strlen(DNA); i++){
		if (DNA[i] == 67 || DNA[i] == 99){
			C++;
		} else if (DNA[i] == 71 || DNA[i] == 103){
			G++;

		} 
	}
	int GC = G + C;
	float GCcontent = (float)GC/strlen(DNA);
	printf("Total Sequence Length is %zu\n",strlen(DNA));
	printf("GC Content is %f\n",GCcontent);
	return;
}

int main(){
	GC();
}

