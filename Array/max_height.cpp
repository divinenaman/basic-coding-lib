#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int max_diff(int arr[],int n,int k) {
	sort(arr,arr+n);	
	int max_ele = arr[n-1], min_ele = arr[0];
	int res = max_ele - min_ele;
	for(int i=0;i<n;i++) {
		min_ele = min(arr[0]+k,arr[i]-k);
		max_ele = min(arr[n-1]-k,arr[i]+k);
		res = min(res,max_ele-min_ele);
	}
	return res;
}

int main() {
	int a[] = {1,6,4,2,8,5,2,3};
	int res = max_diff(a,8,2);
	cout<<res<<endl;
}