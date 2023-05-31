# def find_peaks(arr):
#     peaks = []
#     n = len(arr)
#     find_peaks_recursive(arr, 0, n - 1, peaks)
#     return peaks
#
# def find_peaks_recursive(arr, start, end, peaks):
#     if start > end:
#         return
#
#     mid = (start + end) // 2
#
#     # Check if mid element is a peak
#     if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]):
#         peaks.append(arr[mid])
#
#     # Recursively search in the left and right halves
#
#     find_peaks_recursive(arr, start, mid - 1, peaks)
#
#
#     find_peaks_recursive(arr, mid + 1, end, peaks)
#
# # Example usage:
# array = [1,2]
# peaks = find_peaks(array)
#
# if peaks:
#     print("Peaks found:", peaks)
# else:
#     print("No peaks found in the array.")

def findPeakElement(nums) -> int:
    start = 0
    end = len(nums) - 1

    if len(nums) == 1:
        return 0

    while start <= end:
        if start == end:
            return end
        mid = int((start + end) / 2)
        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid
        if mid>0 and nums[mid] < nums[mid - 1]:
            end = mid - 1
        elif mid==0 and nums[mid] > nums[mid + 1] :
            return mid
        elif mid < end and nums[mid]<nums[mid+1]:
            start = mid+1

print(findPeakElement([1,2]))