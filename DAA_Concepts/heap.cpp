#include<iostream>
using namespace std;
int main(){
    int a=10; //allocate memory in stack
    int *p=new int(); //allocate memory in heap
    *p=10;
    delete(p); //operator delete() will deallocate memory from heap but still have its prsence in stack memory
    p=new int[4]; //allocates consecutive memory for four int 
    p[0]=1;
    p[1]=2;
    p[2]=3;
    p[3]=4;
    cout << p[0]<<endl;
    delete[] p; //deallocates all
    p=NULL;  //pointing to none
    return 0;
} 