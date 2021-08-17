#include<iostream>
#include<vector>

using namespace std;

void swap(int *a,int *b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

void merge_arr(int a1[],int a2[],int n,int m) {
	int i=0,j=0;
	int *ele1,*ele2;

	while(i<n+m && j<m) {
		if(i<n) ele1 = &a1[i];
		else ele1 = &a2[i-n];

		ele2 = &a2[j];

		if(*ele1 <= *ele2) i++;
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
	int arr1[] = {1,3,5,7};
	int arr2[] = {0,3,5,8,9};

	merge_arr(arr1,arr2,4,5);

	for(int i=0; i<4; i++) cout<<arr1[i]<<" ";
	for(int i=0; i<5; i++) cout<<arr2[i]<<" ";	
	cout<<endl;
}