#include <stdio.h>
#define ULL unsigned long long int

int main(){
    int t;
    scanf("%d\n", &t);
    for(int k = 0; k < t; k++){
        int n;
        int p;
        scanf("%d\n", &n);
        scanf("%d\n", &p);
        int ns[p];
        for(int j = 0; j < p; j++){
            scanf("%d", &ns[j]);
        }

        int found = 0;
        for(ULL i = 0; i < (1LLU << p); i++){
            int sum = 0;
            for(int  j = 0; j < p; j++){
                if(i & (1 << j)){
                    sum += ns[j]; 
                }
            }
            if(sum == n){
                found = 1;
                break;
            }
        }

        if(found){
            printf("YES\n");
        }
        else{
            printf("NO\n");
        }
    }
    return 0;

}
