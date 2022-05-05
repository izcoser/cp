#include <iostream>
#include <string>

// I - Calculator Conundrum
//

int main(){
	int t;
	std::cin >> t;
	for(int i = 0; i < t; i++){
		int n, k;
		std::cin >> n;
		std::cin >> k;

		long long int a = k;
		long long int b = std::stoll(std::to_string(k * k).substr(0, n));
		long long int max = std::max(a, b);

		while(a != b){
			a = std::stoll(std::to_string(a * a).substr(0, n));
			b = std::stoll(std::to_string(b * b).substr(0, n));
			b = std::stoll(std::to_string(b * b).substr(0, n));
			long long int temp = std::max(a, b);
			if(temp > max){
				max = temp;
			}
		}
		std::cout << max << std::endl; 
	}
	return 0;
}
