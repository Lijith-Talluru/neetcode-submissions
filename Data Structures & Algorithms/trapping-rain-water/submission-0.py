class Solution:
    def trap(self, height: List[int]) -> int:
        lp, rp = 0, len(height) - 1
        l_max = r_max = 0
        water = 0

        while lp < rp:
            if height[lp] < height[rp]:
                if height[lp] >= l_max:
                    l_max = height[lp]
                else:
                    water += l_max - height[lp]
                lp += 1
            else:
                if height[rp] >= r_max:
                    r_max = height[rp]
                else:
                    water += r_max - height[rp]
                rp -= 1

        return water