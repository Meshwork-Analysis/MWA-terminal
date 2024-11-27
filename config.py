# global pathSlug

# pathSlug = "zxc"

def AddSlug(suffix):
    # global pathSlug 
    # pathSlug = pathSlug + suffix
    # with open(f'config.txt','w') as file:
    #     for line in file:
    #        line = line + suffix
    f = open("config.txt", "r")
    temp = f.read()
    f.close()


    z = open("config.txt", "w")
    z.write(f'{temp}{suffix}')
    z.close()
    # print(f.read())


def Remove(dotdot):
    f = open("config.txt", "r")
    temp = f.read()
    f.close()

    temp = temp.replace(dotdot,'')
    

    print(temp)


    z = open("config.txt", "w")
    z.write(f'{temp}')
    z.close()



def Getpath():
    f = open("config.txt", "r")
    temp = f.read()
    f.close()

    return temp

    # with open(f'config.txt','w') as file:
    #     for line in file:
    #        line.replace(f'{dotdot}','')
    # # glob/al pathSlug
    # temp = pathSlug.replace(f'{dotdot}','')
    # pathSlug = temp




# with open(f'logs/logfile-{datetime.today().strftime('%Y-%m-%d')}.logfile','a') as file:
        # file.write(log+'\n')
# AddSlug('asdf')

# print(pathSlug)
# Remove('f')
# print(pathSlug)

