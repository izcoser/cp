#include <iostream>
#include <climits>

// D - Maximum Sum
// Use a max Seg Tree.
// To find the maximum and second maximum numbers in a range,
// we need to store both the maximum value and the index of the maximum value
// in our Segment Tree. That way we can find the maximum M in the entire range,
// and the second maximum M2, by querying the space before M and after M.

using namespace std;

typedef pair<int, int> pint;
void buildRec(pint* T, int* A, int node, int start, int end) {
    if(start == end) {
        T[node] = pint(A[start], start);
    } else {
        int mid = (start + end) / 2;
        buildRec(T, A, 2 * node, start, mid);
        buildRec(T, A, 2 * node + 1, mid+1, end);
        T[node] = max(T[2 * node], T[2 * node + 1]);        //# <======= IMPORTANTE
    }
}
void build(pint *T, int *A, int n) {
    buildRec(T, A, 1, 0, n-1); //# A raíz tem nó 1 e representa o segmento A[0, ..., n-1]
}

pint queryRec(pint *T, int node, int start, int end, int l, int r) {
    if(r < start or end < l) {
        return pint(INT_MIN, INT_MIN);                                       //# <======= IMPORTANTE
    }
    if(l <= start and end <= r){
        return T[node];
    }
    int mid = (start + end) / 2;
    pint p1 = queryRec(T, 2 * node, start, mid, l, r);
    pint p2 = queryRec(T, 2 * node + 1, mid + 1, end, l, r);
    return max(p1, p2);                                   //# <======= IMPORTANTE
}
pint query(pint* T, int n, int l, int r) { //#Soma(A[l, ..., r])
    return queryRec(T, 1, 0, n-1, l, r);
}

void updateRec(pint* T, int* A, int node, int start, int end, int idx, int val) {
    if(start == end) {
        A[idx] += val;
        T[node].first += val;
    } else {
        int mid = (start + end) / 2;
        if(start <= idx and idx <= mid) {
            updateRec(T, A, 2 * node, start, mid, idx, val);
        } else {
            updateRec(T, A, 2 * node + 1, mid + 1, end, idx, val);
        }
        T[node] = max(T[2 * node], T[2 * node + 1]);        //# <======= IMPORTANTE
    }
}
void update(pint *T, int *A, int n, int idx, int val) { //# A[idx] = A[idx] + val
    updateRec(T, A, 1, 0, n - 1, idx, val);
}

void set(pint *T, int *A, int n, int idx, int val){ // A[idx] = val
    update(T, A, n, idx, val - A[idx]);
}

int main(){
    int N;
    cin >> N;
    int A[N];
    pint T[4*N];
    for(int i = 0; i < N; i++){
        cin >> A[i];
    }
    
    build(T, A, N);

    int Q;
    cin >> Q;
    for(int i = 0; i < Q; i++){
        char op;
        int a, b;
        cin >> op >> a >> b;
        if(op == 'Q'){
            int idmax1 = query(T, N, a - 1, b - 1).second;

            int max2 = INT_MIN;
            if(idmax1 != a - 1){
                max2 = query(T, N, a - 1, idmax1 - 1).first;
            }
            int max3 = INT_MIN;
            if(idmax1 != b - 1){
                max3 = query(T, N, idmax1 + 1, b - 1).first;
            }
            cout << A[idmax1] + max(max2, max3) << endl;
        }
        else{
           set(T, A, N, a - 1, b);
        }

    }
    return 0;
}
