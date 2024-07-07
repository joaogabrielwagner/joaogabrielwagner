import cv2
import numpy as np
import imutils
#pegar coordenadas de cada banco com programa extrair posição
#adicionar posições(x,y,w,h) dos bancos
banco1 = [840, 650, 70, 95]
banco2 =[740, 630, 70, 95]
banco3 =[640, 620, 70, 95]
banco4 = [690, 415, 70, 95]
banco5 =[810, 430, 70, 95]
banco6 =[920, 450, 70, 95]
banco7 =[410, 550, 70, 95]
banco8 =[310, 520, 70, 95]
banco9 =[230, 490, 70, 95]
banco10 =[235, 320, 70, 95]
banco11 =[320, 340, 70, 95]
banco12 =[420, 345, 70, 95]
banco13 =[940, 360, 70, 95]
banco14 =[850, 340, 70, 95]
banco15 =[720, 320, 70, 95]
banco16 =[770, 70, 70, 95]
banco17 =[890, 110, 70, 95]
banco18 =[1000, 130, 70, 95]
banco19 =[450, 250, 70, 95]
banco20 =[340, 230, 70, 95]
banco21 =[240, 220, 70, 95]
banco22 =[295, 20, 70, 95]
banco23 =[390, 20, 70, 95]
banco24 =[490, 20, 70, 95]
#transformando cada variavel banco em uma lista
banco1_mesa1 =[banco1]
banco2_mesa1 =[banco2]
banco3_mesa1 =[banco3]
banco4_mesa1 =[banco4]
banco5_mesa1 =[banco5]
banco6_mesa1 =[banco6]
banco1_mesa2 =[banco7]
banco2_mesa2 =[banco8]
banco3_mesa2 =[banco9]
banco4_mesa2 =[banco10]
banco5_mesa2 =[banco11]
banco6_mesa2 =[banco12]
banco1_mesa3 =[banco13]
banco2_mesa3 =[banco14]
banco3_mesa3 =[banco15]
banco4_mesa3 =[banco16]
banco5_mesa3 =[banco17]
banco6_mesa3 =[banco18]
banco1_mesa4 =[banco19]
banco2_mesa4 =[banco20]
banco3_mesa4 =[banco21]
banco4_mesa4 =[banco22]
banco5_mesa4 =[banco23]
banco6_mesa4 =[banco24]
#colocando a fonte de entrada de video e a imagem do minimapa
video = cv2.VideoCapture('Câmera.mp4')#mudar aqui para camera dai botar 0 sem as aspas
imagem = cv2.imread('Minimapa.png')
# Definir limites aproximados para a cor amarelo no espaço HSV
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])
#raio do circulo do mapa, bolinha vermelha e verde
raio = 17

