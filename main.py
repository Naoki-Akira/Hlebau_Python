while True:
    try:
        num = float(input('Please, enter a number: '))
        break
    except ValueError:
        print('Invalid input. Please enter a number: ')
if num > 7:
    print('Hello')
name = input('Please, enter a name: ')
if name == 'John':
    print('Hello, John')
else:
    print('There is no such name')
arr_str = input('Please, enter a numeric array separated by spaces or commas: ')
arr_str_cleaned = arr_str.replace(',', ' ')
arr_num = [int(x) for x in arr_str_cleaned.split() if(x.lstrip('-').isdigit())]
multiples = (int(x) for x in arr_num if x % 3 == 0)
print(*multiples)