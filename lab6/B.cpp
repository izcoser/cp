#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(){
    int lookFrom = 0;
    string a;
    string s;
    cin >> a;
    cin >> s;
    sort(s.begin(), s.end(), greater<>());
    for(auto n : s){
        bool replaced = false;
        for(int i = lookFrom; i < a.size(); i++){
            if(n > a[i]){
                a[i] = n;
                lookFrom = i + 1;
                replaced = true;
                break;
            }
        }
        if(!replaced){
            break;
        }
    }
    cout << a << endl;
}
