def finder(arr1,arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1,arr2):
        if num != num2:
            return num1

    return arr1[-1]


if __name__ == '__main__':
        print(finder([a,b,c,d],[a,c,g,s]))

