#include<iostream>
#include<algorithm>

using namespace std;
#define max 100

int main() {
	for (int k = 0; k < 10; k++) {
		int test;
		cin >> test;
		int col[max];
		int result = 0;
		for (int i = 0; i < 100; i++) {
			col[i] = 0;
		}
		int cross1 = 0, cross2 = 0;

		for (int i = 0; i < 100; i++) {
			int row = 0;
			for (int j = 0; j < 100; j++) {
				int data;
				cin >> data;
				row = row + data;
				if (i == j) {
					cross1 += data;
				}
				if (i + j == 99) {
					cross2 += data;
				}
				col[j] = col[j] + data;
				if (j == 99) {
					if (result < row) {
						result = row;
					}
				}
				if (i == 99) {

					if (result < col[j]) {
						result = col[j];
					}
					if (j == 0) {
						if (result < cross1) {
							result = cross1;
						}
					}
					if (j == 99) {
						if (result < cross2) {
							result = cross2;
						}
					}
				}
			}
		}
		cout << "#"<<k+1<<" "<<result<<"\n";
	}

	return 0;
}
