#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

void swap(int *a, int *b) {
	int temp = *a;
	*a = *b;
	*a = temp;
}

int count_inversion_bubble(int a[],int n) {
	int c = 0;
	for(int i=0; i<n-1; i++) {
		for(int j=0; j<n-1-i; j++) {
			if(a[j] > a[j+1]) {
				swap(&a[j],&a[j+1]);
				c++;
			}
		}
	}

	return c;
}


int merge(int a[],int l,int mid,int h,int count) {
	int max_ele = -1;

	for(int i=l;i<=h;i++) max_ele = max(max_ele,a[i]);
	max_ele++;

	int i = l, j = mid+1, k = l;
	while(i<=mid && j<=h) {
		int ele1 = a[i]%max_ele;
		int ele2 = a[j]%max_ele;

		if(ele1 <= ele2) {
			a[k]+=(max_ele*ele1);
			i++;
		} else {
			a[k]+=(max_ele*ele2);
			count+=mid+1-k;
			j++;
		}
		k++; 
	}

	while(i<=mid) {
		int ele1 = a[i++]%max_ele;
		a[k]+=(ele1*max_ele);
		k++;
	}

	while(j<=h) {
		int ele2 = a[j++]%max_ele;
		a[k]+=(ele2*max_ele);
		k++;
	}

	for(i=l;i<=h;i++) a[i]/=max_ele;

	return count;	
}

int count_inversion_merge_sort(int a[],int l,int h,int k) {
	if(l<h) {
		int mid = (l+h)/2;
		k+=count_inversion_merge_sort(a,l,mid,0);
		k+=count_inversion_merge_sort(a,mid+1,h,0);
		int b = merge(a,l,mid,h,0);
		return b+k;
	}

	return k;
}

int main() {
	int n,i=0,x;
	cin>>n;

	int arr[n];
	while(i<n) {
		cin>>x;
		arr[i]=x;
		i++;
	}

	int count = count_inversion_merge_sort(arr,0,n-1,0);
	cout<<count<<endl;
}