def magic_square (n):
    if(n%2==0):
        print("magic sqares only work for odd numbers")
        return
    
    magic = [[0 for _ in range (n)]for _ in range (n)]
    num = n*n
    count = 1

    i = n//2
    j = n-1

    while(count<num+1):
        if (i<0):
            if(j<n):
                i=n-1
            else:
                i=0
                j=n-2
        else:
            if(j==n):
                j=0
            else:
                if(magic[i][j] != 0): 
                    i=i+1
                    j=j-2   
                else:
                    magic[i][j]=count
                    count+=1
                    i -= 1
                    j += 1
    for i in magic :
        for j in i :
            print(j, end="\t")
        print()

print("****  magic sqare of n*n ****")
n=int(input("write the dimention of matrix"))

magic_square(n)