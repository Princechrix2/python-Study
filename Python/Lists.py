
numbers = [3, 5, 6, 2, 9, 1, 4]
names = ['john', 'prince', [1,2,3,4], 'eric', 'nkaka', 'fabrice', 'anne', 'tonm']

for idx,name in enumerate(names,start=1):
    print("my name is {} on index {}".format(name,idx))
names.extend(numbers) 
