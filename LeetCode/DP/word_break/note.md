## 

res[i]: = True if s[:i+1] can be make with word in wordDict.
if(res[i] == true):
    for each word in wordDict.
    => concat res[i] with word (=tmp)
    if tmp == s[:i+len(word)]:
    => res[i+len(word)] == True.