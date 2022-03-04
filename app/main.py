from Extrator import Extrator
from Operador import Operador
import requests

class MainExtrator:
    def __init__(self): #instancia as classes Extrator e Operador
        self.extratorObj = Extrator()
        self.operadorObj = Operador()

    def setATRIB(self, idx, video_ref, frame_seconds_index, op_type): #metodo para atribuir valores aos atributos
        self.index=idx
        self.videoRef = video_ref
        self.frameSecond = frame_seconds_index
        self.operationType = op_type
    
    def executarExtrator(self): #metodo que executa o extrator e operador
        requests.post('http://127.0.0.1:5000/registro/create', json={
            "msgIndex": self.index, 
            "video_ref": self.videoRef,
            "frame_seconds_index": self.frameSecond, 
            "op_type": self.operationType,
            "status": ""
        })
        self.extratorObj.setATRIB(video_ref=self.videoRef, frame_seconds_index=self.frameSecond)
        frame_extraido, status = self.extratorObj.extractFrame()
        if status == "OK":
            self.operadorObj.setATRIB(idx=self.index, frame=frame_extraido, op_type= self.operationType)
            status = self.operadorObj.dataAugmentation()

        requests.put('http://127.0.0.1:5000/registro/update/'+str(self.index)+'/'+status)


