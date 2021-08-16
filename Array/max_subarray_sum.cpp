#include<iostream>
#include<vector>

using namespace std;

// int max_sum(int arr[],int l,int h,int sum) {
// 	if(l<=h) {
// 		if(arr[l]>=0) {
// 			sum+=arr[l];
// 			return max_sum(arr,l+1,h,sum);
// 		}else {
// 			int inter_mediate = max_sum(arr,l+1,h,0);
// 			cout<<"inter"<<inter_mediate<<endl;

			
// 				sum+=arr[l]; 
// 				return max(sum,max(sum+inter_mediate,inter_mediate));
// 		}
// 	}
// 	else {
// 		if(arr[h-1]<0) return arr[h-1];
// 		return sum;
// 	}
// }

int max_sum(int arr[],int n) {
	int max_now = 0, max = 0;

	for(int i=0; i<n; i++) {
		int a = arr[i];

		max_now+=arr[i];

		if(max_now<0) max_now = 0;
		if(max_now>max) max = max_now;
	}

	return max;
}

int main() {
	int arr[] = {-2,-3,4,-1,-2,1,5,-3};
	int sum = max_sum(arr,8);
	cout<<sum<<endl;
}