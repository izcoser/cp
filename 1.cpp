#include <iostream>
#include <math.h>

/*
Given two integers a and b, b > a,
return number of numbers between a and b
which have an odd number of divisors.

Answer: only perfect squares have an odd number of divisors.
Therefore we just need to find the number of perfect squares between a and b.

That number is just floor(sqrt(b)) - ceil(sqrt(a)) + 1.
*/

int main(){

    int a;
    int b;

    std::cin >> a;
    std::cin >> b;

    std::cout << floor(sqrt(b)) - ceil(sqrt(a)) + 1 << std::endl; 
}
