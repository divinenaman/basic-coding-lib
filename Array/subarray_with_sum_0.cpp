#include<bits/stdc++.h>
using namespace std;

// prefix sums

int sum_0(int a[],int n) {
	unordered_set<int> prefix_sums;
	int sum = 0, ifZero = 0;
	for(int i=0; i<n; i++) {
		sum+=a[i];
		if(sum==0 || prefix_sums.find(sum)!=prefix_sums.end()) {
			ifZero++;
		}
		prefix_sums.insert(sum);
	}

	return ifZero;
}

int main() {
	int a[] = {4,2,-3,1,6};

	cout<<sum_0(a,5)<<endl;
}