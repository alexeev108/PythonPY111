def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    dict1, dict2 = {}, {}
    for i, ch in enumerate(s):
        if ch in dict1:
            dict1[ch] += 1
        else:
            dict1[ch] = 1
        if t[i] in dict2:
            dict2[t[i]] += 1
        else:
            dict2[t[i]] = 1
    return dict1 == dict2
