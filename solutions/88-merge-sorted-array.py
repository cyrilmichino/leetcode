def merge(nums1, m, nums2, n):
        i = 0
        j = 0
        while j < n:
            if nums1[i] > nums2[j]:
                nums1 = nums1[:i] + [num2[j]] + nums1[i:]
                print(nums1)
                j += 1
            i += 1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

merge(nums1,3,nums2,3)
print(nums1)