def count_pair_sums(arr, number=0):
    '''
    Given an array, find the count of how many pairs of numbers in the array sum
    to the input number

    Parameters
    ----------
    arr: {list} list of integers (positive and negative)
    number: number to see if pairs sum to (default 0)

    Returns
    -------
    {int} the number of pairs found that sum to given number
    '''
    sum_count = 0
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i] + arr[j] == number):
                sum_count = sum_count + 1
    
    return sum_count
