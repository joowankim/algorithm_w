#include<iostream>
#include<string>

using namespace std;

int main() {
	int result = 0;
	for (int i = 0; i < 5; i++) {
		int point;
		cin >> point;
		if (point < 40) {
			result += 40;
			continue;
		}
		result += point;
	}
	cout << result / 5;
	return 0;
}
