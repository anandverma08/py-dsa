def find_all_peaks_2d(array):
    rows = len(array)
    cols = len(array[0])


    def find_peaks_recursive(start_col, end_col):
        mid_col = (start_col + end_col) // 2

        # Find the maximum element in the mid_col and its corresponding row
        max_elem = max(array[row][mid_col] for row in range(rows))
        max_row = max(range(rows), key=lambda row: array[row][mid_col])

        # Check if the maximum element is a peak
        is_peak = True
        if mid_col > 0 and array[max_row][mid_col] < array[max_row][mid_col - 1]:
            is_peak = False
        elif mid_col < cols - 1 and array[max_row][mid_col] < array[max_row][mid_col + 1]:
            is_peak = False

        # List to store the peak elements
        peaks = []

        # If maximum element is a peak, add it to the list
        if is_peak:
            peaks.append((max_row, mid_col))

        # Recursively search in the left and right halves of the array
        if mid_col > start_col:
            peaks.extend(find_peaks_recursive(start_col, mid_col - 1))
        if mid_col < end_col:
            peaks.extend(find_peaks_recursive(mid_col + 1, end_col))

        return peaks

    # Start the recursive search from the entire array
    return find_peaks_recursive(0, cols - 1)
matt= [[5,1,7,9],[2,3,1,2],[1,7,4,6],[8,2,1,9]]
print(find_all_peaks_2d(matt))