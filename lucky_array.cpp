// #include<iostream>
// #include<climits>
// using namespace std;

// int main(){
//     int n;
//     cin>>n;
//     int min=INT_MAX;
//     int arr[n];
//     int count=0;
//     for(int i=0;i<n;i++){
//         cin>>arr[i];
//     }
//     for(int i=0;i<n;i++){
//        if(arr[i]<min){
//         // count+=1;
//         min=arr[i];
//        }


//     }
//     cout<<count;
//     // if(count%2!=0){
//     //     cout<<"Lucky";
//     // }
//     // else{
//     //     cout<<"Unlucky";
//     // }
//     // cout<<min;

//     return 0;
// }




#include<iostream>
#include<vector>
#include<climits>
using namespace std;

int main(){
    int n;
    cin>>n;
    vector<int> v(n);
    // vector<int> v1; //empty vector
    for(int i=0;i<n;i++){
        cin>>v[i];
    }
    int min=INT_MAX;
    int count=0;
    for(int i=0;i<n;i++){
        if(v[i]<min){
            count+=1;
        }
        
        if(count%2!=0){
            cout<<"Lucky";
    
        }
        else cout<<"Unlucky";
    }
    
    // for(int i=0;i<n;i++){
    //    if(arr[i]<min){
    //     // count+=1;
    //     min=arr[i];
    //    }


    // }
    // cout<<count;
    // if(count%2!=0){
    //     cout<<"Lucky";
    // }
    // else{
    //     cout<<"Unlucky";
    // }
    // cout<<min;


    
    return 0;
}


// solve it by vector--
// append in a new list by push_back fntn and then check