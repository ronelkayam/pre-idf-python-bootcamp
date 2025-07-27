"""
3 options for range function
1- range(end) - from 0 to end
2- range(start,end) - from start to end
3- range(start,end,jump) - from start to end with jumping

*** end not included in range
"""

num = 10
jump = 3
print(f"range({num}): 0,1,2,3,4,5,6,7,8,9")
print(f"range(2,{num}): 2,3,4,5,6,7,8,9")
print(f"range(2,{num},{jump}): 2,5,8")