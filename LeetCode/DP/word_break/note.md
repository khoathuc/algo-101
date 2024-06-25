## 

res[i]: = True if s[:i + 1] can be created by using word in wordDict
=> at index i, iterate to end of index.
=> if index j can be created by using word in wordDict => update index j.

=> continue the loop with closest index that true.