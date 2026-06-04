def quick_sort(list):
    if list == []:
        return []
    
    pivot = list[-1] # access the last item
    list1 = []
    list2 = []
    
    for item in list[:-1]:
        if item > pivot:
            list2.append(item)
        else:
            list1.append(item)
    
    return quick_sort(list1) + [pivot] + quick_sort(list2)

inp = input("Enter the list numbers separated by a space : ").split()
arr = [int(x) for x in inp]

print("Unsorted list is :", arr)
print("Sorted list is :", quick_sort(arr))
