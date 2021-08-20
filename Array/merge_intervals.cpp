#include<iostream>
#include<vector>
#include<utility>
#include<algorithm>

using namespace std;

bool comparator(pair<int,int> a,pair<int,int> b) {
	if(a.first==b.first) {
		return a.second > b.second;
	}

	return a.first < b.first;
}

vector<pair<int,int>> merge_intervals(vector<pair<int,int>> a) {
	int n = a.size();
	vector<pair<int,int>> intervals;

	// sort by ascending start time, descending end
	sort(a.begin(),a.end(),comparator);

	for(pair<int,int> i: a) {
		int size = intervals.size();

		if(size==0) intervals.push_back(i);

		else {
			pair<int,int> prev_pair = intervals[size-1];

			if(prev_pair.second >= i.first){
				intervals[size-1] = make_pair(prev_pair.first,max(prev_pair.second,i.second));
			}

			else intervals.push_back(i);
		}	
	}

	return intervals;
}

int main() {
	vector<pair<int,int>> arr;

	int x,y,n,i=0;

	cin>>n;
	while(i<n) {
		cin>>x;
		cin>>y;
		arr.push_back(make_pair(x,y));
		i++;
	}

	vector<pair<int,int>> ans = merge_intervals(arr);

	for(pair<int,int> i: ans) {
		cout<<i.first<<" "<<i.second<<endl;
	}
}