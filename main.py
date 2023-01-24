numList = [12, 2, 56, 34, 45, 23, 35, 64, 67, 8, 55, 6, 3, 4, 5]

user = int(input('Enter the number you want to search: '))

position = ""

for i in range(len(numList)):
    if user == numList[i]:
        position = str(i)

if user in numList:
    if '0' in position:
        print('Your number', user, 'is present in the index', str(int(position) + 1) + 'st' + ' of the list.')
    elif '1' in position:
        print('Your number', user, 'is present in the index', str(int(position) + 1) + 'nd' + ' of the list.')
    elif '2' in position:
        print('Your number', user, 'is present in the index', str(int(position) + 1) + 'rd' + ' of the list.')
    else:
        print('Your number', user, 'is present in the index', str(int(position) + 1) + 'th' + ' of the list.')
else:
    print('Your number', user, 'is not present in the list.')
