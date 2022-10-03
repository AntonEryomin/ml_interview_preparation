from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ocean_view = []

        smallest = -1
        for idx in range(len(heights) - 1, -1, -1):
            if heights[idx] > smallest:
                ocean_view.append(idx)
                smallest = heights[idx]

        return reversed(ocean_view)
