import array

arr = array.array('f',[99, 0, -7, 0, 16])
for i in range(len(arr)):
    print(f"{arr[i]:5} {id(arr[i])}")
