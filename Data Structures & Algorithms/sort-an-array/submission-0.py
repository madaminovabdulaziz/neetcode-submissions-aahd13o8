class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            # Check if left child exists and is greater than root
            if left < n and nums[left] > nums[largest]:
                largest = left

            # Check if right child exists and is greater than root
            if right < n and nums[right] > nums[largest]:
                largest = right

            # Change root, if needed
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]  # swap
                # Heapify the root.
                heapify(n, largest)

        n = len(nums)

        # Build a maxheap.
        # Start from the last non-leaf node and move upwards
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        # One by one extract elements
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]  # swap root with last element
            heapify(i, 0)

        return nums
            