class Solution:
        def maxArea(self, heights: List[int]) -> int:
                maxwat=0;
                lp,rp=0,len(heights)-1;
                while lp<rp:
                        w=rp-lp;
                        h=min(heights[lp],heights[rp])
                        curr=w*h;
                        maxwat=max(maxwat,curr);

                        if heights[lp]<heights[rp]:
                                lp+=1
                        else:
                                rp-=1
                return maxwat