greeting = 'Hello World'
print(greeting) 

age = 34
isHappy = False

if age > 21:
    print('You are an adult')
elif age == 18:
    print('You are a minor')
else:
    print('You are a child')

if isHappy:
    print('You are happy')
else:
    print('You are not happy')

for i in range(5):
    print('Hello', i)

for i in range(3):
    print('Hey', i + 1)

print(range(3))

# while loop
while age < 40:
    print('You are still young')
    age += 1

while True:
    user_input = input('Enter something:')
    if user_input == '0':
        print('We are done here. Goodbye!')
        break