#Write an algorithm that takes an array and moves all of the zeros to the end
#preserving the order of the other elements.
#move_zeros([1, 0, 1, 2, 0, 1, 3]) 
# returns [1, 1, 2, 1, 3, 0, 0]

#MY SOLUTION
#=====================================#
def move_zeros(lst):
    
    list = []
    counter = 0
    
    for i in lst:
        if i == 0:
            counter +=1         
    for i in lst:
        if i != 0:
            list.append(i)     
 
    for i in range(counter):
        list.append(0)
    return list