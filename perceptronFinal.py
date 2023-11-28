import serial
import time
import numpy as np

def hardlim(w, dato, b):
    z = w * dato
    if z.sum() + b > 0:
        return 1
    else:
        return 0
    
def perceptronFinal(dato):
    if hardlim(pesosGlobales, dato, biasGlobal) == 1:
        return "Jitomate"
    else: 
        return "Limón"
    
pesosGlobales = np.array([-0.67858583, -0.41029803,  0.9240771 ])
biasGlobal = np.array([0.67065113])

def arduino_read_data(file):
    encoding = "utf-8"
    # Iniciando la conexion serial
    arduinoPort = serial.Serial('COM7',9600,timeout=1) # Cambiar la entrada del arduino en Windows
    # arduinoPort = serial.Serial('/dev/ttyACM0',9600,timeout=1)  #Cambiar la entrada del arduino en linux
    f = open(file,"w")# Abre el archivo dependiendo del valor que se manda, nombre el archivo txt

    # Retardo para establecer la conexion serial
    time.sleep(.3)  # Retardo para leer los datos, preferentemente debe ser igual al delay del código del arduino
    index = 0
    for i in range (25):
        
        getSerialValue = arduinoPort.readline()
        stringSerialValue = getSerialValue.decode(encoding)
        #print(stringSerialValue)
        arrSerialValue = stringSerialValue.split(",")
        
        if index >= 1:
            
            arrSerialValue[2] = arrSerialValue[2].replace("\r\n", "")
            
            arrIntValues = list(map(int, arrSerialValue))
            
            print(arrIntValues)
            
            f.write(getSerialValue.decode(encoding))
                    
            print(hardlim(pesosGlobales, arrIntValues, biasGlobal))
                
            print(perceptronFinal(arrIntValues))
        
        index += 1
        
        

    # Cerrando el puerto serial
    arduinoPort.close()
    f.close()


arduino_read_data("lecturas.txt")