#include<iostream>
#include<vector>
using namespace std;

void swap(int *a,int *b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

void sort012(int arr[],int n) {
	int low=0,high=n-1,mid=0,pivot=1;

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
	int a[] = {2,1,0,2,1,0,0,2,1,0};

	sort012(a,10);

	for(int i=0;i<10;i++) {
		cout<<a[i]<<" ";
	}
	cout<<endl;
}