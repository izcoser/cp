#include <iostream>

// A - Potentiometers

using namespace std;

void buildRec(int* T, int* A, int node, int start, int end) {
    if(start == end) {
        //# Folha representa um elemento único 
        T[node] = A[start];
    } else {
        int mid = (start + end) / 2;
        //# Chamada recursiva para filho à esquerda 
        buildRec(T, A, 2 * node, start, mid);
        //# Chamada recursiva para filho à direita
        buildRec(T, A, 2 * node + 1, mid+1, end);
        //# Nó interno tem a SOMA dos dois filhos 
        T[node] = T[2 * node] + T[2 * node + 1];        //# <======= IMPORTANTE
    }
}
void build(int *T, int *A, int n) {
    buildRec(T, A, 1, 0, n-1); //# A raíz tem nó 1 e representa o segmento A[0, ..., n-1]
}

int queryRec(int *T, int node, int start, int end, int l, int r) {
    if(r < start or end < l) {
        //# [start, end] está fora de [l, r] -- não há interseção
        return 0;                                       //# <======= IMPORTANTE
    }
    if(l <= start and end <= r){
        //# [start, end] está contido em [l, r] 
        return T[node];
    }
    //# [start, end] e [l, r] têm interseção 
    int mid = (start + end) / 2;
    int p1 = queryRec(T, 2 * node, start, mid, l, r);
    int p2 = queryRec(T, 2 * node + 1, mid + 1, end, l, r);
    return (p1 + p2);                                   //# <======= IMPORTANTE
}
int query(int* T, int n, int l, int r) { //#Soma(A[l, ..., r])
    return queryRec(T, 1, 0, n-1, l, r);
}

void updateRec(int* T, int* A, int node, int start, int end, int idx, int val) {
    if(start == end) {
        //# Nó folha, atualiza A e T
        A[idx] += val;
        T[node] += val;
    } else {
        int mid = (start + end) / 2;
        if(start <= idx and idx <= mid) {
            //# idx está no filho à esquerda 
            updateRec(T, A, 2 * node, start, mid, idx, val);
        } else {
            //# idx está no filho à direita 
            updateRec(T, A, 2 * node + 1, mid + 1, end, idx, val);
        }
        //# Faz atualização do nó pai 
        T[node] = T[2 * node] + T[2 * node + 1];        //# <======= IMPORTANTE
    }
}
void update(int *T, int *A, int n, int idx, int val) { //# A[idx] = A[idx] + val
    updateRec(T, A, 1, 0, n - 1, idx, val);
}

void set(int *T, int *A, int n, int idx, int val){ // A[idx] = val
    //int current = query(T, n, idx, idx);
    update(T, A, n, idx, val - A[idx]);
}


int main(){
    int i = 1;
    while(1){
        int N;
        cin >> N;
        if(N == 0){
            return 0;
        }
        if(i != 1){
            cout << endl;
        }
        cout << "Case " << i << ":" << endl;
        int A[N];
        for(int i = 0; i < N; i++){
            cin >> A[i];
        }
        int T[4*N] = {0};
        build(T, A, N);

        string op;
        while(1){
            cin >> op;
            if(op.compare("END") == 0){
                break;
            }
            if(op.compare("M") == 0){
                int a, b;
                cin >> a;
                cin >> b;
                cout << query(T, N, a - 1, b - 1) << endl;
            }
            else{
                int idx, value;
                cin >> idx;
                cin >> value;
                set(T, A, N, idx - 1, value);
            }
        }

        i++;
    }
    return 0;
}
