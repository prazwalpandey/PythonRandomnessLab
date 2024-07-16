from itertools import permutations
name = 'vodle'
perms = [''.join(i) for i in permutations(name)]
print(*perms,sep='\t')
print()
print(len(perms))
