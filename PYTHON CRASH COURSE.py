# by Eric Matthes
# PYTHON
# CRASH COURSE2ND EDITION A Hands-On, Project-Based Introduction to Programming
# practice 2.4
greeting = '«Hello Eric, would you like to learn some Python today?”'
print(greeting)
print(greeting.lower())
print(greeting.upper())
print(greeting.title())
# practice 2.5
print('Albert Einstein once said, "A person who never made \na mistake never tried anything new."')
# practice 2.6
famous_person = 'Albert Einstein'
message = 'A person who never made a mistake never tried anything new.'
print(f'{famous_person}once said,{message}')
# practice 2.7
name = "\n\t  Akhmed   "
print(name)
print(name.lstrip().rstrip().strip())
# practice 2.8
print(4 + 4)
print(12 - 4)
print(2 * 4)
print(round(16 / 2))
# practice 2.9
favorite_number = 23
print(favorite_number)
# practice 3.1
names = ['Tinky-Winky', 'Dipsy', 'Laa-Laa', 'Po']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
# practice 3.2
print(f"Hi {names[0]}, what's new?")
print(f"Hi {names[1]}, what's new?")
print(f"Hi {names[2]}, what's new?")
print(f"Hi {names[3]}, what's new?")
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
# practice 3.8
country = ['Japan', 'Canada', 'Iceland', 'Argentina', 'Poland']
print(country)
print(sorted(country))
print(country)
print(sorted(country, reverse=True))
print(country)
country.reverse()
print(country)
country.reverse()
print(country)
country.sort()
print(country)
country.sort(reverse=True)
print(country)
# practice 3.9
print(len(guests))
# practice 4.1
pizzas = ['margarita', 'pepperoni', 'pineapple']
for pizza in pizzas:
    print(f'I like {pizza} pizza')
# practice 4.1
animals = ['dog', 'cat','rat','owl']
for animal in animals:
    print(f'A {animal} would make a great pet')
print('Any of these animals would make a great pet!')
1