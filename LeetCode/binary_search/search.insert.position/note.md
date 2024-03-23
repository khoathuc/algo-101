### There are 2 ways to caculate the mid point.

```
    mid = (l + r)/2
```

Or 
```
    mid = l + (r - l)/2
```


The second solution is better because it can reduce the risk of interger overflow.



### Return l?

We return most left index because by the time l > r, l is larger than the length of array.

So l is the index that the "target" should be inserted.