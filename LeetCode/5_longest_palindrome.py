# Valerie Nayak
# 7/28/2020
# LeetCode Longest Palindrome

# not fully done, but changes to make should be checking for palindromes of both even and odd length

def longestPalindrome(s):
    if len(s) < 3:
        if len(s) < 2:
            return s
        if s[0] == s[1]:
            return s
        return s[0]
    
    long_pal = ''
    front = 0
    back = 0
    for mid_ind in range(1, len(s)-1):
        mid_ind2 = None
        if s[mid_ind + 1] == s[mid_ind] and s[mid_ind - 1] != s[mid_ind]:
            mid_ind2 = mid_ind + 1
        elif s[mid_ind - 1] == s[mid_ind] and s[mid_ind + 1] != s[mid_ind]:
            if mid_ind == 1:
                mid_ind = 0
                mid_ind2 = 1
            else:
                continue
        if mid_ind2 is not None:
            front = mid_ind2 + 1
            back = mid_ind -1
        else:
            front = mid_ind + 1
            back = mid_ind - 1
        print('mid', mid_ind)
        while front < len(s) and back >= 0 and s[front] == s[back]:
            print('front', front)
            print('back', back)
            front += 1
            back -= 1
        pal = s[back+1 : front]
        if len(pal) > len(long_pal):
            long_pal = pal
    return long_pal

s = 'aaaa'
print(longestPalindrome(s))