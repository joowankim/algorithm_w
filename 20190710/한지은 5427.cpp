#include <iostream>
#include <queue>
#include <cstdio>
using namespace std;

int w, h;

#define EMPTY '.'
#define WALL '#'
#define SANG '@'
#define FIRE '*'

char map[1001][1001];
int visited[1001][1001];
queue<pair<int, int>> sq; // 상근 큐
queue<pair<int, int>> fq; // 불 큐

int bfs(){
   bool escape = false;
   int dx[] = {1, -1, 0, 0};
    int dy[] = {0, 0, 1, -1};

   while(1){

      int sqsize = sq.size();
      int fqsize = fq.size();

      if(sqsize==0 && fqsize==0){
         break;
      }

      while(sqsize--){
         int sy = sq.front().first;
         int sx = sq.front().second;
         sq.pop();

         if(map[sy][sx]!=SANG)
            continue;

         if(sy == 0 || sy == h-1 || sx == 0 || sx == w-1){
            escape = true;
            return visited[sy][sx];
         }

         for(int i=0; i<4; i++){
            int ny = sy + dy[i];
            int nx = sx + dx[i];

            if(map[ny][nx]==EMPTY && visited[ny][nx]==0){
               map[ny][nx] = SANG;
               visited[ny][nx] = visited[sy][sx] + 1;
               sq.push(make_pair(ny, nx));
            }
         }

      }// while sq

      while(fqsize--){
         int fy = fq.front().first;
         int fx = fq.front().second;
         fq.pop();

         for(int i=0; i<4; i++){
            int ny = fy + dy[i];
            int nx = fx + dx[i];

            if(map[ny][nx]==EMPTY || map[ny][nx]==SANG){
               map[ny][nx] = FIRE;
               visited[ny][nx] = -1;
               map[fy][fx] = WALL;
               fq.push(make_pair(ny, nx));
               
            }
         }

      }// while fq

   }// while

   return -1;

}

int main(){

   int tc;
   cin >> tc;

   while(tc--){
      cin >> w >> h;

      while(!sq.empty()){
         sq.pop();
      }

      while(!fq.empty()){
         fq.pop();
      }

      for(int y=0; y<h; y++){
         for(int x=0; x<w; x++){
            map[y][x] = EMPTY;
            visited[y][x] = 0;
         }
      }

      for(int y=0; y<h; y++){
         for(int x=0; x<w; x++){

            cin >> map[y][x];
            
            if(map[y][x] == SANG){
               sq.push(make_pair(y,x));
               visited[y][x]=1;
            }
            if(map[y][x] == FIRE){
               fq.push(make_pair(y,x));
            }
         }
      }

      int res = bfs();

      if(res==-1){
         cout << "IMPOSSIBLE" << endl;
      }else{
         cout << res << endl; 
      }

   }

}
