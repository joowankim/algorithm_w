#include<iostream>
#include <string>
using namespace std;
#define max 10000
int main() {
	int n, x=0;
	int arr[max];
	int count = 0;
	cin >> n >> x;
	for (int i = 0; i < n; i++) {
		int a = 0;
		cin >> a;
		if (a < x) {
			arr[count] = a;
			count++;
		}
	}
	for (int i = 0; i < count; i++) {
		cout << arr[i] << " ";
	}
	return 0;
}
