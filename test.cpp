#include <iostream>

long long fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int n = 42;
    long long result = fibonacci(n);
    std::cout << "Fibonacci(" << n << ") = " << result << std::endl;
    return 0;
}