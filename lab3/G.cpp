#include <iostream>
#include <map>
// G - Boxes Packing
using namespace std;

int main(){
    int n;
    int max = 0;
    map<int, int> sizeToCount;
    cin >> n;
    for(int i = 0; i < n; i++){
        int k;
        cin >> k;
        sizeToCount[k]++;
        if(sizeToCount[k] > max){
            max = sizeToCount[k];
        }
    }
    cout << max << endl;
    return 0;
}
