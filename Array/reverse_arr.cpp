#include<iostream>
#include<vector>

using namespace std;

void reverse(int arr[],int l,int h) {
	if(l<h) {
		int temp = arr[l];
		arr[l] = arr[h];
		arr[h] = temp;
		reverse(arr,l+1,h-1);
	}
}

int main() {
	int n,i;
	cin>>n;
	int a[n];

	i=0;
	while(i<n) cin>>a[i++];

	reverse(a,0,n-1);

	for(int j: a) cout<<j<<" ";
	cout<<endl;	
}