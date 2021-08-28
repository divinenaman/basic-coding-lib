#include<iostream>
#include<list>
#include<vector>
#include<map>

using namespace std;

bool cycle_dfs(map<int,list<int>> &adj, vector<bool> visited,vector<bool> recur,int src) {
	if(!visited[src]) {
		visited[src] = true;
		recur[src] = true;
		for(int node: adj[src]) {
			if(!visited[node] && cycle_dfs(adj,visited,recur,node)) {
				return true;
			}else if(recur[node]) {
				return true;
			}
		}
	}
	recur[src] = false;
	return false;
}

void detect_cycle_directed(map<int,list<int>> &adj,int src,int v) {
	vector<bool> visited;
	vector<bool> recur_stack;
	for(int i = 0; i < v; i++) {
		visited.push_back(false);
		recur_stack.push_back(false);
	}
	bool z = cycle_dfs(adj,visited,recur_stack,src);
	cout<<z<<endl;
}


int main() {
	map<int,list<int>> adj;
	int n,v,x,y;
	cin>>v>>n;
	while(n--) {
		 cin>>x>>y;
		 adj[x].push_back(y);
	}

	detect_cycle_directed(adj,0,v);
}