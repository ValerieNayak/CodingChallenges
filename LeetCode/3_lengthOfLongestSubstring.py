# Valerie Nayak
# 7/1/2020
# LeetCode: Longest substring without repeats


def lengthLongestSubstring(s):
    max_len = 0
    start = 0
    end = 0
    for index, char in enumerate(s):
        visited_chars = set()
        temp_index = index
        while temp_index < len(s) and s[temp_index] not in visited_chars:
            visited_chars.add(s[temp_index])
            temp_index += 1
        current_len = temp_index - index
        if current_len > max_len:
            start = index
            end = temp_index-1
            max_len = current_len
    print('start', start)
    print('end', end)
    print('max', max_len)
    return max_len

test_str = "abcabcbb"
print(lengthLongestSubstring(test_str))