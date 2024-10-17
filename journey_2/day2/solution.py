import math

class GCDString:
    def __init__(self):
        pass

    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    @staticmethod
    def calculate(str1, str2):
        # Check if they have non-zero GCD string.
        if str1 + str2 != str2 + str1:
            return ""

        # Get the GCD of the two lengths.
        max_length = GCDString.gcd(len(str1), len(str2))
        return str1[:max_length]