# Valerie Nayak
# 8/2/2020
# LeetCode Mock Interview
# 76: Minimum Window Substring
# this was coded assuming that t doesn't have repeated characters

def minWindow(s, t):
    tchars = dict()
    small_sub = None
    for c in t:
        tchars[c] = []
    for index, c in enumerate(s):
        if c in tchars:
            tchars[c].append(index)
    print('tchars', tchars)
    
    for key in tchars:
        for start_index in tchars[key]:
            end_index = None
            found_index = False
            for letter in tchars:
                if letter == key:
                    continue
                found_index = False
                for i in tchars[letter]:
                    if i > start_index:
                        found_index = True
                        if end_index is None or i > end_index:
                            end_index = i
                        break
                if found_index == False:
                    break
            if found_index and ( small_sub is None or 1 + end_index - start_index < len(small_sub) ):
                print('start_index', start_index)
                print('end_index', end_index)
                small_sub = s[start_index : end_index + 1]
    
    if small_sub is None:
        return ""
    else:
        return small_sub

S = 'ADOBECODEBANC'
T = 'ABC'
print(minWindow(S, T))
                    