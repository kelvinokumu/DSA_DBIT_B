def selection_sort(unsorted_list):
    number_of_elements = len(unsorted_list)
    
    for outerloop in range(number_of_elements):
        minimum_index = outerloop
        for innerloop in range(outerloop + 1, number_of_elements):
            # find the smallest value
            if unsorted_list[innerloop] < unsorted_list[minimum_index]:
                minimum_index = innerloop
                print(f"Minimum values is {unsorted_list[minimum_index]}")
            
        # swap the values           
        temp = unsorted_list[outerloop]
        unsorted_list[outerloop] = unsorted_list[minimum_index]
        unsorted_list[minimum_index] = temp
        
        # print(f"Values {unsorted_list}")
        
    return unsorted_list

values = [9,8,7,6,5,4,3,2,1]
print(f"Before sorting {values}")

sorted_values = selection_sort(values)
print(f"Before sorting {sorted_values}")
