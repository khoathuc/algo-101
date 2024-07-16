# Binary search

We use binary search to search for first index that nums[index] > nums[index+1]

l, r = 0, len(nums)

mid = (l + r)/2

if(nums[mid] > nums[r]) => index is on the right side => l = mid

else r = mid