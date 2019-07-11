#include <iostream>
#include <algorithm>
using namespace std;

int value[2][100001];
int dp[100001][3];
int n;

int sticker(int c, int status){
   // c열부터 뗐을 때의 최댓값 구하는 함수
   // c : 스티커를 뗀 열
   // status : 0 => 왼쪽 열에서 떼어낸 스티커 x
   //          1 => 왼쪽 열에서 위에 스티커 뗌
   //          2 => 왼쪽 열에서 아래 스티커 뗌

   if(c==n) return 0;
   if(dp[c][status]!=-1) return dp[c][status];

   int res = sticker(c+1, 0); // 아무것도 x
   if(status!=1) res = max(res, sticker(c+1, 1) + value[0][c]); // 위 스티커 뗐을 때
   if(status!=2) res = max(res, sticker(c+1, 2) + value[1][c]); // 아래 스티커 뗐을 때

   dp[c][status] = res;

   return res;

}

int main(){

   int tc;
   cin >> tc;
   
   while(tc--){

      cin >> n;
      for(int i=0; i<2; i++){
         for(int j=0; j<n; j++){
            cin >> value[i][j];
         }
      }

      for(int i=0; i<n; i++){
         for(int j=0; j<3; j++){
            dp[i][j] = -1;
         }
      }

      cout << sticker(0, 0) << endl;

   }

   return 0;

}
