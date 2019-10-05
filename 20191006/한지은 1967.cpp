#include <iostream>
#include <cstring>
using namespace std;

int n, a, b, c;
int tree[10001][10001] = {0, };
int arr[10001] = {0, };
bool visited[10001][10001] = {0, };

int ans = -1;
int maxlen = 0;

void max_len(int sn, int en, int maxlen)
{
	if(tree[en][sn]!=0 && visited[en][sn]==0)
	{
		maxlen += tree[en][sn];
		visited[en][sn] = 1;
		visited[sn][en] = 1;
		ans = (ans < maxlen) ? maxlen : ans;
		return;
	}

	for(int i=1; i<=n; i++)
	{
		if(tree[i][sn]!=0 && visited[i][sn]==0)
		{
			visited[i][sn] = 1;
			visited[sn][i] = 1;
			max_len(i, en, maxlen + tree[i][sn]);
		}	
	}
}

int main()
{
	cin >> n;

	
	for(int i=0; i<n-1; i++)
	{
		cin >> a >> b >> c;
		tree[a][b] = c;
		tree[b][a] = c;
	}

	int num = 0;
	if(n==2)
	{
		cout << c << endl;
	}
	else
	{
		for(int i=a+1; i<=n; i++)
	{
		    arr[num] = i;
			num++;
	}

	
	int sn, en = 0;
	for(int i=0; i<num; i++)
	{
		sn = arr[i];

		for(int j=i+1; j<num; j++)
		{		
			en = arr[j];
			memset(visited, 0, sizeof(visited));
			max_len(sn, en, 0);			
		}
	}


	cout << ans << endl;

	return 0;

	}
	

}
