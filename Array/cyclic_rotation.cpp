#include<iostream>
#include<vector>

using namespace std;

void swap(int *a,int *b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

void rotate(int arr[],int n,int step) {
	int i = 0, j = n-step;

	while(i<j) {
		swap(&arr[i],&arr[j]);
		i++;

		if(j<n-1) j++;
		else j = n-step;
	}
}

int main() {
	int arr[] = {2,4,5,1,9};
	int n = 5;
	rotate(arr,n,4);

	for(int i=0; i<n; i++) cout<<arr[i]<<' ';
	cout<<endl;
}