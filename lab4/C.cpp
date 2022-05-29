#include <iostream>
#include <climits>
#include <map>
// F - Frequent Values

using namespace std;

void buildRec(int* T, int* A, int node, int start, int end) {
    if(start == end) {
        T[node] = A[start];
    } else {
        int mid = (start + end) / 2;
        buildRec(T, A, 2 * node, start, mid);
        buildRec(T, A, 2 * node + 1, mid+1, end);
        T[node] = max(T[2 * node], T[2 * node + 1]);        //# <======= IMPORTANTE
    }
}
void build(int *T, int *A, int n) {
    buildRec(T, A, 1, 0, n-1); //# A raíz tem nó 1 e representa o segmento A[0, ..., n-1]
}

int queryRec(int *T, int node, int start, int end, int l, int r) {
    if(r < start or end < l) {
        return 0;                                       //# <======= IMPORTANTE
    }
    if(l <= start and end <= r){
        return T[node];
    }
    int mid = (start + end) / 2;
    int p1 = queryRec(T, 2 * node, start, mid, l, r);
    int p2 = queryRec(T, 2 * node + 1, mid + 1, end, l, r);
    return max(p1, p2);                                   //# <======= IMPORTANTE
}
int query(int* T, int n, int l, int r) { //#Soma(A[l, ..., r])
    if(l > r){
        return 0;
    }
    return queryRec(T, 1, 0, n-1, l, r);
}

int main(){
    while(1){
        int N;
        cin >> N;
        if(N == 0){
            break;
        }
        int Q;
        cin >> Q;

        int A[N];
        int T[4*N];
        map<int, int> count;
        int F[N];
        for(int i = 0; i < N; i++){
            cin >> A[i];
            count[A[i]]++;
        }
        for(int i = 0; i < N; i++){
            F[i] = count[A[i]];
        }
        
        build(T, F, N);

        for(int i = 0; i < Q; i++){
            int l, r;
            cin >> l >> r;
            l--;
            r--;

            if(A[l] == A[r]){
                cout << r - l + 1 << endl;
            }

            else{
                int c1 = 1;
                while(A[l] == A[l + 1]){
                    c1++;
                    l++;
                }
                l++;

                int c2 = 1;
                while(A[r] == A[r - 1]){
                    c2++;
                    r--;
                }
                r--;
                cout << max(max(c1, c2), query(T, N, l, r)) << endl;
            }
        }
    

    }

    return 0;
}
