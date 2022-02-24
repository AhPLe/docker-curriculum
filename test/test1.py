def test():
    print('in the test1')
    var_name = 'what is this\n'
    with open('temp.txt', 'a+') as file:
        file.write(var_name)
    print('final')
    return var_name