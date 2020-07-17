print('We can invite only 2 people')
guests = ['Jihyo', 'Momo', 'Dahyun', 'Sana', 'Mina']
print(guests[0] + ', Sorry, bye')
guests.pop(0)
print(guests[1] + ', Sorry, bye')
guests.pop(1)
print(guests[-3] + ', Sorry, bye')
guests.pop(-3)
print('Sana, ' + 'You can come')
print('Mina, ' + 'You can come')
del guests[-2]
del guests[-1]
print(guests)