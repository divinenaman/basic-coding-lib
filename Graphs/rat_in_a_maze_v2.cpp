#include<iostream>
#include<vector>
#include<list>
#include<map>
#include<utility>

using namespace std;

void dfs_from_target(map<int,list<pair<int,char>>> adj,int src,int dest,vector<bool> &visited,string path,vector<string> &paths) {
	if(!visited[src]) {
		visited[src] = true;
		for(pair<int,char> node: adj[src]) {
			string temp = path + node.second;
			if(node.first == dest) {
				paths.push_back(temp);
			} else {
				dfs_from_target(adj,node.first,dest,visited,temp,paths);
			}
		}
		visited[src] = false;
	}
}

vector<string> paths_to_target(map<int,list<pair<int,char>>> adj,int start,int dest,int v){
	vector<string> paths;
	string path;
	vector<bool> visited(v,false); 
	dfs_from_target(adj,start,dest,visited,path,paths);
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
	map<int,list<pair<int,char>>> adj;
	for(int i = 0; i< n; i++) {
		for(int j = 0; j < n;j++) {
			int x;
			cin>>x;
			a[i].push_back(x);
		}
	}

	// other approach but TLE
	for(int i = 0; i< n; i++) {
		for(int j = 0; j < n;j++) {
			int l = j -1 ,r = j + 1,t = i - 1,b = i + 1;

			if(l>=0 && a[i][l]==1) adj[j+i*n].push_back(make_pair(l+i*n,'L'));
			if(r<n && a[i][r]==1) adj[j+i*n].push_back(make_pair(r+i*n,'R'));
			if(t>=0 && a[t][j]==1) adj[j+i*n].push_back(make_pair(j+t*n,'U'));
			if(b<n && a[b][j]==1) adj[j+i*n].push_back(make_pair(j+b*n,'D'));  
		}
	}

	for(auto it = adj.begin(); it!=adj.end(); it++) {
		cout<<it->first<<": ";
		for(pair<int,char> i: it->second) {
			cout<<"("<<i.first<<","<<i.second<<")";
		}
		cout<<endl;
	}
	cout<<endl<<endl;

	vector<string> paths = paths_to_target(adj,0,(n-1+(n-1)*n),v);
	
	for(string s: paths) {
		cout<<s<<endl;
	}
}



