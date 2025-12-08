#include <iostream>
#include <climits>
using namespace std;

int main()
{
    int arr[5] = {1, 2, 3, 4, 5};
    int n = 5;
    int max_num=INT_MIN;
    for (int st = 0; st < n; st++)
    {
        for (int end = st; end < n; end++)//some subarrays have same start and end like
        //single element subarrays (1,2,3,4,5)they have same st and end
        {
            for (int i = st; i <= end; i++)
            {
                cout << max(arr[i],max_num);
            }
            cout << " ";
        }
        cout << endl;
    }
    return 0;
}