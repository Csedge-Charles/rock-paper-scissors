class math:
    def fac(x):
        y = x
        for i in range(x - 1):
            y -= 1
            x *= y
        return x
    def sqrt(x):
        return x ** (1 / 2)
    def log(x, base):
        if x == 1:
            return 0
        if x == base:
            return 1
        if x <= 0:
            return None
        else:
            digit_1 = 0
            digit_2 = 0
            digit_3 = 0
            digit_4 = 0
            digit_5 = 0
            digit_6 = 0
            digit_7 = 0
            while base ** (digit_1) < x:
                digit_1 += 1
            while base ** (digit_1 + (digit_2 / 10)) < x:
                digit_2 += 1
            while base ** (digit_1 + (digit_2 / 10) + (digit_3 / 100)) < x:
                digit_3 += 1
            while base ** (digit_1 + (digit_2 / 10) + (digit_3 / 100) + (digit_4 / 1000)) < x:
                digit_4 += 1
            while base ** (digit_1 + (digit_2 / 10) + (digit_3 / 100) + (digit_4 / 1000) + (digit_5 / 10000)) < x:
                digit_5 += 1
            while base ** (digit_1 + (digit_2 / 10) + (digit_3 / 100) + (digit_4 / 1000) + (digit_5 / 10000) + (digit_6 / 100000)) < x:
                digit_6 += 1
            while base ** (digit_1 + (digit_2 / 10) + (digit_3 / 100) + (digit_4 / 1000) + (digit_5 / 10000) + (digit_6 / 100000) + (digit_7 / 1000000)) < x:
                digit_7 += 1
            return (digit_1 + (digit_2 / 10) + (digit_3 / 100) + (digit_4 / 1000) + (digit_5 / 10000) + (digit_6 / 100000) + (digit_7 / 1000000))
    e = 2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932
    def ln(x):
        return math.log(x, math.e)
    def __init__(self, factorial):
        self.factorial = self.fac(factorial)
        



