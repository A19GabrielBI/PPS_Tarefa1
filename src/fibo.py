def fibonacci(pos: int) -> int:
    first = 0
    second = 1
    posCounter = 1
    while posCounter < pos:
        second += first
        first = second - first
        posCounter += 1
    return first