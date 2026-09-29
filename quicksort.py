def quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        # Partition the array around the pivot element
pivot_index = partition(arr, low, high)
        # Recursively sort the left and right sub-arrays
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[low]
i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
arr[i], arr[j] = arr[j], arr[i]
i += 1
arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

# Function to get user input and convert it to a list of integers
def get_user_input():
user_input = input("Enter a list of integers separated by spaces: ")
input_list = list(map(int, user_input.split()))
    return input_list

# Main code
if __name__ == "__main__":
unsorted_list = get_user_input()
sorted_list = quicksort(unsorted_list)
    print(f"Sorted list: {sorted_list}")
