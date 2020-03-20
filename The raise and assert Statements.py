def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1.')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

boxPrint('*', 20, 5)
