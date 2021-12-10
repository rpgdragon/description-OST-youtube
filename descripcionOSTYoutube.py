# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 10:43:04 2021

@author: rpgdragon
"""
import os
import glob
from mutagen.mp3 import MP3
from math import trunc

class DescripcionOSTYoutube:
 
    def generaArchivoCanciones(path=''):
        self = DescripcionOSTYoutube()
        f = open(path + "out.txt","wt")
        seconds = 0
        minutes = 0
        hours = 0
        for name in glob.glob(path + '*.mp3'):
            nombrecorto = os.path.basename(name)
            audio = MP3(name)
            #en cada linea va, el tiempo actual y el nombre de la cancion
            #de momento solo ponemos el nombre de la cancio
            nombreSinExtension = nombrecorto.replace('.mp3','')
            f.write(self.__crearCadenaTiempo(hours,minutes,seconds))
            f.write(' ')
            f.write(nombreSinExtension)
            f.write('\n')
            # cargamos los tiempos, sumamos los segundos, se utilizan los decimales para la suma
            # para calcular el tiempo exacto
            seconds = seconds + audio.info.length
            # y ahora lo convertimos a formato correcto
            minutessumar = trunc(seconds / 60)
            seconds = seconds % 60
            minutes = minutes + minutessumar
            hourssumar = trunc(minutes / 60)
            minutes = minutes % 60
            hours = hours + hourssumar
        f.close()
    
    def __crearCadenaTiempo(self,hours,minutes,seconds):
        seconds = trunc(seconds)
        if(seconds<10):
            seconds='0' + str(seconds)
        else:
            seconds = '' + str(seconds)
        if(minutes<10):
            minutes='0' + str(minutes)
        else:
            minutes = '' + str(minutes)
        if(hours<10):
            hours='0' + str(hours) 
        else:
            hours= '' + str(hours)
        
        if(hours!='00'):
            return hours +":" + minutes + ":" + seconds
        else:
            return minutes + ":" + seconds
