#include <iostream>
#include <bitset>
using namespace std;

// D - One Little, Two Little, Three Little Endians 

int main(){
    int n;
    while(cin >> n){
        bitset<32> b = n;
        bitset<32> tmp;
        for(auto i = 0; i < 8; i++){
            tmp[24 + i] = b[i];
        }
        for(auto i = 8; i < 16; i++){
            tmp[8 + i] = b[i];
        }
        for(auto i = 16; i < 24; i++){
            tmp[-8 + i] = b[i];
        }
        for(auto i = 24; i < 32; i++){
            tmp[-24 + i] = b[i];
        }
        cout << n << " converts to " << (int)(tmp.to_ulong()) << endl;
    }
    return 0;
}