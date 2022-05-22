#include <iostream>
#include <algorithm>

// E - Counting Kangaroos is Fun
using namespace std;

int main(){
    int n;
    cin >> n;
    int visible = n;
    int v[n];
    for(int i = 0; i < n; i++){
        cin >> v[i];
    }
    sort(v, v + n);
    int startAt = n/2;
    for(int i = 0; i < n/2; i++){
        bool found = false;
        for(int j = startAt; j < n; j++){
            if(v[j] >= 2 * v[i]){
                visible--;
                found = true;
                startAt = j + 1;
                break;
            }
        }
        if(!found){
            break;
        }
    }
    cout << visible << endl;

    return 0;
}
