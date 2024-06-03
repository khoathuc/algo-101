This is listing problems => think about backtracking
note that at index i: <br>

c_i: number of closes at index i <br>
o_i: number of open at index i <br>

if(o_i < c_i) => this is invalid because we can not adding more open in previous index

=> just need to check if o_i > c_i at index i, and o_i and c_i <= n