#include <iostream>
using namespace std;
int main()
{
	int x=0, y=0,temp=0;
	cin >> x >> y;
	
	temp = y;
	while(--x){
		if (x  == 1 || x == 3 || x == 5 || x == 7 || x == 8 || x == 10 || x == 12) {
			temp = temp + 31;
		}
		else if (x  == 2)
			temp += 28;
		else
			temp += 30;
	}
	if (temp % 7 == 0)
		cout << "SUN";
	else if (temp % 7 == 1)
		cout << "MON";
	else if (temp % 7 == 2)
		cout << "TUE";
	else if (temp % 7 == 3)
		cout << "WED";
	else if (temp % 7 == 4)
		cout << "THU";
	else if (temp % 7 == 5)
		cout << "FRI";
	else
		cout << "SAT";
	return 0;
}
