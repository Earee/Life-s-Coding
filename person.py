persons = [
    ['egoing', 'Seoul', 'Web'],
    ['basta', 'Seoul', 'IOT'],
    ['blackdew', 'Tongyeong', 'ML'],
]

person = ['egoing', 'Seoul', 'Web']
name = person[0]
address = person[1]
interest = person[2]

 
name, address, interest = ['egoing', 'Seoul', 'Web']

 
for name, address, interest in persons:
    print(name+','+address+','+interest)