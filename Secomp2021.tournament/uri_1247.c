#include <stdio.h>

int main() {
    float d, vf, vg, tf, tg;

    while(scanf ("%f %f %f", &d, &vf, &vg) == 3){
        if (d == 0){
            printf('S\n');
        }
        else if (d == 12){
            printf('N\n');
        }else{
            tf = (12-d)/vf;
            tg = (12)/vg;
            printf("%c\n", (tg<=tf? 'S' : 'N'));
        }
    }
}