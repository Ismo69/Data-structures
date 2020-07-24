
import numpy 
import time



def binary_search(arr, target):
    high = (len(arr) - 1)
    low = 0
    while low <= high and target >= arr[low] and target <= arr[high]:

        pos = int((low + high)/ 2)
        
        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1;
        else:
            high = pos - 1;
    
    return "does not belong to this sequence"

def interp_search(arr, target):
    high = (len(arr) - 1)
    low = 0
    while low <= high and target >= arr[low] and target <= arr[high]:

        pos = low + int(((( arr[high] - arr[low])) * ( target - arr[low]))/float(high - low))

        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1;
        else:
            high = pos - 1;
    
    return "does not belong to this sequence"




def main():

    seq = numpy.random.randint(1,32767, 5000)
    
    start_time_BS = time.clock()
    binary_search(seq, 9)
    end_time_BS = time.clock()


    
    
    start_time_IS = time.clock()
    interp_search(seq, 9)
    end_time_IS = time.clock()

 

    millisecs1 = (end_time_IS - start_time_IS) * 1000
    print("The time taken im milliseconds to complete the interpolation search is %.12f" % millisecs1)

    millisecs2 = (end_time_BS - start_time_BS) * 1000
    print("The time taken in milliseconds to complete the binary search is %.12f" % millisecs2)

if __name__ == "__main__":
    main()
