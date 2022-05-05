#include <iostream>
#include <cmath>

// I - Calculator Conundrum
//

int main(){
	int t;
	std::cin >> t;
	for(int i = 0; i < t; i++){
		int n, k;
		std::cin >> n;
		std::cin >> k;

		long long int limit = pow(10, n) - 1;
		long long int a = k;
		long long int b = k * k;
		while(b > limit){
			b /= 10;
		}
		long long int max = std::max(a, b);

		while(a != b){
			a *= a;
			while(a > limit){
				a /= 10;
			}

			b *= b;
			while(b > limit){
				b /= 10;
			}

			b *= b;
			while(b > limit){
				b /= 10;
			}
			
			long long int temp = std::max(a, b);
			if(temp > max){
				max = temp;
			}
		}
		std::cout << max << std::endl; 
	}
	return 0;
}
