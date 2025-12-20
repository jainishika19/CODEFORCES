#include<iostream>
using namespace std;
#include<climits>


int main(){
    int sz;
    cin>>sz;
    long long smallest=INT_MAX;
    int index=1;
    int arr[sz];
    for(int i=0;i<sz;i++){
        cin>>arr[i];
    }
    for(int i=0;i<sz;i++){
          for(int i=0;i<sz;i++){
        if(arr[i]<smallest){
            smallest=arr[i];
            index=i+1;//+1 as we need start from 1 index not zero
        }
    }

        
}
cout<<smallest<<" "<<index;
    return 0;
}
