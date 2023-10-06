import random
import time

number_of_points = int(input("Please enter the number of points: "))
coordinate_list = []
Pareto_optimal_points = []

for i in range(number_of_points): #make a list with random coordinate for testing purpose.
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    coordinate_list.append([x, y])

start = time.time_ns()
def merge_sort(lst): #sortslist into two from the middle and calls the merge function for the left and right half of the list
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2 # divide the list into two equal halfs
    left_side = merge_sort(lst[:mid]) # left half of the list
    right_side = merge_sort(lst[mid:]) # right half of the list
    return merge(left_side, right_side) # call the function with left and right half.

def merge(left, right): #Sorts the smaller list and merges it into 1 whole list.
    #The x coordinate is priritiszr. if two same value for x coordinate. Then we sort based on y value
    result = []
    i = j = 0

    while i < len(left) and j < len(right): 
        if left[i][0] < right[j][0]: #compares two coordinates x values and add the point of the highest x value.
            result.append(left[i])
            i += 1
        elif left[i][0] > right[j][0]: #compares two coordinates x values and add the point of the highest x value.
            result.append(right[j])
            j += 1
        else:
            if left[i][1] < right[j][1]:# if two cordinates x values are same, comapre there y value.
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

    result += left[i:] #add remaining elements in the result list(sorted)
    result += right[j:] #add remaining elements in the result list(sorted)
    return result

sorted_points = merge_sort(coordinate_list) #use the merge sort algorithm to sort the coordinats

current_best = sorted_points[-1] # the highest x value coordinate is the first Parreto Optimal point and current best point.

Pareto_optimal_points.append(current_best) # add the current best to the solution list

for i in reversed(sorted_points): #reverse iterate the sorted list
    if i[1] > current_best[1]: # commpare the y coordinate for the current best with ith y coordinate
        Pareto_optimal_points.append(i) #if it is grater then we add it to the solution list
        current_best = i #update the current best

print(Pareto_optimal_points)
end = time.time_ns()
print(end - start)

