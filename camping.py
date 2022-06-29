def bestSol(N,X):
   
    l=0
    for each in X:
       l=l+each
    length=l+1
    breadth=1
    perimeter=2*(length+breadth)
    return(perimeter)



result=bestSol(3,[1,1,2])
print(result)

