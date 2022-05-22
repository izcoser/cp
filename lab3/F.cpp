#include <iostream>
#include <set>
// F - Make Them Odd
using namespace std;

int main(){
    int t;
    cin >> t;
    for(int i = 0; i < t; i++){
        int n;
        cin >> n;
        set<int> s;
        for(int j = 0; j < n; j++){
            int k;
            cin >> k;
            while(k % 2 == 0){
                s.insert(k);
                k /= 2;
            }
        }
        cout << s.size() << endl;
    }
    return 0;
}
