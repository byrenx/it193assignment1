def gelistintegers(file_name):
    file_content = open(file_name)
    lst = []
    for num in file_content:
        lst.append(int(num))

    file_content.close()

    return lst

def mergesort(lst):
    '''Recursively divides list in halves to be sorted'''
    if len(lst) == 1:
        return lst, 0
    middle = int(len(lst)/2)
    left, s1 = mergesort(lst[:middle])
    right, s2= mergesort(lst[middle:])
    sortedlist, s3 = merge(left, right)
    return sortedlist, (s3+s1+s2)

def merge(left, right):
    '''Subroutine of mergesort to sort split lists.  Also returns number
    of split inversions (i.e., each occurence of a number from the sorted second
    half of the list appearing before a number from the sorted first half)'''
    i, j = 0, 0
    splits = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            splits += len(left[i:])
    result += left[i:]
    result += right[j:]
    ##print result, splits
    return result, splits

if __name__ == '__main__':
    lst_contents = gelistintegers('IntegerArray.txt')
    ##print str(lst_contents[3])
    ##lst_contents = [5,4,3,2,1]
    mg_rs, split = mergesort(lst_contents)
    print "# of inversions: " + str(split)




