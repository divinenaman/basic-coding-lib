#include<iostream>
#include<vector>
using namespace std;

void swap(int *a,int *b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

void neg_sort(int arr[],int n) {
	int low=0,high=n-1,mid=0,pivot=0;

	while(mid<=high) {
		if(arr[mid] < pivot){
			swap(&arr[low],&arr[mid]);	
			low++;
			mid++;
		}
		else if(arr[mid] > pivot) {
			swap(&arr[high],&arr[mid]);	
			high--;	
		}
		else {
			mid++;
		}	
	}
}

int main() {
	int a[] = {-2,1,3,-2,1,-8,-1,2,-4,5};

	neg_sort(a,10);

	for(int i=0;i<10;i++) {
		cout<<a[i]<<" ";
	}
	cout<<endl;
}