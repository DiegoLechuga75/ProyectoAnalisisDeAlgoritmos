import serial
import time
import numpy as np

def hardlim(w, dato, b):
    z = w * dato
    if z.sum() + b > 0:
        return 1
    else:
        return 0
    
pArr=np.array([[103, 69, 68],
            [103, 76, 68],
            [103, 75, 68],
            [103, 75, 68],
            [103, 75, 62],
            [103, 75, 68],
            [104, 69, 68],
            [104, 75, 68],
            [104, 75, 68],
            [103, 75, 68],
            [103, 75, 68],
            [103, 69, 68],
            [103, 75, 68],
            [103, 75, 68],
            [103, 75, 62],
            [103, 75, 68],
            [103, 69, 68],
            [103, 75, 68],
            [97, 75, 67],
            [104, 75, 68],
            [103, 75, 68],
            [104, 75, 68],
            [103, 75, 68],
            [100, 75, 68],
            
            [58, 149, 117],
            [59, 142, 117],
            [60, 147, 116],
            [60, 147, 116],
            [59, 147, 116],
            [59, 147, 117],
            [59, 147, 116],
            [59, 147, 116],
            [59, 147, 116],
            [59, 141, 116],
            [59, 141, 116],
            [59, 147, 116],
            [59, 141, 116],
            [59, 147, 119],
            [59, 147, 116],
            [59, 146, 116],
            [59, 149, 116],
            [59, 141, 116],
            [59, 147, 117],
            [59, 140, 116],
            [59, 148, 117],
            [59, 141, 116],
            [59, 147, 116],
            [59, 146, 117]])

tRes=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

response=np.array(tRes)

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
            
            pesos = np.random.uniform(-1, 1, size=3)
            bias = np.random.uniform(-1,1)
            learningRate = 0.01
            epocas = 300
            
            for epoca in range(epocas):
                totalErrors = 0
                for i in range(len(pArr)):
                    prediction = hardlim(pesos, pArr[i], bias)
                    error = response[i] - prediction
                    totalErrors += error**2
                    
                    pesos[0] += learningRate * pArr[i][0] * error
                    pesos[1] += learningRate * pArr[i][1] * error
                    pesos[2] += learningRate * pArr[i][2] * error
                    
                    bias += learningRate * error
                    
            hardlim(pesos, arrIntValues, bias)
            
            def perceptronFinal(dato):
                if hardlim(pesos, dato, bias) == 1:
                    return "Jitomate"
                else: 
                    return "Limón"
                
            print(perceptronFinal(arrIntValues))
        
        index += 1
        
        

    # Cerrando el puerto serial
    arduinoPort.close()
    f.close()


arduino_read_data("lecturas.txt")