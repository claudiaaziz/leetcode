class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return False





class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        # Check if the total sum is odd, in which case partitioning is not possible
        if total_sum % 2 != 0:
            return False
        
        target_sum = total_sum // 2
        
        # Define a recursive helper function to explore partition options
        def canPartitionHelper(index, remaining_sum, memo):
            if (index, remaining_sum) in memo:
                return memo[(index, remaining_sum)]
            # Base case: If remaining sum becomes 0, we found a partition
            if remaining_sum == 0:
                return True
            # Base case: If index is out of bounds or remaining sum becomes negative
            if index == len(nums) or remaining_sum < 0:
                return False
            
            # Explore two options: include current element or exclude it
            memo[(index, remaining_sum)] = canPartitionHelper(index + 1, remaining_sum - nums[index], memo) or canPartitionHelper(index + 1, remaining_sum, memo)
            return memo[(index, remaining_sum)]
        
        # Start the recursive exploration from index 0 with the target sum
        return canPartitionHelper(0, target_sum, {})