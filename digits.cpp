
#include<iostream>
using namespace std;

int main(){
    int t;
    cin>>t;
    for(int i=1;i<=t;i++){
        long long n;
        cin>>n;
        // if(n==0) cout<<0;
        while(n>=0){
            int ld=n%10;
            n=n/10;
            cout<<ld;
            cout<<" ";

        }
        cout<<endl;
    }
    
    return 0;
}

// testcase not passsed----