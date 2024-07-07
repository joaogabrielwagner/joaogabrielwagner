#codigo utilizado apenas para extrair a posição x,y,w,h da area dos bancos
#ao selecionar com o mouse o retangulo que desejamos, apertar 'barra de espaço' e extrair do output a posição

import cv2
import imutils
#colocando a fonte de entrada de video
video = cv2.VideoCapture(3)# colocar 0 ali da p usar webcam tbm
tracker = cv2.TrackerCSRT_create()#localizando a area selecionada
# open cv lendo a entrada de video e botando em cada variavel
check, img = video.read()
#redimensionando a janela
img = imutils.resize(img, width=1080)
bbox = cv2.selectROI('video',img,False)

tracker.init(img,bbox)

while True:
    check, img = video.read()
    img = imutils.resize(img, width=1080)
    check2,bbox = tracker.update(img)#variavel do objeto que esta detectando
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    print(x,y,w,h)#utilizado para mostrar a posição em x,y,w,h da area que desejamos
    if check2:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
    cv2.imshow('video', img)
    cv2.waitKey(10)