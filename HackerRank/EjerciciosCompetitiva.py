from collections import Counter

def pickingNumbers(a):
    # Write your code here
    arr = Counter(a)
    print(arr)
    maxnumber = 0
    for i in range(100):
        print(i)
        print(arr[i], arr[i+1])
        maxnumber = max(maxnumber, arr[i]+arr[i+1])



def findMedian(arr):
    # Write your code here
    arr = sorted(arr)
    print(arr)
    if len(arr)%2 != 0:
        return arr[(len(arr)//2)]
    else:
        return (arr[(len(arr)//2)] + arr[(len(arr)//2)+1])/2
    


def flatlandSpaceStations(n, c):
    c = sorted(c)
    if len(c) == n:
        return 0
    maxdis = 0
    for i in range(0,len(c)-1):
        tempdis = (c[i+1] - c[i])//2
        maxdis = max(maxdis, tempdis)
        
    maxdis = max(maxdis, c[0], n-1 - c[-1])
    return maxdis
    


def topView(root):
    #Write your code here
    #Create dict
    d = {}
    
    def traverse(root,key,level):
        if root:
            # check if Key not present in dict
            if key not in d:
                d[key] = [root,level]
            
            # Key with lesser level
            elif d[key][1] > level:
                d[key] = [root,level]
                
            # Traverse to left and rigth of tree
            traverse(root.left, key-1, level+1)
            traverse(root.right, key+1, level+1)
            
    traverse(root,0,0)
    # Print elements in order
    for key in sorted(d):
        print(d[key][0], end=" ")



def largestRectangle(h):
    stack = []
    area = i = 0
    h.append(0)
    print(h)
    # main logic
    while i < len(h):
        # Stack is empty or greater heigth is found
        if stack:
            print("la altura es:" + str(h[stack[-1]]))
        print("la altura siguiente es:" + str(h[i]))
        print(not stack or h[stack[-1]] < h[i])
        if not stack or h[stack[-1]] < h[i]:
            stack.append(i)
            i+=1
            
        # if height is lesser
        else:
            top = stack.pop()
            area = max(area, h[top]* (i-stack[-1]-1 if stack else i))
        
    return area