#include <iostream>
using namespace std;

int dp[1001][1001];
int N, K;
const int mod = 10007;

int main(){

	cin >> N >> K;

	for(int i=0; i<=N; i++){
		for(int j=0; j<=N; j++){
			if(i==0 || j==0) dp[i][j] = 1;
		}
	}

	for(int i=1; i<=N; i++){
		for(int j=0; j<=N; j++){
			dp[i][j] = dp[i-1][j] + dp[i][j-1];
			dp[i][j] %= mod;
		}
	}

	cout << dp[N-K][K] << endl;

	return 0;

}
