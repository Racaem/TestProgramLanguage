proc fibonacci(n: int): int64 = 
    if n <= 1: 
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

var n = 42
var result = fibonacci(n)
echo "Fibonacci(" & $n & ") = " & $result