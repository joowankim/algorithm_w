#include <iostream>
using namespace std;

int tc;
char tree[27][2];

// 본인 > 왼 > 오
void preorder(int location)
{
	if(location + 'A' == '.') return;

	cout  << (char)(location + 'A');
	preorder(tree[location][0] - 'A');
	preorder(tree[location][1] - 'A');
	return;
}

// 왼 > 본인 > 오
void inorder(int location)
{
	if(location + 'A' == '.') return;

	inorder(tree[location][0] - 'A');
	cout << (char)(location + 'A');
	inorder(tree[location][1] - 'A');
	return;
}

// 왼 > 오 > 본인
void postorder(int location)
{
	if(location + 'A' == '.') return;

	postorder(tree[location][0] - 'A');
	postorder(tree[location][1] - 'A');
	cout << (char)(location + 'A');
	return;

}
int main()
{
	cin >> tc;
	char a, b, c;

	while(tc--)
	{
		cin >> a >> b >> c;
		tree[a - 'A'][0] = b;
		tree[a - 'A'][1] = c;
	}

	preorder(0);
	cout << endl;

	inorder(0);
	cout << endl;

	postorder(0);
	cout << endl;

	return 0;
}
