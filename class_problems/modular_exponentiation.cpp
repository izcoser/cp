#include<iostream>

/*
Problem: given A, B and C non negative integers, calculate A^B mod C.
Solution: you can't use pow(A, B) or a loop like expMod1() because the result will quickly extrapolate even 64 bit integers.
We must use the property: (A * B) mod C = (A mod C * B mod C) mod C.
*/


using namespace std;


// Naive approach.
int expMod1(int A, int B, int C) {
    int r = A;
    for (int i = 0; i < B - 1; i++)
      r *= A;
    return r % C;
}

// O(B) multiplications and mod. Still not good enough.
int expMod2(int A, int B, int C) {
    int r = A % C;
    for (int i = 0; i < B - 1; i++) {
      r = (r * (A % C)) % C;
    }
    return r;
} 

// O(lg B) operations. Best approach.
int expMod3(int A, int B, int C) {  
  if (B == 0) 
    return 1;
  int y = expMod3(A, B / 2, C); 
  return ((y % C) * (y % C) * (B % 2? A % C: 1)) % C;
}

int main() {
    cout << expMod1(5, 200000, 11) << endl; //# wrong
    cout << expMod2(5, 200000, 11) << endl; //# ok, but slow
    cout << expMod3(5, 200000, 11) << endl; //# ok and fast =)

    return 0;
}
