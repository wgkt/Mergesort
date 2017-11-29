def mergeSort(listone):
    if len(listone)>1:
        mid = len(listone)//2
        left = listone[:mid]
        right = listone[mid:]

        mergeSort(left)
        mergeSort(right)

        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                listone[k]=left[i]
                i=i+1
            else:
                listone[k]=right[j]
                j=j+1
            k=k+1

        while i < len(left):
            listone[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            listone[k]=right[j]
            j=j+1
            k=k+1

listone = [25,4,8,45,75,60,12,99,15,35]
print("List before sorting: ")
print(listone)
mergeSort(listone)
print("List after sorting")
print(listone)
