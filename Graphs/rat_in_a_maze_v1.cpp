#include<iostream>
#include<vector>
#include<list>
#include<map>
#include<utility>

using namespace std;

bool ifSafe(int a,int b,int n) {
	return a<n && b<n && a>-1 && b>-1;
}

void dfs_from_target(vector<vector<int>> a,int n,int s1,int s2, int d1,int d2,vector<vector<bool>> &visited,string path,vector<string> &paths) {
	if(!visited[s1][s2] && ifSafe(s1,s2,n)) {
		visited[s1][s2] = true;


		if(s1==d1 && s2==d2) {
			paths.push_back(path);
		}

		int l = s2 -1 ,r = s2 + 1,t = s1 - 1,b = s1 + 1;

		// down
		if(ifSafe(b,s2,n) && a[b][s2]==1) {
			dfs_from_target(a,n,b,s2,d1,d2,visited,path+'D',paths);
		}

		// left
		if(ifSafe(s1,l,n) && a[s1][l]==1) {
			dfs_from_target(a,n,s1,l,d1,d2,visited,path+'L',paths);
		}

		// right
		if(ifSafe(s1,r,n) && a[s1][r]==1) {
			dfs_from_target(a,n,s1,r,d1,d2,visited,path+'R',paths);
		}

		// up
		if(ifSafe(t,s2,n) && a[t][s2]==1) {
			dfs_from_target(a,n,t,s2,d1,d2,visited,path+'U',paths);
		}

		visited[s1][s2] = false;
	}
}

vector<string> paths_to_target(vector<vector<int>> a,int n,int s1,int s2, int d1,int d2){
	vector<string> paths;
	string path;
	vector<vector<bool>> visited(n,vector<bool>(n,false)); 
	dfs_from_target(a,n,s1,s2,d1,d2,visited,path,paths);
	return paths;
}


int main() {

	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif

	int n;
	cin>>n;
	int v = n*n;
	vector<vector<int>> a(n);
	
	for(int i = 0; i< n; i++) {
		for(int j = 0; j < n;j++) {
			int x;
			cin>>x;
			a[i].push_back(x);
		}
	}

	vector<string> paths = paths_to_target(a,n,0,0,n-1,n-1);
	
	for(string s: paths) {
		cout<<s<<endl;
	}
}



