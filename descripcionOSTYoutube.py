# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 10:43:04 2021

@author: rpgdragon
"""
import os
import sys
import glob
from math import trunc


if __name__ == '__main__':
    # To check for the existence of modules without importing them.
    # Apparently imp and importlib are a forest of deprecation!
    # The API was changed once in 3.3 (deprecating imp),
    # and then again in 3.4 (deprecating the 3.3 API).
    # So.... we have to do this dance to avoid deprecation warnings.
    try:
        try:
            from importlib.util import find_spec as find_module # Python 3.4+
        except ImportError:
            from importlib import find_loader as find_module # Python 3.3
    except ImportError:
        from imp import find_module # Python 2

    # User-friendly name, import name, pip specification.
    requiredModules = [
        ['mutagen', 'mutagen', 'mutagen >= 1.45.0, < 1.45.1']
    ]

    def moduleExists(name):
        try:
            result = find_module(name)
        except ImportError:
            return False
        else:
            return result is not None
    def neededInstalls(requiredModules=requiredModules):
        uninstalledModules = []
        for module in requiredModules:
            if not moduleExists(module[1]):
                uninstalledModules.append(module)
        return uninstalledModules

    def install(package):
        nowhere = open(os.devnull, 'w')
        exitStatus = subprocess.call([sys.executable, '-m', 'pip', 'install', package],
                                     stdout=nowhere,
                                     stderr=nowhere)
        if exitStatus != 0:
            raise OSError("Failed to install package.")
    def installModules(modules, verbose=True):
        for module in modules:
            if verbose:
                print("Installing {}...".format(module[0]))
            
            try:
                install(module[2])
            except OSError as e:
                if verbose:
                    print("Failed to install {}. "
                          "You may need to run the script as an administrator "
                          "or superuser.".format(module[0]),
                          file=sys.stderr)
                    print("You can also try to install the package manually "
                          "(pip install \"{}\")".format(module[2]),
                          file=sys.stderr)
                raise e
    def installRequiredModules(needed=None, verbose=True):
        needed = neededInstalls() if needed is None else needed
        installModules(neededInstalls(), verbose)

    needed = neededInstalls()
    if needed:
        if moduleExists('pip'):
            # Needed to call pip the official way.
            import subprocess
        else:
            print("You don't seem to have pip installed!", file=sys.stderr)
            print("Get it from https://pip.readthedocs.org/en/latest/installing.html", file=sys.stderr)
            sys.exit(1)

    try:
        installRequiredModules(needed)
    except OSError:
        sys.exit(1)

# ------


from mutagen.mp3 import MP3


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
        
if __name__ == '__main__':
    import argparse

    SCRIPT_NAME = os.path.split(sys.argv[0])[-1]

    # Tiny details!
    class KindArgumentParser(argparse.ArgumentParser):
        def error(self, message):
            print("No se ha especificado la ruta del OST! Debe incluir la ruta absoluta donde se encuentra la colección de Mp3", file=sys.stderr)
            sys.exit(1)

    

    def doIt(): # Only in a function to be able to stop after errors, really.
        parser = KindArgumentParser(description="Crea un fichero de tiempos para Youtube.\n\n"
                                    "Examples:\n"
                                    "%(prog)s /home/pi/tmp\n",
                                    epilog="Script escrito por José Manuel Castellano Domínguez",
                                    add_help=False)
        
        try: # Even more tiny details!
            parser._positionals.title = "Positional arguments"
            parser._optionals.title = "Optional arguments"
        except AttributeError:
            pass

        parser.add_argument('path',
                            help="Ruta donde se localizan los Mp3 que se quiera generar los tiempos de pista para Youtube")
        
        parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                            help="Enseña esta ayuda y termina el programa")
       
        arguments = parser.parse_args()


        path = arguments.path if arguments.path is not None else []
        DescripcionOSTYoutube.generaArchivoCanciones(path)
        return 0
    
    sys.exit(doIt())
