def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 0
    ##################
    # YOUR CODE HERE #
    ##################
    # track the current longest increasing subarray
    # and the length of the current increasing subarray
    longest_subarray_length = 0
    current_subarray_length = 0

    # iterate through the indices: for each i from 1 ... len(A) - 1,
    # if A[i - 1] < A[i], we're in an increasing subarray
    # increment the current subarray length by 1 (or 2 if it's 0)
    # compare to the longest subarray length: if it's >, update and set count to 1
    # if it's ==, increment count
    # if A[i - 1] >= A[i], then we're out of the subarray - set current length to 0
    for i in range(1, len(A)):
        if (A[i - 1] < A[i]):
            current_subarray_length += 2 if current_subarray_length == 0 else 1

            if (current_subarray_length == longest_subarray_length):
                count += 1
            elif (current_subarray_length > longest_subarray_length):
                longest_subarray_length = current_subarray_length
                count = 1
        else:
            current_subarray_length = 0

    return count
