from collections import defaultdict, Counter


def sub(s, t):
    letters_dict = Counter(t)
    selected = defaultdict(int)
    l = 0
    best = ""
    len_of_target_sub = len(t)
    for r, char in enumerate(s):
        if char in letters_dict:
            if letters_dict[char] > 0:
                len_of_target_sub -= 1
            letters_dict[char] -= 1
            selected[char] += 1
        while len_of_target_sub == 0:
            if not best or (r - l + 1) < len(best):
                best = s[l:r + 1]


            # 2. remove s[l] from window
            letters_dict[s[l]] += 1

            selected[s[l]] -=1


            # 3. if removing it broke a requirement, increment len_of_target_sub
            if letters_dict[s[l]] > 0:
                len_of_target_sub += 1

            l += 1
    return best

print(sub("aawertyuq", "aw"))
print(sub("ADOBECODEBANC", "ABC"))