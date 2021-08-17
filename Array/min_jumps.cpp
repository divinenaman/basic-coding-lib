#include<iostream>

using namespace std;

int min_jumps(int arr[],int n) {
	int jumps = 1,prev_pass=arr[0],forward_pass = arr[0];
	
	if(prev_pass==0) return -1;

	for(int i=1; i<n; i++) {
		
		if(i==n-1) break;

		prev_pass--;
		forward_pass--;
		forward_pass=max(arr[i],forward_pass);
		
		if(prev_pass==0) {
			prev_pass = forward_pass;
			jumps++;

			if(prev_pass==0) return -1;

			if(prev_pass+i >= n-1) break;
		}

	}
	return jumps;
}

int main() {
	int arr[] = {1,3,5,8,9,2,6,7,6,8,9};
	int j = min_jumps(arr,11);

	cout<<j<<endl; 
}