import cv2
import os
import imutils

# Nombre de la persona a capturar
personName = 'Bismar'
dataPath = 'E:/P.D.Imagenes/CARPETA DEL PROYECTOI/fotos' # Cambia a la ruta donde hayas almacenado Data
personPath = os.path.join(dataPath, personName)

# Crear la carpeta si no existe
if not os.path.exists(personPath):
    print('Carpeta creada:', personPath)
    os.makedirs(personPath)

# Inicializar la cámara
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Clasificador de rostros
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Redimensionar el frame para una mejor visualización
    frame = imutils.resize(frame, width=640)
    
    # Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()

    # Detectar rostros
    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Dibujar un rectángulo alrededor del rostro detectado
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Extraer el rostro y redimensionarlo
        rostro = auxFrame[y:y + h, x:x + w]
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
        
        # Guardar la imagen del rostro
        cv2.imwrite(os.path.join(personPath, 'rostro_{}.jpg'.format(count)), rostro)
        count += 1
    
    # Mostrar el frame con los rostros detectados
    cv2.imshow('frame', frame)

    # Salir del bucle si se presiona 'ESC' o se capturan 300 rostros
    k = cv2.waitKey(1)
    if k == 27 or count >= 300:
        break

# Liberar la cámara y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
