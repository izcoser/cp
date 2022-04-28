#include <iostream>

/*

Hare and tortoise, Floyd's algorithm.

Problem input:
An array a with size n + 1, only numbers from 1 to n in the array.
One number in a appears twice.

Output:
Find the repeating number in a.
*/

int main(){
    int a[] {1, 5, 4, 2, 6, 8, 7, 5, 3};
    
    // First part.

    int t { a[0] }; // tortoise
    int h { a[a[0]] }; // hare

    while(t != h){
        t = a[t];
        h = a[a[h]];
    }

    // Second part.

    t = 0;
    while(t != h){
        t = a[t];
        h = a[h];
    }

    std::cout << t << std::endl;

    return 0;
}
