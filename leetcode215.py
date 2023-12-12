class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        #Modify this function so that it returns the range [i,j] that are correctly sorted
        def partition(low, high):

            pivot = nums[high]
            l, r = low, high
            writePointer = low

            #-------------
            #[start,writePointer-1]   nums that are < pivot
            #[writePointer,l-1]   nums that are equal pivot
            #[l,high] nums that are > pivot

            while (l<=r):
                if nums[l]<pivot:
                    nums[writePointer], nums[l] = nums[l], nums[writePointer]
                    writePointer+=1
                    l+=1
                elif nums[l]==pivot:
                    l+=1
                else: #nums[l]>pivot
                    nums[l], nums[r] = nums[r], nums[l]
                    r-=1


            #nums[writePointer],nums[high] = nums[high], nums[writePointer]
            return(writePointer,l-1)
        
        left, right = 0, len(nums)-1

        while(left<=right):

            pivotI = partition(left,right)

            if pivotI[0]<=(len(nums)-k)<=(pivotI[1]):
                return(nums[pivotI[0]])

            if pivotI[0] < len(nums)-k:
                left = pivotI[1]+1
            elif pivotI[0] > len(nums)-k:
                right = pivotI[0]-1
        
