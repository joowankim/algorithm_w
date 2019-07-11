#include <iostream>
#include <algorithm>
using namespace std;

const int IMPOSSIBLE = 1000000000;
int N, K;
int cost[101];
int dp[101][10001];

int coin(int n, int k){
   if(n==N) return (k==0 ? 0 : IMPOSSIBLE);
   if(dp[n][k]!= -1) return dp[n][k];

   int res = coin(n+1, k); // k<cost[n], n번째 동전 사용 불가
   if(k>=cost[n]) res = min(res, coin(n, k-cost[n]) + 1); // k>= cost[n], n번째 동전 사용

   dp[n][k] = res;
   return res;
}

int main(){
   cin >> N >> K;
   for(int i=0; i<N; i++){
      cin >> cost[i];
   }

   for(int i=0; i<=N; i++){
      for(int j=0; j<=K; j++){
         dp[i][j] = -1;
      }
   }

   int result = coin(0, K);
   if(result == IMPOSSIBLE) cout << -1;
   else cout << result;

   return 0;

}
