#TAGS: BS
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #Step 1: Find the pivot
        l, r = 0, len(nums)-1

        if nums[0]>nums[-1]:

            while(l<=r):
                mid = (l+r)>>1
                if nums[0]<=nums[mid]:
                    l=mid+1
                elif nums[0]>nums[mid]:
                    r=mid-1
            
            pivotIDX = max(l,r)

            #Step 2: Find the start location to do binary search           
            if nums[0]<=target<=nums[pivotIDX-1]:
                l, r = 0, pivotIDX-1
            elif nums[pivotIDX]<=target<=nums[-1]:
                l, r = pivotIDX, len(nums)-1
            else:
                return(-1)


        #Step 3: Do the ordinary BS
        while (l<=r):
            mid = (l+r)>>1
            if nums[mid]<target:
                l = mid+1
            elif nums[mid]>target:
                r = mid-1
            else:
                return(mid)
        
        return(-1)


        



