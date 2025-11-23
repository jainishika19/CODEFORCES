#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    long long n,m,k;
    cin>>n>>m>>k;
    long use_mouth;
    use_mouth=min(n,min(m,k));
    //if we have to find min(n,m,k) direct by passing 
    //3 values then syntax of thus is--min({m,n,k})
    n-=use_mouth;
    m-=use_mouth;
    k-=use_mouth;
    long use_no_mouth=min(n/2,k);
    long d=use_mouth+use_no_mouth;
    cout<<d;


    return 0;
}