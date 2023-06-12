def longestSubRec(s,maxed = 0):
    if len(s) >= 1:

        used = []
        for i in s:
            if i not in used:
                used.append(i)
            else:
                break
            # print(used)
            #print("first max", maxed)
        return len(used)

def lengthOfLongestSubstring(s: str, maxed=0):
    all = []
    all.append(longestSubRec(s))
    for i in range(1,len(s)-1):
        all.append(longestSubRec(s[i:]))
    if len(all) > 0:
        return max(all)
    else:
        return 0


if __name__ == '__main__':
    print(lengthOfLongestSubstring(" "))
