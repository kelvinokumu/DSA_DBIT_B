def find_maximum(values):
    max = values[0]
    for i in values:
        if i > max:
            max = i
            
    return max
    
    



values = [9,8,7,6,5,4,3,2,1]
ans = find_maximum(values)
print(f"Min is {ans}")



