#include<iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    for(int i=1;i<=n;i++){
        int spaces=n-i; // at starting spaces=3
        int stars=2*i-1; // at staring star=1
        //printing spaces
        for(int s=0;s<spaces;s++){
            cout<<" ";
        }
        for(int s=0;s<stars;s++){
            cout<<"*";
        }
        cout<<endl;
    }
return 0;
}


//------for shape 3------

// #include<iostream>
// using namespace std;

// int main(){
//     int n;
//     cin>>n;
//     for(int i=1;i<=n;i++){
//         int spaces=n-i; // at starting spaces=3
//         int stars=2*i-1; // at staring star=1
//         //printing spaces
//         for(int s=0;s<spaces;s++){
//             cout<<" ";
//         }
//         for(int s=0;s<stars;s++){
//             cout<<"*";
//         }
//         cout<<endl;
//     }

//         for(int i=n;i>=1;i--){
//         int spaces=n-i; // at starting spaces=3
//         int stars=2*i-1;
//         for(int s=0;s<spaces;s++){
//             cout<<" ";
//         }
//         for(int s=0;s<stars;s++){
//             cout<<"*";
//         }
//         cout<<endl;
//     }
    

//     return 0;
// }