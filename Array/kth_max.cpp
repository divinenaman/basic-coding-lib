#include<iostream>
#include<vector>

using namespace std;

int partition(int arr[],int l,int h) {
	int x = arr[h],i=l;
	for(int j=l; j<=h-1 ;j++){
		if(arr[j] < x) {
			int temp = arr[j];
			arr[j] = arr[i];
			arr[i] = temp;
			i++;
		}
	}
	int temp = arr[i];
	arr[h] = temp;		
	arr[i] = x;

	return i;
}

int quicksort(int arr[],int l,int h,int k) {
	if(l<=h){
		int pivot = partition(arr,l,h);
		if(pivot == k-1) return arr[pivot];
		else if(pivot > k-1) return quicksort(arr,l,pivot-1,k);
		return quicksort(arr,pivot+1,h,k);
	}

	return -1;
}

int main() {
	int a[] = {1,3,2,0,7};
	int z = quicksort(a,0,4,4);
	for(int i: a) {
		cout<<i<<" ";
	}
	cout<<endl<<z<<endl;
}