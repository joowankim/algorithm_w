#include <iostream>
#include <queue>
using namespace std;

int n, m;
int a, b;
int x, y;
int visited[101][101];
int depth[101];
queue<int> q;

int main(){

   cin >> n >> a >> b >> m;
   q.push(a);

   for(int i=0; i<m; i++){
      cin >> x >> y;
      visited[x][y] = visited[y][x] = 1;
   }

   while(!q.empty()){
      int cur = q.front();
      q.pop();
      for(int i=0; i<n; i++){
         if(visited[cur][i]!=0 && depth[i]==0){
            depth[i] = depth[cur]+1;
            q.push(i);
         }
      }
   }

   if(depth[b]==0){
      cout << -1;
   }else {
      cout << depth[b];
   }

   return 0;
}
