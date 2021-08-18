#include<iostream>
#include<vector>

using namespace std;

void swap(int *a,int *b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

void merge_arr_weird(int a1[],int a2[],int n,int m) {
	int max_num = -1;

	for(int i=0;i<n;i++) {
		if(max_num<a1[i]) max_num=a1[i];
	}

	for(int i=0;i<m;i++) {
		if(max_num<a2[i]) max_num=a2[i];
	}

	max_num++;

	int x=0,y=0,k=0;

	while(x<n && y<m && k< (m+n)) {
		int e1 = a1[x]%max_num;
		int e2 = a2[y]%max_num;

		if(e1<=e2) {
			if(k<n) {
				a1[k] += e1*max_num;
			}else {
				a2[k-n] += e1*max_num;
			}
			k++;
			x++;
		}else {
			if(k<n) {
				a1[k] += e2*max_num;
			}else {
				a2[k-n] += e2*max_num;
			}
			k++;
			y++;
		}
	}

	while(x<n) {
		int e1 = a2[x]%max_num;

		if(k<n) {
			a1[k] += e1*max_num;
		}else {
			a2[k-n] += e1*max_num;
		}
		x++;
		k++;	
	}

	while(y<m) {
		int e2 = a2[y]%max_num;

		if(k<n) {
			a1[k] += e2*max_num;
		}else {
			a2[k-n] += e2*max_num;
		}
		y++;
		k++;	
	}

	for(int i=0;i<n;i++) {
		a1[i]=a1[i]/max_num;
	}

	for(int i=0;i<m;i++) {
		a2[i]= a2[i]/max_num;
	}
}

void merge_arr_naive(int a1[],int a2[],int n,int m) {
	int i=0,j=0;
	int *ele1,*ele2;

	while(i<n+m) {
		if(i<n) ele1 = &a1[i];
		else ele1 = &a2[i-n];

		ele2 = &a2[j];

		if(*ele1 <= *ele2) {
			i++;

			if(i>n-1) j++;
		}
		else if(*ele1 > *ele2) {
			swap(ele1,ele2);
			i++;

			int k = j+1, l = j;
			while(k<m && a2[l] > a2[k]) {
				swap(&a2[l++],&a2[k++]);
			}

			if(i>n-1) j++;
		}
	}
}

int main() {
	int arr1[] = {7,9,9,10,11,11,13,14,17,19};
	int arr2[] = {1,1,4,5,8,11,13,16,19,19};

	merge_arr_weird(arr1,arr2,10,10);

	for(int i=0; i<10; i++) cout<<arr1[i]<<" ";
	for(int i=0; i<10; i++) cout<<arr2[i]<<" ";	
	cout<<endl;
}