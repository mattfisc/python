import sys
print('----')
print(sys.version)
print(sys.executable)
print('----')


def greet(who_to_greet):
    greeting = 'hello, {}'.format(who_to_greet)
    return greeting

print(greet('world'))
print(greet('matt'))
