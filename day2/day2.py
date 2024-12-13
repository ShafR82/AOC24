from itertools import pairwise

def safe_report(line):
       
    pair_list_diff = [x[0]-x[1] for x in list(pairwise((line)))]
    absolute = all(1 <= abs(x) <= 3 for x in pair_list_diff)
    all_neg = all(x < 0 for x in pair_list_diff)
    all_pos = all(x > 0  for x in pair_list_diff)
    return int(absolute and (all_neg or all_pos))

def single_bad_level_idx(line):

    def helper_scan(func, l):
        for x,y in enumerate(l):
            if not func(y[0]-y[1]):
                return x,y
        return None 

    pair_list = list(pairwise((line)))
    
    if (pair_list[0][0]-pair_list[0][1] > 0):
        # all_pos = all(x > 0  for x in pair_list_diff)
        all_pos = helper_scan(lambda x : x > 0, pair_list)
        if all_pos is not None: 
            return all_pos 
    else:
        all_neg = helper_scan(lambda x : x < 0, pair_list) 
        if all_neg is not None:
            return all_neg

    absolute = helper_scan(lambda x :1 <= abs(x) <= 3, pair_list)
    if absolute is not None:
        return absolute

    return None

#main part1 
f = open("input.txt", "r")

sum = 0
for line in f:    
    sum += safe_report(map(int, line.split()))
print("part1:" +str(sum))
f.close()

#main part2 

def safe_report_with_tolerance(line):
    test = single_bad_level_idx(line)    
        
    if test is not None:
        input1 = line.copy()
        input2 = line.copy()
        input1.remove(test[1][0])
        input2.remove(test[1][1])
        return(int (safe_report(input1) or safe_report(input2)))      
    else:
        return(safe_report(line))

# input = [7,6,4,2,1] #Safe without removing any level.
# print(safe_report_with_tolerance(input))

# input = [1,2,7,8,9] #Unsafe regardless of which level is removed.
# print(safe_report_with_tolerance(input))

# input = [9,7,6,2,1] #Unsafe regardless of which level is removed.
# print(safe_report_with_tolerance(input))

# input = [1,3,2,4,5] #Safe by removing the second level, 3.
# print(safe_report_with_tolerance(input))

# input = [8,6,4,4,1] #Safe by removing the third level, 4.
# print(safe_report_with_tolerance(input))

# input = [1,3,6,7,9] #Safe without removing any level.
# print(safe_report_with_tolerance(input))

f = open("input.txt", "r")
sum = 0
for line in f:  
    line_int = list(map(int, line.split()))
    safe = safe_report_with_tolerance(line_int)    
f.close()

print("part2:"+str(sum))

# input = [61, 64, 67, 68, 69, 72, 74, 77]
# print(input)
# print(safe_report_with_tolerance(input))
# print(safe_report(input))
