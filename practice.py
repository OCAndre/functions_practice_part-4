def max_num(x, y, z):
    if x>y:
        if x>z:
            print(x,"is the maximum")
        else:
            print(z,"is the maximum")
    else:
        if y>z:
            print(y,"is the maximum")
        else:
            print(z,"is the maximum")

def mult_list(list):
    if len(list)==0:
        return 0
    product=list[0]
    if len(list)>1:
        for i in list[1:]:
            product=product*i
    return product



def rev_string(string):
    return string[::-1]


def num_within(num, rangeStart, rangeEnd):
    return num in range(rangeStart, rangeEnd+1,1)


def pascal(n):
    pTriangle=[[1]]
    if n<1:
        print ("Requires 1 row")
    elif n==1:
        print(pTriangle[0])
    else:
        # set starting row number
        row_num=1
        while row_num<=n:
            # current and previous row
            row=[]
            row_prev=pTriangle[row_num-1]
            for i in range(row_num):
                # rows start with 1
                if i == 0:
                    row.append(1)
                elif i> 0 and i < row_num-1:
                    row.append(pTriangle[row_num-1][i-1]+pTriangle[row_num-1][i])
                # rows end with 1
                else:
                    row.append(1)
            pTriangle.append(row)
            row_num += 1
            print(row)





        




# Test

max_num(1, 2, 3)
max_num(1, 3, 2)
max_num(2, 1, 3)
max_num(3, 1, 2)

print(mult_list([1,5,3]))

print(rev_string("Hello world!"))

print(num_within(3,1,5))
print(num_within(3,1,3))
print(num_within(1,3,5))

pascal(1)
pascal(5)