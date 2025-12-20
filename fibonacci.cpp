// by simplest iterative method---
#include<iostream>
using namespace std;

int main(){
    long long n;
    cin>>n;
    if(n==1) 
    cout<<0;//a
    else if(n==2) 
    cout<<1;//b
    else{
    long long a=0,b=1,c;
    for(long long i=3;i<=n;i++){
        c=a+b;
        a=b;
        b=c;
    }
    cout<<b;
    // cout<<c; can;t we also cout c as it also holds a+b --answer
}

    return 0;
}
// always use long long 🥹🥹🥹


