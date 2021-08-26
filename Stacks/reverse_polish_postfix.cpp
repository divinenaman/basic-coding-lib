#include<iostream>
#include<stack>
#include<vector>
#include<string>
#include<map>
#include<cctype>

using namespace std;

vector<char> get_postfix(string exp) {
	map<char,int> ope_priority;
	ope_priority['+'] = 0;
	ope_priority['-'] = 0;
	ope_priority['*'] = 1;
	ope_priority['/'] = 1;
	ope_priority['^'] = 2;

	vector<char> postfix;	
	stack<char> ope;
	for(char s: exp) {
		if(isdigit(s)) {
			postfix.push_back(s);
		}
		else {
			switch(s){
				case '+':
				case '-':
				case '*':
				case '/':
				case '^':
					if(ope.empty()) ope.push(s);
					else {
						while(!ope.empty() && ope_priority[s]<=ope_priority[ope.top()] && ope.top()!='('){
							postfix.push_back(ope.top());
							ope.pop();
						}
						ope.push(s);
					}
					break;
				case '(':
					ope.push(s);
					break;	
				case ')':	
					while(ope.top()!='('){
						postfix.push_back(ope.top());
						ope.pop();
					}
					ope.pop();
					break;
			}
		}
	}
	while(!ope.empty()) {
		postfix.push_back(ope.top());
		ope.pop();
	}

	return postfix;
}

int main() {
	string exp;
	cin>>exp;
	vector<char> postfix_exp = get_postfix(exp);

	for(char i: postfix_exp) {
		cout<<i<<" ";
	}
	cout<<endl;
}