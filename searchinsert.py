def searchInsert(self, nums, target):
        if target not in nums:
            nums.append(target)
            nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                return i

        return -1
