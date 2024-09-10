digite = input('Digite algo: ')

print('Você digitou: {} você digitou algo do tipo {}, ele pode ser número: {}, pode ser letra: {}, ele pode ser os dois: {}'.format(digite, type(digite).__name__, digite.isnumeric(), digite.isalpha(), digite.isalnum()))