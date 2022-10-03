from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = {}
        for idx in range(len(nums)):
            if nums[idx] != 0:
                self.nums[idx] = nums[idx]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_res = 0
        for k, v in self.nums.items():
            if k in vec.nums:
                dot_res += v*vec.nums[k]

        return dot_res


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

#Tests
vec_1 = SparseVector([1,0,0,2,3])
vec_2 = SparseVector([0,3,0,4,0])
assert vec_1.dotProduct(vec_2) == 8
