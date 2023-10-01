# Assume the first element is the maximum
# Iterate through the elements in the array
# Update max if a larger element is found



def find_max(array):

    max=array[0]            

    for i in array:
        if i>max:
            max=i
    return max

array=[10,83,48,20,4,6,15,96]
max_value=find_max(array)
print(f"The maximum element is {max_value}")
