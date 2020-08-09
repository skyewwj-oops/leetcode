from typing import List

def kmp_match_table(s: str) -> List[int]:
    res = [0] * len(s)
    j = 0
    for i in range(1, len(s)):
        while s[i] != s[j] and j != 0:
            j = res[j - 1]
        if s[i] == s[j]:
            res[i] = j + 1
            j += 1
        else:
            res[i] = 0
    return res


def kmp_partial_match_table(s: str, start: int) -> List[int]:
    # partial match: fine longest sufix starting in reverse str part
    res = [0] * len(s)
    j = 0
    for i in range(1, len(s)):
        if i == start:
            j = 0
        while s[i] != s[j] and j != 0:
            j = res[j - 1]
        if s[i] == s[j]:
            res[i] = j + 1
            j += 1
        else:
            res[i] = 0
    return res