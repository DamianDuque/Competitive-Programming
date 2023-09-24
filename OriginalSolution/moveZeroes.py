def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lastzero = -1
        i=0
        while i < len(nums):
            #print(nums, i)
            if nums[i] == 0:
                lastzero = i
            elif nums[i] != 0 and lastzero != -1:
                #print("cambio realizado")
                nums[i],nums[lastzero] = nums[lastzero],nums[i]
                lastzero = -1
                if i-2 >= 0:
                    i-=2
                else: i=0
                continue
            i+=1

        return nums