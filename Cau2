#include <stdio.h>
#include <math.h>

// Hàm kiểm tra xem một số có phải là số chính phương hay không
int isPerfectSquare(int num) {
    int squareRoot = sqrt(num);
    return squareRoot * squareRoot == num;
}

// Hàm đếm và in ra các số chính phương nhỏ hơn n
void printPerfectSquares(int n) {
    printf("Cac so chinh phuong nho hon %d la:\n", n);
    for (int i = n - 1; i >= 1; i--) {
        if (isPerfectSquare(i)) {
            printf("%d ", i);
        }
    }
    printf("\n");
}

int main() {
    int n;
    printf("Nhap vao so nguyen duong n: ");
    scanf("%d", &n);
    printPerfectSquares(n);
    return 0;
}
