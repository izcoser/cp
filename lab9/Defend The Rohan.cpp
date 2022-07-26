#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int m[50][50];
int N = 0;
void floyd_warshall(){
    for(int k = 0; k < N; k++){
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(m[i][j] > m[i][k] + m[k][j]){
                    m[i][j] = m[i][k] + m[k][j];
                }
            }
        }
    }
}

int main(){
    int t;
    cin >> t;
    for(int c = 0; c < t; c++){
        cin >> N;
        int s = 0;
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                cin >> m[i][j];
            }
        }

        floyd_warshall();
        int R;
        cin >> R;
        for(int i = 0; i < R; i++){
            int a, b;
            cin >> a >> b;
            a--;
            b--;
            s += m[a][b];
        }
        cout << "Case #" << (c + 1) << ": " << s << endl; 
    }
    return 0;
}