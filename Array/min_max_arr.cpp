#include<iostream>
#include<vector>

using namespace std;

void min_max(int arr[],int n) {
	int min1 = arr[0],min2 = arr[n-1],max1 = arr[0],max2 = arr[n-1];
	for(int i=0; i<(n/2+n%2); i++){
		if(arr[i]<min1) min1=arr[i];
		if(arr[n-1-i]<min2) min2=arr[n-1-i];
		if(arr[i]>max1) max1=arr[i];
		if(arr[n-1-i]>max2) max2=arr[n-1-i];
	}

	cout<<"Max: "<<max(max2,max1)<<endl;
	cout<<"Min: "<<min(min2,min1)<<endl;
}

int main() {
	int n,i;
	cin>>n;
	int a[n];

	i=0;
	while(i<n) cin>>a[i++];

	min_max(a,n);
}