#include <iostream>
using namespace std;

int main()
{
    int x;
    // cin >> x;

    while (cin >> x)//we take input untill we got correct password
    {
        if (x == 1999)
        {
            cout << "correct"<<endl;
            break;
        }
        else
            cout << "wrong"<<endl;
    }

return 0;
}