
def moving_average(arr, window_size):
    i = 0
    # Initialize an empty list to store moving averages
    moving_averages = []
    # Loop through the array to consider
    # every window of size 3
    while i < len(arr) - window_size + 1:
        # Store elements from i to i+window_size
        # in list to get the current window
        window = arr[i : i + window_size]
        # Calculate the average of current window
        window_average = round(sum(window) / window_size, 2)
        # Store the average of current
        # window in moving average list
        moving_averages.append(window_average)
        # Shift window to right by one position
        i += 1
    return(moving_averages)


########### Testing

temps = [1,2,3,4,5,6,7,6,5,4,3,2,1,-20,-10,0, 5]
days = 3
print(moving_average(temps, days))
