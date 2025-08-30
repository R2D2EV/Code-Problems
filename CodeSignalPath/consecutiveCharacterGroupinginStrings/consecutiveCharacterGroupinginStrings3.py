# n this task, you need to write a Python function that finds repeating two-character patterns in a string. The function should identify when the same pair of characters appear next to each other in the string and count how many times each pair repeats consecutively.
# The function should return a new string that lists each pair followed by the number of times it repeats consecutively. For example, let's break down the input string "aaabbabbababacab":
# Divide the string into pairs:

# "aa"
# "ab"
# "ba"
# "bb"
# "ab"
# "ab"
# "ac"
# "ab"
# Note the consecutive pairs:

# "ab" appears twice consecutively in the middle.
# Therefore, the output string will be: "aa1ab1ba1bb1ab2ac1ab1".

# Similarly, for the input string "aaababbababaca", the output should be "aa1ab2ba3ca1".

# Key points to remember:

# The input string always has an even number of characters.
# The string contains only lowercase letters.
# The string length can be up to 500 characters.
# Focus on finding consecutive repetitions of the same two-character patterns.

def solution(s):
    result = []
    i = 0
    while i < len(s) - 1:
        pair = s[i:i+2]
        count = 1
        while i + 2 < len(s) and s[i:i+2] == s[i+2:i+4]:
            count += 1
            i += 2
        result.append(f"{pair}{count}")
        i += 2
    return ''.join(result)
