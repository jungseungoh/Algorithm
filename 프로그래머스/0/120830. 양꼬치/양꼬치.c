#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n, int k) {
    return n*12000 + (k-n/10)*2000;
}

// 10인분 먹으면 음료수 하나 서비스 제공
// 양꼬치 1인분 12000
// 음료수 2000