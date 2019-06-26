#include <iostream>
#include <queue>
using namespace std;

const int dy[] = {0, 0, 1, -1};
const int dx[] = {1, -1, 0 ,0};

int M, N, K;
int map[51][51] = {0, };
int y, x;
int cnt=0;

int bfs(){

	queue <int> q;
	int visited[51][51] = {0, };

	for(int y=0; y<N; y++){
		for(int x=0; x<M; x++){
			if(map[y][x]==1) q.push(y*10+x);
		}
	}

	cnt = 0;
	int cur = 0;

	while(!q.empty()){

		cur = q.front(); q.pop();
		int cy = cur/10;
		int cx = cur%10;
		
		if(visited[cy][cx]==0 && map[cy][cx]==1){
			cnt++;
		}

		for(int i=0; i<4; i++){
			int ny = cy + dy[i];
			int nx = cx + dx[i];

			if(ny<0 || ny>=N || nx<0 || nx>=M) continue;

			if(visited[ny][nx]==0 && map[ny][nx]==1){
				visited[ny][nx]=1;
				map[ny][nx]=0;
			}
		}
	}

    return cnt;
}

int main(void){

	int TC;
	cin >> TC;

	while(TC--){

		cin >> M >> N >> K;

		for(int i=0; i<K; i++){
			cin >> x >> y;
			map[y][x] = 1;
		}

		cout << bfs() << endl;
		
	}// while

	return 0;

}
