#include <iostream>
#include <queue>
using namespace std;

const int dy[] = {0, 0, -1, 1};
const int dx[] = {1, -1, 0, 0};

char map[51][51];
int n, m;
int max_res = 0, min_res = 0x7fffffff;

void bfs()
{

   int visited[51][51] = {0, };
   char backup[51][51];
   queue<pair<int,int>> q;

   for(int y=0; y<n; y++)
   {
      for(int x=0; x<n; x++)
      {
         backup[y][x] = map[y][x];
         if(backup[y][x]=='0')
         {
            q.push(make_pair(y,x));
            visited[y][x] = 1;
         }         
      }
   }

   int cnt=0;
   int vcnt = 0;
   while(!q.empty())
   {
      cnt++; // 시간

      int q_size = q.size();
      for(int j=0; j<q_size; j++)
      {
         int cy = q.front().first;
         int cx = q.front().second;
         q.pop();

         for(int i=0; i<4; i++)
         {
            int ny = cy + dy[i];
            int nx = cx + dx[i];

            if(ny < 0 || ny >= n || nx < 0 || nx >= n) continue;


            if(backup[ny][nx]=='*' && visited[ny][nx]==0)
            {
              
               backup[ny][nx] = '0';
               //cout << "!!!!!!!!!!!!!!!!1 backup : "<< backup[ny][nx] << endl;
               visited[ny][nx] = 1;
               q.push(make_pair(ny, nx));
            }

            if(backup[ny][nx]=='@' && visited[ny][nx]==0)
            {
               backup[ny][nx] = '0' + cnt;
               //cout << " backup : "<< backup[ny][nx] << endl;
               visited[ny][nx] = 1;
               q.push(make_pair(ny, nx));
            }
            
         }// for-i
      }// for-j
   
      

   }// while

   for(int i=0; i<n; i++)
   {
      for(int j=0; j<n; j++)
      {
         if(backup[i][j]=='@')
         {
            min_res = 1000000;
            return;
         }

         if(backup[i][j]=='*' || backup[i][j]=='0') continue;
         //cout << "#########backup : "<< backup[i][j] << endl;
         max_res = (max_res < backup[i][j]-'0') ? backup[i][j]-'0' : max_res;
      }
   }

   min_res = (min_res > max_res) ? max_res : min_res;

}

void dfs(int cnt, int sy, int sx)
{
   if(cnt==m)
   {  
      // cout<<"라너란맂러ㅏㄷㅈ러ㅏ디" << endl;
      bfs();
      return;
   }

   for(int y=sy; y<n; y++)
   {
      for(int x=sx; x<n; x++)
      {
         if(map[y][x]=='*')
         {
            map[y][x] = '0';
            dfs(cnt+1, y, x);
            map[y][x] = '*';
         }
      }
      sx = 0;
   }
}

int main()
{
   cin >> n >> m;
   for(int y=0; y<n; y++)
   {
      for(int x=0; x<n; x++)
      {
         cin >> map[y][x];
         if(map[y][x]=='0') map[y][x] = '@'; // 빈칸
         else if(map[y][x]=='1') map[y][x] = '-'; // 벽
         else if(map[y][x]=='2') map[y][x] = '*'; // 바이러스

      }
   }

   dfs(0, 0, 0);


   if(min_res==1000000) cout << -1 << endl;
   else cout << min_res << endl;

   return 0;
}
