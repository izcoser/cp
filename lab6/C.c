#include <stdio.h>
#include <stdlib.h>

char out[1000005];

int main(){
    int n;
    scanf("%d", &n);
    int sa = 0;
    int sg = 0;
    for(int i = 0; i < n; i++){
        int a, g;
        scanf("%d %d", &a, &g);
        int diff_a = abs(sa + a - sg);
        int diff_g = abs(sa - (sg + g));
        if(diff_a < diff_g){
            sa += a;
            out[i] = 'A';
        }
        else{
            sg += g;
            out[i] = 'G';
        }
    }
    if(abs(sa - sg) <= 500){
        out[n] = '\0';
        printf("%s\n", out);
    }
    else{
        printf("-1\n");
    }
    return 0;
}
