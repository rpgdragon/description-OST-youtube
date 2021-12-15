# description-OST-youtube
Fichero Python para generar las rutas de tiempo de un video músical de Youtube. Al ejecutarse este script en Python lo que hará es generar un fichero con extensión txt, donde cada linea aparecerá

`hh:mm:ss NombreCanción`  

Donde hh:mm:ss es la hora, minuto y segundo en la que empieza a reproducirse la canción en el video y el Nombre de la canción, es el nombre que tiene el fichero MP3 sin la extensión MP3. Es importante recalcar que el orden de las canciones viene determinada por el nombre de los ficheros MP3. Si se graba el video en un orden distinto, se debe reordenar los ficheros Mp3 con un nombre ordenado antes de ejecutar este script. Se muestra a continuación, una porción de un ejemplo de la ejecución de este programa

00:00 1-01 Professor Layton vs Phoenix Wright- Ace Attorney ~ Opening Theme  
01:56 1-02 About Town ~ PL vs PW- AA Version  
04:18 1-03 Bewitching Puzzles  
06:55 1-04 A Strange Story ~ PL vs PW- AA Version  
09:55 1-05 Labyrinthia  
12:36 1-06 Crisis ~ PL vs PW- AA Version  
14:33 1-07 A Pleasant Afternoon ~ PL vs PW- AA Version  
16:48 1-08 An Uneasy Atmosphere ~ PL vs PW- AA Version  
.......................

Para usar basta unicamente importar el módulo y usar una llamada como la que se indica a continuación
```
DescripcionOSTYoutube.generaArchivoCanciones(path="rutaabsoluta")
```

| Parámetro | Descripción |
| --------- | ----------- |
| Path | Indica la ruta absoluta donde se encuentran los ficheros MP3 ubicados y que forman parte del video. Si no se indica, se hará en el directorio actual. El fichero de salida se ubica en este mismo directorio. |
| hayretardo | Parámetro Opcional que indica si debe aplicarse un retraso de 1seg cada 5 canciones. No utilizar si se utiliza directamente en un ripeador tipo Sony Vegas o Camtasia |
