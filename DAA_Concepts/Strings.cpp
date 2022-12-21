#include <iostream>
using namespace std;
int main()
{
    // string str="hello world";
    // string str1(5,'m');
    string str = "bihibuyvuv";
    // getline(cin, str);
    // // cin >> str;
    // cout << str << endl;
    // str.append("hello");
    // str.append(" world");
    // str = str + "family";
    // cout << str;
    // string s1 = "abc";
    // string s2 = "def";
    // cout << s2.compare(s1) << endl;
    // s1.clear();
    // if (s1.empty())
    // {
    //     cout << "string is empty";
    // }
    // cout << str;
    // cout << str.find("buy");
    str.insert(3, "hello");
    cout << str << endl;
    cout << str.size();
    cout << str.length(); // same
    cout << str.substr(6, 4);
}