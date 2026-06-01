class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lef,rig=0,len(numbers)-1;
        while lef<rig:
            curr=numbers[lef]+numbers[rig]

            if curr>target:
                rig -= 1
            elif curr<target:
                lef += 1
            else:
                return [lef+1 , rig+1]
            
        