#include <iostream>
#include <cstring>
#include <queue>
using namespace std;

const int dy[] = {0, 0, -1, 1};
const int dx[] = {1, -1, 0, 0};

int map[51][51] = {0, };
int arr[51][51] = {0, };
int visited[51][51] = {0, };
int r, c, t = 0;
queue <int> airq;
queue <pair<int, int>> dustq;

int upy, dny = 0;

void AirClean()
{
   // 반시계
   int y = upy - 1;
   int x = 0;
   map[y][x] = 0; // 미세먼지 제거
   for(int i=0; i<y; i++)
   {
      map[y][x] = map[y-1][x];
      y--;
   }

   for(int i=0; i<c-1; i++)
   {
      map[y][x] = map[y][x+1];
      x++;
   }

   for(int i=0; i<upy; i++)
   {
      map[y][x] = map[y+1][x];
      y++;

   }

   for(int i=0; i<c-1; i++)
   {
      if(map[y][x-1]==-1) map[y][x] = 0;
      else{
         map[y][x] = map[y][x-1];
         x--;
      }      
   }



   // 시계
   y = dny + 1;
   x = 0;
   map[y][x] = 0; // 미세먼지 제거

   for(int i=0; i<r-y-1; i++)
   {
      map[y][x] = map[y+1][x];
      y++;
   }

   for(int i=0; i<c-1; i++)
   {
      map[y][x] = map[y][x+1];
      x++;
   }

   for(int i=0; i<dny; i++)
   {
      map[y][x] = map[y-1][x];
      y--;

   }

   for(int i=0; i<c-1; i++)
   {
      if(map[y][x-1]==-1)   map[y][x] = 0;
      else
      {
         map[y][x] = map[y][x-1];
         x--;
      }
   }


   for(int i=0; i<r; i++)
   {
      for(int j=0; j<c; j++)
      {
         if(map[y][x]>0) dustq.push(make_pair(i,j));
      }
   }
}

void PlusDust()
{
   for(int y=0; y<r; y++)
   {
      for(int x=0; x<c; x++)
      {
         map[y][x] += arr[y][x];
      }
   }

}

void Diffusion()
{
   memset(arr, 0, sizeof(arr));

   int dust_size = dustq.size();
   for(int i=0; i<dust_size; i++)
   {
      int cy = dustq.front().first;
      int cx = dustq.front().second;
      dustq.pop();

      int dcnt = 0;

      for(int i=0; i<4; i++)
      {
         int ny = cy + dy[i];
         int nx = cx + dx[i];

         if(ny < 0 || ny >= r || nx < 0 || nx >= c) continue;
         
            dcnt++;
             arr[ny][nx] += map[cy][cx]/5;
         
      }

      map[cy][cx] = map[cy][cx] - (map[cy][cx]/5)*dcnt;

   }

   PlusDust();

}

int main()
{
   cin >> r >> c >> t;

   for(int y=0; y<r; y++)
   {
      for(int x=0; x<c; x++)
      {
         cin >> map[y][x];
         if(map[y][x]==-1)
         {
            airq.push(y);
         }
         else if(map[y][x]!=0 && map[y][x]!=-1)
         {
            dustq.push(make_pair(y,x));
         }

      }
   }

   upy = airq.front();
   airq.pop();
   dny = airq.front();
   airq.pop();

   while(t--)
   {
      Diffusion();
      AirClean();

   }// t초 동안 발생



   int res = 0;
   for(int y=0; y<r; y++)
   {
      for(int x=0; x<c; x++)
      {
         if(map[y][x]>0) res += map[y][x];
      }
   }

   cout << res << endl;
   return 0;
}
