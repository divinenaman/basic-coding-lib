#include<iostream>
#include<vector>
#include<queue>
#include<map>
#include<list>

using namespace std;

template<typename T>
class Graph{
	private:
		map<T,list<pair<T,int>>> adjlist;

	public:
		void addEdge(T u,T v,int dist,bool directed = 0) {
			adjlist[u].push_back(make_pair(v,dist));
			if(!directed) {
				adjlist[v].push_back(make_pair(u,dist));
			}
		}

		void print_adj() {
			for(auto node: adjlist) {
				for(auto adj_node: node.second) {
					cout<<"("<<node.first<<","<<adj_node.first<<")"<<"->"<<adj_node.second<<"\t";
				}
				cout<<endl;
			}
		}

		void bfs(T src) {
			map<T,bool> visited;
			queue<T> q;
			q.push(src);

			while(!q.empty()) {
				T node = q.front();
				q.pop();
				for(auto a: adjlist[node]) {
					if(!visited[a.first]){
						q.push(a.first);
						visited[a.first] = true;
						cout<<node<<"->"<<a.first<<endl;
					}
				}
			}
		}

		void dfs(T src) {
			map<T,bool> visited;
			dfs_recur(src,visited);
		}

		void dfs_recur(T src,map<T,bool> &visited) {
			visited[src] = true;
			for(auto a: adjlist[src]) {
				if(!visited[a.first]) {
					cout<<src<<"->"<<a.first<<endl;
					dfs_recur(a.first,visited);
				}
			}
		}		
};

int main() {
	Graph<int> g = Graph<int>();
	g.addEdge(0,1,4,0);
	g.addEdge(0,7,8,0);
	g.addEdge(1,7,11,0);
	g.addEdge(1,2,8,0);
	g.addEdge(7,8,7,0);
	g.addEdge(2,8,2,0);
	g.addEdge(8,6,6,0);
	g.addEdge(2,5,4,0);
	g.addEdge(6,5,2,0);
	g.addEdge(2,3,7,0);
	g.addEdge(3,3,14,0);
	g.addEdge(3,4,9,0);
	g.addEdge(5,4,10,0);
	g.addEdge(7,6,1,0);

	g.print_adj();

	g.bfs(0);

	cout<<endl;
	
	g.dfs(0);
}