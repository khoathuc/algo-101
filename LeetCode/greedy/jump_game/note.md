### Naive solution
TODO: explain this !!
```python
        def solve(self):
        global arr
        
        tmp:List[int] = []
        for i, val in enumerate(arr):
            tmp.append(val + i)

        def furthest(index):
            nonlocal tmp
            _max = tmp[index]
            for i in range (index + 1, tmp[index] + 1):
                if(i < len(tmp)):
                    _max = max(_max, furthest(i))
                    
            return _max
            
        return furthest(0) >= len(arr) - 1
        pass

```


### Use visited list to store the furthest of index i.
```python
    def solve(self):
        global arr
        
        tmp:List[int] = []
        visited: List[int] = [False] * len(arr)
        for i, val in enumerate(arr):
            tmp.append(val + i)

        target = len(tmp) - 1
        def furthest(index):
            nonlocal tmp
            nonlocal target
            nonlocal visited

            if(visited[index]):
                return visited[index]
            
            if(index >= target):
                return target
            
            _max = tmp[index]
            for i in range (index + 1, tmp[index] + 1):
                if(i < target):
                    _max = max(_max, furthest(i))

                        
            
            visited[index] = _max
            return _max
            
        print(furthest(0) > target)
        pass
```

### Store the furthest by using reachable.

