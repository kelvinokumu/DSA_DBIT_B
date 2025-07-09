def bubble_sort(unsorted_list):
    number_of_elements = len(unsorted_list)
    
    for outerloop in range(number_of_elements):
        for innerloop in range(0,number_of_elements - 1 - outerloop):
            if unsorted_list[innerloop] > unsorted_list[innerloop + 1]:
                # unsorted_list[innerloop], unsorted_list[innerloop + 1] = (
                #     unsorted_list[innerloop+1] ,unsorted_list[innerloop] 
                # )
                
                # diffrent way of swapping values
                temp = unsorted_list[innerloop]
                unsorted_list[innerloop] = unsorted_list[innerloop + 1]
                unsorted_list[innerloop + 1] = temp
                
            # inside inner loop
            # print(f"Innerloop {unsorted_list}")
            
        # inside outer loop
        print(f"Outerloop {unsorted_list}")
    return unsorted_list

values = [9,8,7,6,5,4,3,2,1]
print(f"Before sorting {values}")


sorted_values = bubble_sort(values)
print(f"Before sorting {sorted_values}")