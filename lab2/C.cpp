#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
// C - ID Codes

int main(){
    while(1){
        string code;
        getline(cin, code);
        
        if(code.compare("#") == 0){
            break;
        }
        vector<char> v(code.begin(), code.end());
        if(next_permutation(v.begin(), v.end())){
            for(char i : v){
                cout << i;
            }
            cout << endl;
        }
        else{
            cout << "No Successor" << endl;
        }
    }
    return 0;
}