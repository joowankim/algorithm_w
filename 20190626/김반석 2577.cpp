#include<iostream>
#include<string>

using namespace std;

int main() {
	int num = 0;
	int result = 0;
	for (int i = 0; i < 3; i++) {
		cin >> num;
		if (i == 0) {
			result = num;
		}
		else {
			result *= num;
		}
	}
	string str = to_string(result);
	
	for (int i = 0; i < 10; i++) {
		int result = 0;
		for (int j = 0; j < str.length(); j++) {
			char chr = str[j];
			int n = chr-'0';
			if (n == i) {
				result++;
			}
		}
		cout << result << "\n";
	}
	return 0;
}
