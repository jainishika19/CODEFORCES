#include <iostream>
using namespace std;

int main()
{
    int arr[5] = {1, 2, 3, 4, 5};
    int n = 5;
    int count=0;
    for (int st = 0; st < n; st++)
    {
        for (int end = st; end < n; end++)//some subarrays have same start and end like
        //single element subarrays (1,2,3,4,5)they have same st and end
        {
            for (int i = st; i <= end; i++)
            {
                count+=1;
            }
        }
        cout <<count;
    }
    return 0;
}