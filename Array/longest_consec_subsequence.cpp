#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int long_subseq(int a[],int n) {
	unordered_map<int,int> seq;
	int maxx = 0;
	for(int i=0;i<n;i++	) {
		if(seq.find(a[i]) == seq.end()) {
			if(seq.find(a[i]-1) != seq.end()) {
				seq[a[i]-1]++;
				seq[a[i]]=seq[a[i]-1];
			}else seq[a[i]] = 1;

			maxx = max(maxx,seq[a[i]]);

			if(seq.find(a[i]+1) != seq.end()) {
				seq[a[i]]+=seq[a[i]+1];
				seq[a[i]+1] = seq[a[i]];

				maxx = max(maxx,seq[a[i]]);
			}
		}
	}

	return maxx; 
}

int main() {
	int n,i=0,x;
	cin>>n;
	int a[n];
	while(i<n) {
		cin>>x;
		a[i++] = x;
	}

	int len = long_subseq(a,n);

	cout<<len<<endl;
}