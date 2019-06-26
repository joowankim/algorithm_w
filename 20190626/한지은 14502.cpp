#include <queue>
#include <algorithm>
#include <cstdio>
using namespace std;

const int dx[] = {-1,1,0,0};
const int dy[] = {0,0,-1,1};

int map[8][8];
int N, M, ans;

void bfs(){
	queue<int> vq; // 바이러스 큐
	int visit[8][8] = {0, };
	int backup[8][8];

	for(int y=0; y<N; y++){
		for(int x=0; x<M; x++){
			backup[y][x]=map[y][x];
			if(backup[y][x] == 2){
				vq.push(y*10+x);
				visit[y][x]=1;
			}
		}
	}

	while(!vq.empty()){
		int cur = vq.front();
		vq.pop();
		int cy = cur/10;
		int cx = cur%10;
		
		backup[cy][cx] = 2; // 왜 해주는 거지?

		for(int i=0; i<4; i++){
			int nx = cx + dx[i];
			int ny = cy + dy[i];

			if(ny<0 || ny>=N || nx<0 || nx>=M)
				continue;

			if(visit[ny][nx]==0 && backup[ny][nx]==0){
				visit[ny][nx]=1;
				vq.push(ny*10+nx);
			}
		}
	}

	int area=0;
	for(int i=0; i<N; i++){
		for(int j=0; j<M; j++){
			if(backup[i][j]==0){
				area++;
			}
		}
	}

	if(ans<area){
		ans = area;
	}
}

void pick_dfs(int cnt, int sy, int sx){

	if(cnt == 3){
		bfs();
		return;
	}

	for(int y=sy; y<N; y++){
		for(int x=sx; x<M; x++){
			if(map[y][x]==0){
				map[y][x]=1;
				pick_dfs(cnt+1,y,x);
				map[y][x]=0;
			}
		}
		sx=0;
	}

}

int main(){
	scanf("%d %d", &N, &M);

	for(int y=0; y<N; y++){
		for(int x=0; x<M; x++){
			scanf("%d", &map[y][x]);
		}
	}
	pick_dfs(0, 0, 0);
	printf("%d\n", ans);

	return 0;

}
