import itertools

g = list(itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=2))
alpha = []
for k in g:
    p = k[0] + k[1]
    alpha.append(p)
new_alpha = " ".join([str(a) for a in alpha])
print (new_alpha)