while video.isOpened():
    #open cv lendo a entrada de video e botando em cada variavel
    check, img = video.read()
    #se não constar video o codigo para
    if not check:
        break
    #deixar video na proporção certa, redimensionar
    img = imutils.resize(img, width=1282)
    #definindo novas variaveis auxiliares
    qtVagasAbertas = 0
    totaldebancos = 24
    gray_pixel_count_banco1_mesa1 = 0
    gray_pixel_count_banco2_mesa1 = 0
    gray_pixel_count_banco3_mesa1 = 0
    gray_pixel_count_banco4_mesa1 = 0
    gray_pixel_count_banco5_mesa1 = 0
    gray_pixel_count_banco6_mesa1 = 0
    gray_pixel_count_banco1_mesa2 = 0
    gray_pixel_count_banco2_mesa2 = 0
    gray_pixel_count_banco3_mesa2 = 0
    gray_pixel_count_banco4_mesa2 = 0
    gray_pixel_count_banco5_mesa2 = 0
    gray_pixel_count_banco6_mesa2 = 0
    gray_pixel_count_banco1_mesa3 = 0
    gray_pixel_count_banco2_mesa3 = 0
    gray_pixel_count_banco3_mesa3 = 0
    gray_pixel_count_banco4_mesa3 = 0
    gray_pixel_count_banco5_mesa3 = 0
    gray_pixel_count_banco6_mesa3 = 0
    gray_pixel_count_banco1_mesa4 = 0
    gray_pixel_count_banco2_mesa4 = 0
    gray_pixel_count_banco3_mesa4 = 0
    gray_pixel_count_banco4_mesa4 = 0
    gray_pixel_count_banco5_mesa4 = 0
    gray_pixel_count_banco6_mesa4 = 0
    #iniciando os loops para percorrer cada banco e analisa-los
    for x,y,w,h in banco1_mesa1:
        #definindo limites para analise da imagem
        recorte = img[y:y + h, x:x + w]
        #area selecionada trocada para o padrao hsv
        hsv_recorte = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
        #criando uma mascara para extrair apenas cores amarelos
        mask = cv2.inRange(hsv_recorte, lower_yellow, upper_yellow)
        #colocando quantos pixels amarelos tem na area selecionada
        gray_pixel_count_banco1_mesa1 += np.count_nonzero(mask)
        #imprime na interface da camera a quantidade de pixel amarelo
        cv2.putText(img, str(gray_pixel_count_banco1_mesa1), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255, 255, 255), 1)
        #colocando condicionais para o banco ser ocupado ou livre
        if gray_pixel_count_banco1_mesa1> 150:
            #imprime na interface da camera um retangulo vermelho
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            #imprime no minimapa um circulo vermelho
            cv2.circle(imagem, (392, 338), raio, (0, 0, 255), -1)
        else:
            #imprime na interface da camera um retangulo verde
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            #imprime no minimapa um circulo verde
            cv2.circle(imagem, (392, 338), raio, (0, 255, 0), -1)
            #adiciona no numero de vagas livres +1
            qtVagasAbertas += 1
    for x,y,w,h in banco2_mesa1:
        recorte = img[y:y + h, x:x + w]
        hsv_recorte = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_recorte, lower_yellow, upper_yellow)
        gray_pixel_count_banco2_mesa1 += np.count_nonzero(mask)

        cv2.putText(img, str(gray_pixel_count_banco2_mesa1), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255),
                    1)  # mostrando a quantidade de pixel da cor por frame
        if gray_pixel_count_banco2_mesa1> 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.circle(imagem, (342, 338), raio, (0, 0, 255), -1)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(imagem, (342, 338), raio, (0, 255, 0), -1)
            qtVagasAbertas += 1
    for x, y, w, h in banco3_mesa1:
        recorte = img[y:y + h, x:x + w]
        hsv_recorte = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_recorte, lower_yellow, upper_yellow)
        gray_pixel_count_banco3_mesa1 += np.count_nonzero(mask)

        cv2.putText(img, str(gray_pixel_count_banco3_mesa1), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255),
                    1)  # mostrando a quantidade de pixel da cor por frame
        if gray_pixel_count_banco3_mesa1> 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.circle(imagem, (292, 338), raio, (0, 0, 255), -1)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(imagem, (292, 338), raio, (0, 255, 0), -1)
            qtVagasAbertas += 1
    for x, y, w, h in banco4_mesa1:
        recorte = img[y:y + h, x:x + w]
        hsv_recorte = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_recorte, lower_yellow, upper_yellow)
        gray_pixel_count_banco4_mesa1 += np.count_nonzero(mask)

        cv2.putText(img, str(gray_pixel_count_banco4_mesa1), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255),
                    1)  # mostrando a quantidade de pixel da cor por frame
        if gray_pixel_count_banco4_mesa1> 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.circle(imagem, (292, 238), raio, (0, 0, 255), -1)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(imagem, (292, 238), raio, (0, 255, 0), -1)
            qtVagasAbertas += 1
    for x, y, w, h in banco5_mesa1:
        recorte = img[y:y + h, x:x + w]
        hsv_recorte = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_recorte, lower_yellow, upper_yellow)
        gray_pixel_count_banco5_mesa1 += np.count_nonzero(mask)

        cv2.putText(img, str(gray_pixel_count_banco5_mesa1), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255),
                    1)  # mostrando a quantidade de pixel da cor por frame
        if gray_pixel_count_banco5_mesa1> 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.circle(imagem, (342, 238), raio, (0, 0, 255), -1)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(imagem, (342, 238), raio, (0, 255, 0), -1)
            qtVagasAbertas += 1
    for x, y, w, h in banco6_mesa1:
        recorte = img[y:y + h, x:x + w]
        hsv_recorte = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_recorte, lower_yellow, upper_yellow)
        gray_pixel_count_banco6_mesa1 += np.count_nonzero(mask)

        cv2.putText(img, str(gray_pixel_count_banco6_mesa1), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255),
                    1)  # mostrando a quantidade de pixel da cor por frame
        if gray_pixel_count_banco6_mesa1> 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.circle(imagem, (392, 238), raio, (0, 0, 255), -1)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(imagem, (392, 238), raio, (0, 255, 0), -1)
            qtVagasAbertas += 1
    for x, y, w, h in banco1_mesa2:
        recorte = img[y:y + h, x:x + w]
        hsv_recorte = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_recorte, lower_yellow, upper_yellow)
        gray_pixel_count_banco1_mesa2 += np.count_nonzero(mask)

        cv2.putText(img, str(gray_pixel_count_banco1_mesa2), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255),
                    1)  # mostrando a quantidade de pixel da cor por frame
        if gray_pixel_count_banco1_mesa2> 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.circle(imagem, (142, 338), raio, (0, 0, 255), -1)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(imagem, (142, 338), raio, (0, 255, 0), -1)
            qtVagasAbertas += 1
    for x, y, w, h in banco2_mesa2:
        recorte = img[y:y + h, x:x + w]
        hsv_recorte = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_recorte, lower_yellow, upper_yellow)
        gray_pixel_count_banco2_mesa2 += np.count_nonzero(mask)

        cv2.putText(img, str(gray_pixel_count_banco2_mesa2), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255),
                    1)  # mostrando a quantidade de pixel da cor por frame
        if gray_pixel_count_banco2_mesa2> 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.circle(imagem, (92, 338), raio, (0, 0, 255), -1)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(imagem, (92, 338), raio, (0, 255, 0), -1)
            qtVagasAbertas += 1
    for x, y, w, h in banco3_mesa2:
        recorte = img[y:y + h, x:x + w]
        hsv_recorte = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_recorte, lower_yellow, upper_yellow)
        gray_pixel_count_banco3_mesa2 += np.count_nonzero(mask)

        cv2.putText(img, str(gray_pixel_count_banco3_mesa2), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255),
                    1)  # mostrando a quantidade de pixel da cor por frame
        if gray_pixel_count_banco3_mesa2> 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.circle(imagem, (42, 338), raio, (0, 0, 255), -1)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(imagem, (42, 338), raio, (0, 255, 0), -1)
            qtVagasAbertas += 1
    for x, y, w, h in banco4_mesa2:
        recorte = img[y:y + h, x:x + w]
        hsv_recorte = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_recorte, lower_yellow, upper_yellow)
        gray_pixel_count_banco4_mesa2 += np.count_nonzero(mask)

        cv2.putText(img, str(gray_pixel_count_banco4_mesa2), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255),
                    1)  # mostrando a quantidade de pixel da cor por frame
        if gray_pixel_count_banco4_mesa2> 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.circle(imagem, (42, 238), raio, (0, 0, 255), -1)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(imagem, (42, 238), raio, (0, 255, 0), -1)
            qtVagasAbertas += 1
    for x, y, w, h in banco5_mesa2:
        recorte = img[y:y + h, x:x + w]
        hsv_recorte = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_recorte, lower_yellow, upper_yellow)
        gray_pixel_count_banco5_mesa2 += np.count_nonzero(mask)

        cv2.putText(img, str(gray_pixel_count_banco5_mesa2), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255),
                    1)  # mostrando a quantidade de pixel da cor por frame
        if gray_pixel_count_banco5_mesa2> 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.circle(imagem, (92, 238), raio, (0, 0, 255), -1)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(imagem, (92, 238), raio, (0, 255, 0), -1)
            qtVagasAbertas += 1
    for x, y, w, h in banco6_mesa2:
        recorte = img[y:y + h, x:x + w]
        hsv_recorte = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_recorte, lower_yellow, upper_yellow)
        gray_pixel_count_banco6_mesa2 += np.count_nonzero(mask)

        cv2.putText(img, str(gray_pixel_count_banco6_mesa2), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255),
                    1)  # mostrando a quantidade de pixel da cor por frame
        if gray_pixel_count_banco6_mesa2> 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.circle(imagem, (142, 238), raio, (0, 0, 255), -1)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(imagem, (142, 238), raio, (0, 255, 0), -1)
            qtVagasAbertas += 1
    for x, y, w, h in banco1_mesa3:
        recorte = img[y:y + h, x:x + w]
        hsv_recorte = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_recorte, lower_yellow, upper_yellow)
        gray_pixel_count_banco1_mesa3 += np.count_nonzero(mask)

        cv2.putText(img, str(gray_pixel_count_banco1_mesa3), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255),
                    1)  # mostrando a quantidade de pixel da cor por frame
        if gray_pixel_count_banco1_mesa3> 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.circle(imagem, (392, 188), raio, (0, 0, 255), -1)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(imagem, (392, 188), raio, (0, 255, 0), -1)
            qtVagasAbertas += 1
    for x, y, w, h in banco2_mesa3:
        recorte = img[y:y + h, x:x + w]
        hsv_recorte = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_recorte, lower_yellow, upper_yellow)
        gray_pixel_count_banco2_mesa3 += np.count_nonzero(mask)

        cv2.putText(img, str(gray_pixel_count_banco2_mesa3), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255),
                    1)  # mostrando a quantidade de pixel da cor por frame
        if gray_pixel_count_banco2_mesa3> 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.circle(imagem, (342, 188), raio, (0, 0, 255), -1)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(imagem, (342, 188), raio, (0, 255, 0), -1)
            qtVagasAbertas += 1
    for x, y, w, h in banco3_mesa3:
        recorte = img[y:y + h, x:x + w]
        hsv_recorte = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_recorte, lower_yellow, upper_yellow)
        gray_pixel_count_banco3_mesa3 += np.count_nonzero(mask)

        cv2.putText(img, str(gray_pixel_count_banco3_mesa3), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255),
                    1)  # mostrando a quantidade de pixel da cor por frame
        if gray_pixel_count_banco3_mesa3> 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.circle(imagem, (292, 188), raio, (0, 0, 255), -1)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(imagem, (292, 188), raio, (0, 255, 0), -1)
            qtVagasAbertas += 1
    for x, y, w, h in banco4_mesa3:
        recorte = img[y:y + h, x:x + w]
        hsv_recorte = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_recorte, lower_yellow, upper_yellow)
        gray_pixel_count_banco4_mesa3 += np.count_nonzero(mask)

        cv2.putText(img, str(gray_pixel_count_banco4_mesa3), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255),
                    1)  # mostrando a quantidade de pixel da cor por frame
        if gray_pixel_count_banco4_mesa3> 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.circle(imagem, (292, 88), raio, (0, 0, 255), -1)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(imagem, (292, 88), raio, (0, 255, 0), -1)
            qtVagasAbertas += 1
    for x, y, w, h in banco5_mesa3:
        recorte = img[y:y + h, x:x + w]
        hsv_recorte = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_recorte, lower_yellow, upper_yellow)
        gray_pixel_count_banco5_mesa3 += np.count_nonzero(mask)

        cv2.putText(img, str(gray_pixel_count_banco5_mesa3), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255),
                    1)  # mostrando a quantidade de pixel da cor por frame
        if gray_pixel_count_banco5_mesa3> 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.circle(imagem, (342, 88), raio, (0, 0, 255), -1)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(imagem, (342, 88), raio, (0, 255, 0), -1)
            qtVagasAbertas += 1
    for x, y, w, h in banco6_mesa3:
        recorte = img[y:y + h, x:x + w]
        hsv_recorte = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_recorte, lower_yellow, upper_yellow)
        gray_pixel_count_banco6_mesa3 += np.count_nonzero(mask)

        cv2.putText(img, str(gray_pixel_count_banco6_mesa3), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255),
                    1)  # mostrando a quantidade de pixel da cor por frame
        if gray_pixel_count_banco6_mesa3> 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.circle(imagem, (392, 88), raio, (0, 0, 255), -1)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(imagem, (392, 88), raio, (0, 255, 0), -1)
            qtVagasAbertas += 1
    for x, y, w, h in banco1_mesa4:
        recorte = img[y:y + h, x:x + w]
        hsv_recorte = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_recorte, lower_yellow, upper_yellow)
        gray_pixel_count_banco1_mesa4 += np.count_nonzero(mask)

        cv2.putText(img, str(gray_pixel_count_banco1_mesa4), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255),
                    1)  # mostrando a quantidade de pixel da cor por frame
        if gray_pixel_count_banco1_mesa4> 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.circle(imagem, (142, 188), raio, (0, 0, 255), -1)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(imagem, (142, 188), raio, (0, 255, 0), -1)
            qtVagasAbertas += 1
    for x, y, w, h in banco2_mesa4:
        recorte = img[y:y + h, x:x + w]
        hsv_recorte = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_recorte, lower_yellow, upper_yellow)
        gray_pixel_count_banco2_mesa4 += np.count_nonzero(mask)

        cv2.putText(img, str(gray_pixel_count_banco2_mesa4), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255),
                    1)  # mostrando a quantidade de pixel da cor por frame
        if gray_pixel_count_banco2_mesa4> 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.circle(imagem, (92, 188), raio, (0, 0, 255), -1)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(imagem, (92, 188), raio, (0, 255, 0), -1)
            qtVagasAbertas += 1
    for x, y, w, h in banco3_mesa4:
        recorte = img[y:y + h, x:x + w]
        hsv_recorte = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_recorte, lower_yellow, upper_yellow)
        gray_pixel_count_banco3_mesa4 += np.count_nonzero(mask)
        
        cv2.putText(img, str(gray_pixel_count_banco3_mesa4), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255),
                    1)  # mostrando a quantidade de pixel da cor por frame
        if gray_pixel_count_banco3_mesa4> 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.circle(imagem, (42, 188), raio, (0, 0, 255), -1)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(imagem, (42, 188), raio, (0, 255, 0), -1)
            qtVagasAbertas += 1
    for x, y, w, h in banco4_mesa4:
        recorte = img[y:y + h, x:x + w]
        hsv_recorte = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_recorte, lower_yellow, upper_yellow)
        gray_pixel_count_banco4_mesa4 += np.count_nonzero(mask)
        
        cv2.putText(img, str(gray_pixel_count_banco4_mesa4), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255),
                    1)  # mostrando a quantidade de pixel da cor por frame
        if gray_pixel_count_banco4_mesa4> 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.circle(imagem, (42, 88), raio, (0, 0, 255), -1)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(imagem, (42, 88), raio, (0, 255, 0), -1)
            qtVagasAbertas += 1
    for x, y, w, h in banco5_mesa4:
        recorte = img[y:y + h, x:x + w]
        hsv_recorte = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_recorte, lower_yellow, upper_yellow)
        gray_pixel_count_banco5_mesa4 += np.count_nonzero(mask)
        
        cv2.putText(img, str(gray_pixel_count_banco5_mesa4), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),
                    1)  # mostrando a quantidade de pixel da cor por frame
        if gray_pixel_count_banco5_mesa4> 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.circle(imagem, (92, 88), raio, (0, 0, 255), -1)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(imagem, (92, 88), raio, (0, 255, 0), -1)
            qtVagasAbertas += 1
    for x, y, w, h in banco6_mesa4:
        recorte = img[y:y + h, x:x + w]
        hsv_recorte = cv2.cvtColor(recorte, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_recorte, lower_yellow, upper_yellow)
        gray_pixel_count_banco6_mesa4 += np.count_nonzero(mask)
        
        cv2.putText(img, str(gray_pixel_count_banco6_mesa4), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),
                    1)  # mostrando a quantidade de pixel da cor por frame
        if gray_pixel_count_banco6_mesa4> 150:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
            cv2.circle(imagem, (142, 88), raio, (0, 0, 255), -1)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.circle(imagem, (142, 88), raio, (0, 255, 0), -1)
            qtVagasAbertas += 1
    #imprime na interface da camera a quantidade de lugares livres
    cv2.putText(img,f'LIVRE: {qtVagasAbertas}/{totaldebancos}',(30,200),cv2.FONT_HERSHEY_SIMPLEX,1.5,(171,71,0),5)
    #imprime o titulo mapa ao vivo no mapa
    cv2.putText(imagem,'MAPA AO VIVO',(105,50),cv2.FONT_HERSHEY_SIMPLEX,1,(171,71,0),3)
    #mostrar isso ao usuario
    cv2.imshow('Minimapa',imagem)
    cv2.imshow('Camera',img)
    #open cv aguarda a tecla 'q' ser apertada
    key = cv2.waitKey(1)
    if key == ord('q'):  # Verifica se a tecla 'q' foi pressionada e fecha o codigo
        break

cv2.destroyAllWindows()