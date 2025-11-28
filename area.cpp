// r=float(input())
// area=3.141592653*r*r
// print(area)


#include<iostream>
using namespace std;
#include<iomanip>

int main(){
    float r;
    cin>>r;
    cout<<fixed<<setprecision(9)<<3.141592653*r*r;
    return 0;
}