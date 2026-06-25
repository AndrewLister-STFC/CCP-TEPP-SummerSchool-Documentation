def myfun(*args):
    var1 = 0
    for var2 in range(args[0]):
        var3 = args[1][var2] - args[2][var2]
        var1 += var3 * var3 / args[0]
    return sqrt(var1)
