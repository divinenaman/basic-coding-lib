#include<iostream>

using namespace std;

int min_jumps(int arr[],int n) {
	int max = ((n-1)*(n-1+1))/2;
	for(int i=0; i<n; i++) {
		max-=arr[i];
	}
	return abs(max);
}

int main() {
	int arr[] = {1,3,4,2,2};
	int j = min_jumps(arr,5);

	cout<<j<<endl; 
}