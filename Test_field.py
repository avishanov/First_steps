# practice 3.4
guests = ['Julius Caesar', 'John Wayne', 'William Munny']
invitation = 'приглашен на обед'
print(f'{guests[0]} {invitation}')
print(f'{guests[1]} {invitation}')
print(f'{guests[2]} {invitation}')
# practice 3.5
print(f'{guests[2]} не сможет прийти на обед')
guests[2] = 'Chingachgook'
print(f'{guests[0]} {invitation}')
print(f'{guests[1]} {invitation}')
print(f'{guests[2]} {invitation}')
# practice 3.6
print('список гостей расширен на три человека')
guests.insert(0, 'Predator')
guests.insert(2,'Alien')
guests.append('Terminator')
print(guests)
print(f'{guests[0]} {invitation}')
print(f'{guests[1]} {invitation}')
print(f'{guests[2]} {invitation}')
print(f'{guests[3]} {invitation}')
print(f'{guests[4]} {invitation}')
print(f'{guests[5]} {invitation}')
# practice 3.7
print('на обед приглашаются тлько два гостя')
del_guest = guests.pop()
print(f'{del_guest} сожалею об отмене приглашения' )
del_guest = guests.pop()
print(f'{del_guest} сожалею об отмене приглашения' )
del_guest = guests.pop()
print(f'{del_guest} сожалею об отмене приглашения' )
del_guest = guests.pop()
print(f'{del_guest} сожалею об отмене приглашения' )
print(f'{guests[0]} ранее приглашение остается в силе')
print(f'{guests[1]} ранее приглашение остается в силе')
del guests[0]
del guests[0]
print(guests)


