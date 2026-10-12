class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        trace={}

        for i in nums:
            trace[i]=trace.get(i,0)+1

        top=sorted (trace,key=trace.get,reverse=True)[:k]

        return top
        