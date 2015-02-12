__author__ = 'talluri'

def fastCar():
    fastcar_list = []
    for i in range(1,101):
        if i%21 == 0:
            fastcar_list.append('FastCar')
        elif i%3 == 0:
            fastcar_list.append('Fast')
        elif i%7 == 0:
            fastcar_list.append('Car')
        else:
            fastcar_list.append(i)
    return fastcar_list