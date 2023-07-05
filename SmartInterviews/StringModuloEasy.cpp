#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int t;cin>>t;
    while(t-->0){
        string n;
        long p;
        cin>>n>>p;
        int i=0;
        long res=0;
        while (i<n.length()){
            res=(res*10+n[i++]-'0')%p;
        }
        cout<<res<<endl;
    }
    return 0;
}

/*
12345 % 100:
ans = 0
ans = (0*10 + 1)%100
ans = (1*10 + 2)%100
ans = (12*10 + 3)%100
ans = (23*10 + 4)%100
ans = (34*10 + 5)%100
ans = 45.
*/
