#include<iostream>
#include<vector>
#include<climits>

using namespace std;

vector<int> union_array(int arr1[],int arr2[],int n,int m) {
	vector<int> union_arr;
	int i = 0, j = 0;
	while(i<n || j<m){
		int min = INT_MAX;
		if(i<n) {
			min = arr1[i]; 
		}
		if(j<m && arr2[j] < min) {
			min = arr2[j];
			j++;
		}else i++;

		while(i<n && arr1[i]==min) i++;
		while(j<m && arr2[j]==min) j++;

		union_arr.push_back(min);
	}

	return union_arr;
}

vector<int> intersect_array(int arr1[],int arr2[],int n,int m) {
	vector<int> intersec_arr;
	int i = 0, j = 0;
	while(i<n && j<m){
		int max = INT_MIN;
		if(i<n) {
			max = arr1[i]; 
		}
		if(j<m && arr2[j] > max) {
			max = arr2[j];
		}

		while(i<n && arr1[i]<max) i++;
		while(j<m && arr2[j]<max) j++;

		if(arr1[i]==arr2[j]){
			intersec_arr.push_back(arr1[i]);
			while(i<n && arr1[i]==max) i++;
			while(j<m && arr2[j]==max) j++;
		}	
	}

	return intersec_arr;
}

int main() {
	int a1[] = {1,2,3,5,6,7};
	int a2[] = {4,5,6,8,10};

	vector<int> ans1 = union_array(a1,a2,6,5);

	vector<int> ans2 = intersect_array(a1,a2,6,5);

	for(int i: ans1) cout<<i<<' ';
	cout<<endl;

	for(int i: ans2) cout<<i<<' ';
	cout<<endl;	
}