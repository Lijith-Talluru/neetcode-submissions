class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        value = int("".join(map(str, digits)))
        value+=1
        return [ int(d) for d in str(value)]
        
        