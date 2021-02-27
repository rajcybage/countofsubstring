#version 1.0 Rajarshi
def count_substring(string, sub_string):
    k=len(string)
    m=len(sub_string)
    i=0
    l=0
    count=0
    while l<k:
        if string[l:l+m]==sub_string:
            count=count+1
        l=l+1
    return count


def removal_ch(x):
    new_x=""
    for i in range(len(x)): 
        if i != 2: 
            new_x = new_x + x[i]
    
    return new_x

	
stra=input()
#stra="2 aaaa aa"
p,x,y = stra.split(" ")
p=int(p)
count = 0

for i in range(len(x)):
     if(count_substring(x, y) != p):
         x = removal_ch(x)
         count += 1
     else:
        print(str(count))
        break

#print(count_substring(x, y))
