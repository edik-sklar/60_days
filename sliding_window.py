from collections import defaultdict


def substring_set(s):
    seen = set()
    l = 0
    best = 0
    for r, char in enumerate(s):
        # we can remove if/else since we add char to seen regardless
        if char not in seen:
            seen.add(char)
        else:
            while char in seen:
                seen.remove(s[l])
                l += 1
            seen.add(char)
        best = max(best, r - l + 1)
    return best

def substring_dict(s):
    seen = {}
    l = 0
    best = 0
    for r, char in enumerate(s):
        if char in seen:
            l = max(l, seen[char]+1)
        seen[char] = r
        best = max(best, r-l+1)
    return best

def character_replacement(s, k):
    count = defaultdict(int)
    max_freq = 0
    l = 0
    best = 0
    for r, char in enumerate(s):
        count[char] += 1
        max_freq = max(max_freq, count[char])
        if r - l + 1 - max_freq > k:
            count[s[l]] -= 1
            l += 1
        best = max(best, r - l + 1)
    return best

s ="abcbca"

print(substring_set(s))
print(substring_dict(s))

def slide(s,k):
    seen = defaultdict(int)
    l =0
    freq = 0
    best = 0
    for r, char in enumerate(s):
        seen[char] += 1
        freq = max(freq, seen[char])
        if r-l +1 - freq > k: #maybe while?
            seen[s[l]] -= 1
            l+=1
        best = max(best,  r-l +1 )
    return best

s = "ABAB"
k = 2
print(slide(s,k))