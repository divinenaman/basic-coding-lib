#include<iostream>
#include<vector>
#include<list>
#include<queue>
#include<map>

using namespace std;

void bfs(map<int,list<int>> adj, int src) {
	queue<int> q;
	map<int,bool> visited;
	q.push(src);

	while(!q.empty()) {
		int node = q.front();
		q.pop();
		cout<<node<<" ";
		for(auto a: adj[node]) {
			if(!visited[a]) {
				q.push(a);
				visited[a] = true;
			}
		}
	}

	cout<<endl;
}
	
int main() {
	map<int,list<int>> adj;

	adj[0].push_back(1);
	adj[0].push_back(2);
	adj[0].push_back(3);
	adj[2].push_back(4);

	bfs(adj,0);
}