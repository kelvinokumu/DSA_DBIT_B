def find_minimum(values):
    min = values[0]
    for i in values:
        if i < min:
            min = i
            
    return min
    
    



values = [9,8,7,6,5,4,3,2,1]
ans = find_minimum(values)
print(f"Min is {ans}")



