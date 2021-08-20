#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

void next_permute(vector<int>& a) {
	int n = a.size();
	int f = n-2;    
	while(f>=0 && a[f+1] <= a[f]) f--;
	
	if(f>=0) {
		int i = n - 1;
		while(a[i] <= a[f]) i--;

		int temp = *(a.begin()+f);
		*(a.begin()+f) = *(a.begin()+i);
		*(a.begin()+i) = temp;
	}    
	
	int j = n - 1;
	f++;    
	while(f<j) {
		int temp = *(a.begin()+f);
		*(a.begin()+f) = *(a.begin()+j);
		*(a.begin()+j) = temp;
		f++;
		j--;
	}

	for(int i: a) cout<<i<<" ";
	cout<<endl;

}

int main() {
	vector<int> arr;
	int n,i=0,x;

	cin>>n;

	while(i<n){
		cin>>x;
		arr.push_back(x);
		i++;
	}

	next_permute(arr);
}