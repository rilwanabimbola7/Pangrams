import itertools 

g = list(itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=2))#putting the alphabets in a list and using the itertools.product to perform combination
alpha = []#creating an empty list to append the output of the for loop
for k in g:
    p = k[0] + k[1]
    alpha.append(p)
new_alpha = " ".join([str(a) for a in alpha])#joining the member of the list into a string
print (new_alpha)
