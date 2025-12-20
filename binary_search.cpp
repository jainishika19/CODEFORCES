#include<iostream>
#include<algorithm>//for sort fntn
using namespace std;

void binarySearch(long long arr[],long long num,long long n){
    long long st=0,mid,end=n-1;
    long long f=0;
    while(st<=end){
        mid=(st+end)/2;
        if(arr[mid]==num){
            f=1; 
            break;
        }
        else if(arr[mid]>num){
            end=mid-1;
        }
        else{
            st=mid+1;
        }
    }
    if(f==1){
        cout<<"found\n";
    }
    else
    cout<<"not found\n";
}
int main(){
    long long n,q,num;
    cin>>n>>q;
    long long arr[n];
    for(long long i=0;i<n;i++){
        cin>>arr[i];
    }
    sort(arr,arr+n);//sorting array before searching
    
    for(long long i=0;i<q;i++){
        cin>>num;//taking i/p
        binarySearch(arr,num,n);//and then search it 

    }





    
    return 0;
}