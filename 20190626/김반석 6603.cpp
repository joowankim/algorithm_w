#include<iostream>
#include<vector>
#include<algorithm>
#define max 100
using namespace std;
void solve(vector<int>);
int main() {

	int n, N=0;

	vector<int> Testcase[max];
	while (1) {
		
		cin >> n;
		if (n == 0) {//0이면 종료.
			break;
		}
		for (int i = 0; i < n; i++) {//모든 값 vector에 넣기
			int temp;
			cin >> temp;
			Testcase[N].push_back(temp);
		}
		N++;
	}
	for(int i=0;i<N;i++)
		solve(Testcase[i]);//출력 함수

	return 0;
}
void solve(vector<int> vec) {
	vector<int> Testcase_temp;// 6개 이외의 수 저장

	int k = vec.size();
	int n = 6;
	for (int i = 0; i < n; i++) {
		Testcase_temp.push_back(1);
	}

	for (int i = 0; i < k - n; i++) {
		Testcase_temp.push_back(0);
	}
	
	int counter = Testcase_temp.size();
	do{
		for (int i = 0; i < counter; i++) {
				if(Testcase_temp[i]==1)
				cout << vec[i] << " ";
		}
		cout << "\n";
	} while (prev_permutation(Testcase_temp.begin(), Testcase_temp.end()));
	cout << "\n";
}
