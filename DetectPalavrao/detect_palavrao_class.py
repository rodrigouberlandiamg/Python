# Instalação de pacotes
# pip install SpeechRecognition
# pip install pipwin
# pipwin install PyAudio

import speech_recognition as sr

class DetectPalavrao:
    def __init__(self):
        self.__list_palavroes = ['carai','otario','*','bixa','veado','fudido','burro','burra','imbecil','caralho','doente','puta','merda','bosta','fodeu']
        self.__palavras = []
        self.__bloqueio = False

    @property
    def list_palavroes(self):
        return self.__list_palavroes

    @property
    def palavras(self):
        return self.__palavras

    @property
    def bloqueio(self):
        return self.__bloqueio

    @palavras.setter
    def palavras(self,palavras):
        self.__palavras.append(palavras)

    @bloqueio.setter
    def bloqueio(self,bloqueio):
        self.__bloqueio = bloqueio


    def bloqueia_internet(self):
        print('Sua internet será bloqueada.')

    def verificarFala(self):
        rec = sr.Recognizer()
        while True:
            texto_encontrato = []
            self.bloqueio = False
            with sr.Microphone(1) as mic:
                # print(sr.Microphone().list_microphone_names())
                rec.adjust_for_ambient_noise(mic)
                print('Escutando ...')
                audio = rec.listen(mic)
                texto = rec.recognize_google(audio,language="pt-BR",show_all=True)

            if texto:
                qtde_texto_encontrado = len(texto['alternative'])
                for i in range(qtde_texto_encontrado):
                    texto_encontrato.append(texto['alternative'][i]['transcript'])
                print(texto_encontrato)
                self.palavras.append(texto_encontrato)
                print(texto)
                for palavrao in self.list_palavroes:
                    for i in range(qtde_texto_encontrado):
                        if palavrao in texto_encontrato[i]:
                            self.bloqueio = True
                if self.bloqueio:
                    self.bloqueia_internet()
