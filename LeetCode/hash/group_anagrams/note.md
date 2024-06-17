## Naive
Iterate through the list, sort all string and group
```python
    def solve(self, strs: List[str])-> List[List[str]]:
        #solve here
        groups: Dict[str, List[str]] = {}
        for str in strs:
            tmp = ''.join(sorted(str))
            if( tmp in groups):
                groups[tmp].append(str)
            else:
                groups[tmp] = [str]
            
        #get result
        res: List[List[str]] = []
        for key in groups:
            res.append(groups[key])
        
        return res
```


## Innovative Methods
Iterate though the list.
But do not sort the str, save the list of number of appearance of each character, then hased it.