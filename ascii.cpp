#include<iostream>
using namespace std;

int main(){
    char a;
    cin>>a;
    int i=a;
    if(int(a)>=65 && int(a)<=90)
    cout<<"large";
    
    else if(int(a)>=97 && int(a)<=122)
    cout<<"small";
    else if(i>=0 && i<=9)
    cout<<"digit";

    
    return 0;
}