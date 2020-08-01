# Valerie Nayak
# 7/29/2020
# LeetCode: Roman to Integer

def romanToInt(s):
    # s is input string
    conversion = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    num = 0
    i = 0
    while i < len(s):
        if i+1 < len(s):
            if s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X'):
                num += conversion[s[i + 1]] - 1

romanToInt('x')