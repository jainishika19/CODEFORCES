# // #include<iostream>
# // using namespace std;

# // int main(){
# //     int i;
# //     long long l;
# //     char c;
# //     float f;
# //     double d;

# //     cin>>i>>l>>c>>f>>d;
# //     cout<<i<<endl;
# //     cout<<l<<endl;
# //     cout<<c<<endl;
# //     cout<<f<<endl;
# //     cout<<d<<endl;

# //     return 0;
# // }












# // #include<iostream>
# // using namespace std;
# // #include<iomanip>

# // int main(){
# //     int a;
# //     long long l;
# //     char c;
# //     float f;
# //     double d;

# //     cin>>a;
# //     cin>>l;
# //     cin>> ws>> c;
# //     cin>>f;
# //     cin>>d;

# //     cout<<a<<endl;
# //     cout<<l<<endl;
# //     cout<<c<<endl;
# //     cout<<f<<endl;
# //     cout<<fixed<<setprecision(3)<<d<<endl;

    
# //     return 0;
# // }


# taking input in a single line 
a,l,c,f,d=input().split()
#  convert types
a=int(a)
l=int(l)
c=c #by default input takes as str (and char here length of 1 str)
f=float(f)
d=float(d)

print(a)
print(l)
print(c)
print(f)
print(d)

