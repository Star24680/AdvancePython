No1=[2,4,6]
No2=[1,3,5]
Result=map(lambda x,y: x+y,No1,No2)
print("Addition of 2 lists: ")
print(list(Result))
No3=[5,10,15,20,25]
def sq(n):
    return n*n
Square=list(map(sq,No3))
print("Square of numbers in list=: ", Square)