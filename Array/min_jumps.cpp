#include<iostream>

using namespace std;

int min_jumps(int arr[],int n) {
	int jumps = 1,prev_pass=arr[0],forward_pass = 0;
	
	if(prev_pass==0) return -1;

	for(int i=1; i<n; i++) {
		
		if(i==n) break;

		prev_pass--;
		if(forward_pass>prev_pass) forward_pass--;
		forward_pass=max(arr[i],forward_pass);
		
		if(prev_pass==0) {
			if(forward_pass>0){ 
				prev_pass = forward_pass;
				forward_pass=max(arr[i],forward_pass);
				jumps++;
			}
			else {
				jumps = -1;
				break;
			}
		}

	}
	return jumps;
}

int main() {
	int arr[] = {3,0,0,0,0,0};
	int j = min_jumps(arr,6);

	cout<<j<<endl; 
}