import math
import cv2
import os

class Extrator:
    def setATRIB(self, video_ref, frame_seconds_index): #metodo para atribuir valores aos atributos
        self.videoRef = video_ref
        self.frameSecond = frame_seconds_index

    def extractFrame(self): #metodo para extrair um frame do video de acordo com o tempo fornecido
        try:
            frame_escolhido=0
            cap= cv2.VideoCapture(os.path.join(os.pardir, "data\\"+self.videoRef))
            numeroFrames=cap.get(cv2.CAP_PROP_FRAME_COUNT) #Numero de frames
            fps=cap.get(cv2.CAP_PROP_FPS) #Frames por Segundo
            tempoVideo=math.floor(numeroFrames/fps) #Tempo do video(floor)

            if self.frameSecond < tempoVideo: #Checa o comprimento do video e compara com o valor recebido
                cap.set(cv2.CAP_PROP_POS_FRAMES, self.frameSecond*fps) #Seleciona o frame no segundo fornecido
            else:
                #extrair ultimo frame
                cap.set(cv2.CAP_PROP_POS_FRAMES, (tempoVideo-1)*fps) #Seleciona o ultimo frame

            res, frame = cap.read() #Le o frame
            frame_escolhido=frame
            #cv2.imwrite('f.png',frame)
            cap.release()
            return frame_escolhido, "OK"
        except:
            return frame_escolhido, "ERRO"



