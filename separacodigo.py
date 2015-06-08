if __name__ == "__main__":

    direcccion="C:\Users\mary\PycharmProjects\djdoc\djwebdoc\\"
    direcccion2="C:\Users\mary\PycharmProjects\djdoc\\app6\\"

    f = open(direcccion+"app6")
    namefile="script"
    cadenaespacial ="$$$$$\n"
    contador =1


    for i in range( 0 ,7 ):
        f.readline()

    g = open(direcccion2+namefile+str(contador)+".py",'w')

    for linea in f:
        #print linearead()
        if linea==cadenaespacial:
            contador+=1
            g = open(direcccion2+namefile+str(contador)+".py",'w')
        else:
            g.write(linea)


    g.close()
    f.close()