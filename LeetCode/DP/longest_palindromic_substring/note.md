## Naive ways
- Find all substring and check if that string is palindromic

=> Find all substring: $O(n^2)$ <br>
=> Check if the string is palindromic: Iterate through all character => O(n)

=> Big O Notation $O(n^3)$


## Expand from an index

- Expand left and right from an index. 
- We need to separate into 2 cases: odd length and even length.
=> if (s[i-k] == s[i+k]) and s[i-k+1: i+k] is a palindromic, then s[i-k::i+k+1] is a palindromic <br>
For example: String: ``abcba`` <br>
- Check index = 0 a => pld(palindromic substring) is a <br>
- Check index = 1 => expand to left and right => pld is b <br>
- Check index = 2 => expand to left and right => pld is bcb, then abcba <br>

```python
    ##Expand way
    #Odd palindromic substring(plds)
    longest_odd_plds = ""
    for i,char in enumerate(s):
        l, r = i-1, i + 1
        plds = char
        while l >= 0 and r < len(s):
            if(s[l] == s[r]):
                plds = s[l:r+1]
                #update left and right
                l-=1
                r+=1
            else:
                break
        longest_odd_plds = plds if (len(plds) > len(longest_odd_plds)) else longest_odd_plds 
    
    #Even palindromic substring(plds)
    longest_even_plds = ""
    for i,char in enumerate(s):
        l, r = i, i + 1
        plds = ""
        while l >= 0 and r < len(s):
            if(s[l] == s[r]):
                plds = s[l:r+1]
                #update left and right
                l-=1
                r+=1
            else:
                break
        longest_even_plds = plds if (len(plds) > len(longest_even_plds)) else longest_even_plds 
    
    return longest_even_plds if (len(longest_even_plds) > len(longest_odd_plds)) else longest_odd_plds
```
```BigO```
Iterate through each index: O(n) <br>
Expand from index: O(n)<br>
=> O($n^2$)

## Dynamic programming