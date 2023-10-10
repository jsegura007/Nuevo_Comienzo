from PIL import Image

# Cargar la imagen
image_1 = Image.open("C:\\Users\\Persu_007\\Documents\\hacha.jpg")
image_2 = Image.open("C:\\Users\\Persu_007\\Documents\\pistola.jpeg")
image_3 = Image.open("C:\\Users\\Persu_007\\Documents\\dia o noche.jpg")
image_4 = Image.open("C:\\Users\\Persu_007\\Documents\\cocodrilo.jpeg")
image_5 = Image.open("C:\\Users\\Persu_007\\Documents\\sin_mano.jpeg")
image_6 = Image.open("C:\\Users\\Persu_007\\Documents\\pie.jpeg")
#variable_de_arma = "hacha"
#print(variable_de_arma)

print("Si vas caminando y te encuentras un hacha y una pistola, ¿cuál de las dos eliges? Solo puedes llevar una.")

arma = input("Selecciona 'hacha' o 'pistola': ")

if arma == "1":
    print("###############################")
    print("### Has elegido un Hacha !!! ##")
    print("###############################")
    image_1.show()
    print("")
    print("#########################################################1#############################################################################################################################")
    print("# Hay 2 caminos a seguir en tu ruta al trabajo, el primero es de día pero llueve tanto que hay peces y cocodrilos (1), el segundo es de noche y hay muchos ladrones y serpientes (2) ###")
    print("######################################################################################################################################################################################")
    
    image_3.show()
    camino = input("Elige tu camino (1 para día y 2 para la noche): ")
   

    if camino == "1":
        print("Elegiste el camino de día con peces y cocodrilos. Luchaste contra ellos pero PERDISTE EL HACHA Y UNA MANO.")
        image_5.show()



    elif camino == "2":
        print("Elegiste el camino de noche con ladrones y serpientes. Luchaste contra ellos pero no podías ver bien y te apuñalaron en el pie y PERDISTE EL HACHA.")
        image_6.show()
    
elif arma == "2":
    print("#################################")
    print("## Has elegido una pistola !!!  #")
    print("#################################")
    print("")
    image_2.show()
    print("##########################################################################################################################################")
    print("#Hay 2 caminos a seguir en tu ruta al trabajo, el primero es de día pero llueve tanto que hay peces y cocodrilos (1), el segundo es de noche y hay muchos ladrones y serpientes (2)####")
    print("########################################################################################################################################")
    
    image_3.show()
    camino = input("Elige tu camino (1 para día y 2 para la noche): ")
    

    if camino == "1":
        print("Elegiste el camino de día con peces y cocodrilos. Luchaste contra ellos y se acabaron las balas, entonces te comieron un brazo.")
    
    elif camino == "2":
        print("Elegiste el camino de noche con ladrones y serpientes. Luchaste contra ellos pero se te cayó el arma y no podías ver por la oscuridad, entonces te rompieron una pierna.")

else:
    print("Si este no es tu camino, ¡vete! ...")
