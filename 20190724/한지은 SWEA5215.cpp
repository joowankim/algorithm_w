#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int n, l;
int T[21], K[21];
int max_r;
bool visited[21];

void dfs(int idx, int sum, int csum){
	if(csum > l) return;

	max_r = max(max_r, sum);
  
  // if(max_r < sum) max_r = sum;

	for(int i=idx; i<n; i++){
		if(!visited[i]){
			visited[i] = true;
			dfs(i+1, sum + T[i], csum + K[i]);
			visited[i] = false;
		}
	}
}

int main(){

	int tc;
	cin >> tc;

	for(int i=1; i<=tc; i++){

		cin >> n >> l;

		for(int j=0; j<n; j++){

			cin >> T[j] >> K[j];
			visited[j] = false;

		}

		max_r = -1;
		dfs(0, 0, 0);

		cout << "#" << i << " " << max_r << endl;

	}

	return 0;

}
