#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <climits>

using namespace std;

int m[100][100];
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
    string x;
    int t;
    cin >> t;
    getline(cin, x);
    for(int c = 0; c < t; c++){
        cin >> N;
        int E;
        cin >> E;
        E--;
        int T;
        cin >> T;
        int M;
        cin >> M;

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                m[i][j] = 1e8;
            }
        }

        for(int i = 0; i < M; i++){
            int a, b, w;
            cin >> a >> b >> w;
            a--;
            b--;
            m[a][b] = w;
        }

        for(int i = 0; i < N; i++){
            m[i][i] = 0;
        }

        floyd_warshall();
 
        int count = 0;
        for(int i = 0; i < N; i++){
            if(m[i][E] <= T){
                count++;
            }
        }

        cout << count << endl;
        if(c < t - 1){
            getline(cin, x);
        }
    }
    return 0;
}