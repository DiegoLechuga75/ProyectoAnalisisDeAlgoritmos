#define S0 8
#define S1 9
#define S2 12
#define S3 11
#define salidaSensor 10
int frecuenciaRojo=0;
int frecuenciaVerde=0;
int frecuenciaAzul=0;

void setup() {
  //Salidas
  pinMode(S0,OUTPUT);
  pinMode(S1,OUTPUT);
  pinMode(S2,OUTPUT);
  pinMode(S3,OUTPUT);

  //Entrada
  pinMode(salidaSensor,INPUT);

  //escala de la Frecuencia a 20%
  digitalWrite(S0,HIGH);
  digitalWrite(S1,LOW);

  //comunicacion en serie
  Serial.begin(9600);

}

void loop() {
  //lectura de fotodiodos con filtro rojo
  digitalWrite(S2,LOW);
  digitalWrite(S3,LOW);
  //leer la frecuencia de salida del sensor
  frecuenciaRojo=pulseIn(salidaSensor,LOW);
  //mostrar el valor de rojo en la comunicación serial
  Serial.print("");
  Serial.print(frecuenciaRojo);
  Serial.print(",");
  delay(500);
  
  //lectura de fotodiodos con filtro verde
  digitalWrite(S2,HIGH);
  digitalWrite(S3,HIGH);
  //leer la frecuencia de salida del sensor
  frecuenciaVerde=pulseIn(salidaSensor,LOW);
  //mostrar el valor de verde en la comunicación serial
  Serial.print("");
  Serial.print(frecuenciaVerde);
  Serial.print(",");
  delay(500);

  //lectura de fotodiodos con filtro azul
  digitalWrite(S2,LOW);
  digitalWrite(S3,HIGH);
  //leer la frecuencia de salida del sensor
  frecuenciaAzul=pulseIn(salidaSensor,LOW);
  //mostrar el valor de azul en la comunicación serial
  Serial.print("");
  Serial.print(frecuenciaAzul);
  Serial.println("");
  delay(500);
}
