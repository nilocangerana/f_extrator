import numpy as np
import cv2
from PIL import Image
import os

class Operador:
    def setATRIB(self, idx, frame, op_type): #metodo para atribuir valores aos atributos
        self.index = idx
        self.frame = frame
        self.op_list = op_type.split("|") #gera uma lista com todas as operacoes a serem realizadas no frame

    def dataAugmentation(self): #metodo que realiza o data augmentation no frame
        try:
            frame_aug=self.frame
            if "noise" in self.op_list:
                frame_aug=self.noise(frame_aug, 0.03)

            if "grayscale" in self.op_list:
                frame_aug = cv2.cvtColor(frame_aug, cv2.COLOR_BGR2GRAY)

            if "flip" in self.op_list:
                frame_aug = np.fliplr(frame_aug)

            if "random_rotation" in self.op_list:
                angle = np.random.uniform(0,180)
                pil_image=Image.fromarray(frame_aug)
                pil_image=pil_image.rotate(angle)
                frame_aug = np.array(pil_image)

            print('  Processando mensagem: ', self.index,' - Salvando frame...')
            #cv2.imwrite(os.path.join(os.pardir, "data\\frames_extraidos\\frame-"+str(self.index)+".png"),frame_aug)
            return "OK"
        except:
            return "ERRO"

    def noise(self, image, prob): #adiciona ruido preto/branco
        black = np.array([0, 0, 0], dtype='uint8') #pixel preto
        white = np.array([255, 255, 255], dtype='uint8') #pixel branco
        probs = np.random.random(image.shape[:2]) #cria uma matriz do tamanho da imagem e preenche com numeros aleatorio no intervalo: [0.0, 1.0)
        #compara o valor da matriz com o valor passado inicialmente(prob)
        image[probs < (prob)] = black #define se o valor do pixel é preto
        image[probs > (1 - prob)] = white #define se o valor do pixel é branco, nao pode ser branco e preto ao mesmo tempo
        return image
