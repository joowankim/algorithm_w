#include <iostream>
#include <algorithm>
using namespace std;

int map[101][101] = {0, };
int val = 0;
int ans = 0 ;

void dfs(int y, int x, int vmax){

	for(int y=0; y<100; y++){
		for(int x=0; x<100; x++){
			val += map[y][x];
		}

		if(vmax < val){			
			vmax = val;
		}
		val = 0;
	}

	for(int x=0; x<100; x++){
		for(int y=0; y<100; y++){
			val += map[y][x];
		}
		if(vmax < val){
			vmax = val;
		}
		val = 0;
	}

	for(int i=0; i<100; i++){
			val += map[i][i];
	}

	if(vmax < val){
		vmax = val;
	}
	val = 0;
    

    int j=99;
    
    for(int i=0; i<100; i++){
     val += map[i][j];   
        j--;
    }
    if(vmax < val){
     vmax = val;   
    }
    
    val = 0;
    
    ans = vmax;
    
}

int main(){

	int N=10;
	int TC=0;

	while(N--){

		cin >> TC;

		for(int y=0; y<100; y++){
			for(int x=0; x<100; x++){
				cin >> map[y][x];
			}
		}

		dfs(0, 0, 0);

		cout << "#" << TC << " " << ans << endl;
        ans = 0;

	}// while

	return 0;
}
