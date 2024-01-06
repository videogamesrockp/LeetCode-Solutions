import math

class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        neg = False
        if x[0] == "-":
            neg = True

        if neg:
            x = x[1:]

        x = x[::-1]

        if neg:
            x = "-" + x

        x = int(x)
        
        if x > math.pow(2, 31) - 1:
            return 0
        elif x < -math.pow(2, 31):
            return 0
        else:
            return x
