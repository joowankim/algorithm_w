#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;
#define MAX 101

int n, m, k;
int A[MAX][MAX] = {0, };
int visited[MAX][MAX] = {0, };
int backup[MAX][MAX] = {0, };

struct POSI
{
	int r, c, s;
};

vector<POSI> turn;

int min_res = 0x7fffffff;

void SUM(int arr[MAX][MAX])
{
	for(int i=0; i<n; i++)
	{
		int sum=0;
		for(int j=0; j<m; j++)
		{
			sum += arr[i][j];
		}
		min_res = min(min_res, sum);
	}

}


void Turn(vector<int> v)
{
	for(int y=0; y<n; y++)
	{
		for(int x=0; x<m; x++)
		{
			backup[y][x] = A[y][x];
		}
	}


	while(!v.empty())
	{
		int cur = v.front();
		POSI tg = turn[cur];

		int cr = tg.r;
		int cc = tg.c;
		int cs = tg.s;

		for(int y=0; y<n; y++)
		{
			for(int x=0; x<m; x++)
			{
				if(y < cr * cs && x >= cc * cs)
				{
					backup[y][x] = A[y][x+1];
				}
				else if(y <= cr * cs && x > cc * cs)
				{
					backup[y][x] = A[y+1][x];
				}
				else if(y > cr * cs && x >= cc * cs)
				{
					backup[y][x] = A[y][x-1];
				}
				else if(y >= cr * cs && x < cc * cs)
				{
					backup[y][x] = A[y-1][x];
				}
			}
		}
	}

	SUM(backup);
}


int main()
{
	cin >> n >> m >> k;

	for(int y=0; y<n; y++)
	{
		for(int x=0; x<m; x++)
		{
			cin >> A[y][x];;
		}
	}

	SUM(A);

	POSI target;
	int r, c, s;
	for(int i=0; i<k; i++)
	{
		cin >> r >> c >> s;
		target.r = r, target.c = c, target.s = s;
		turn.push_back(target);
	}

	vector<int> v(101);
	for(int i=0; i<k; i++)
	{
		v[i] = i;
	}

	while(next_permutation(v.begin(), v.end()))
	{
		Turn(v);
	}
	
	cout << min_res << endl;

	return 0;
}
