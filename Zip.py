X=[5,10,25]
Y=['!','G','T']
Z=list(zip(X,Y))
print(Z,"\n")
A=[2,4,6,8]
B=[1,3,5,7]
for x,y in zip(A,B[::-1]):
    print(x,y)
P=["Tree","Chemistry","Math"]
Q=[470,4,13]
NewDict={Books:Pages for Books,Pages in zip(P,Q)} 
print("\n{}".format(NewDict))