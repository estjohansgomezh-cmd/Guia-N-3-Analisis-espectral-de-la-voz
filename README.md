# Guia-N-3-Analisis-espectral-de-la-voz
---
## Descripción
En este repositorio se presenta el informe y los resultados de la Práctica de Laboratorio #3 de Análisis espectral de la voz.

En esta práctica de laboratorio se tuvo como propósito aplicar técnicas de análisis espectral para caracterizar y diferenciar señales de voz humana según el género del hablante. Se grabaron seis señales de voz en formato WAV (tres voces masculinas y tres femeninas), pronunciando la misma frase corta en condiciones controladas de silencio ambiental. A partir de estas grabaciones, se empleó Python para realizar el procesamiento digital completo: representación en el dominio del tiempo, cálculo de la Transformada de Fourier (FFT), estimación de la Densidad Espectral de Potencia (PSD) y extracción de parámetros característicos como la frecuencia fundamental (F0), la frecuencia media, el brillo espectral (centroide espectral), la intensidad (energía RMS), el jitter y el shimmer.
Los resultados permiten comparar cuantitativamente las diferencias espectrales entre voces masculinas y femeninas, y reflexionar sobre la aplicabilidad clínica de estos parámetros en áreas como la biometría vocal, el reconocimiento de hablantes y la detección de patologías de la voz.
## Metodología
Las grabaciones se realizaron con los micrófonos integrados de teléfonos inteligentes, con el fin de garantizar condiciones comparables entre los seis participantes. Cada grabador pronunció la misma frase corta durante aproximadamente cinco segundos en un entorno sin ruido ambiental significativo.
Los archivos resultantes fueron nombrados de forma sistemática (hombre1.wav, hombre2.wav, hombre3.wav, mujer1.wav, mujer2.wav, mujer3.wav) y subidos al repositorio de GitHub del grupo para su procesamiento colaborativo.
##  Adquisición de las señales de voz (Parte A)

### Graficas de dominio en el tiempo de las notas de voz 

<img width="2685" height="1219" alt="A1_tiempo_20260319_135541" src="https://github.com/user-attachments/assets/7b136003-53c4-494f-bd77-8b0e7627ce84" />


### Datos optenidos.
### HOMBRES
1).


<img width="304" height="250" alt="image" src="https://github.com/user-attachments/assets/872bb959-b6a8-46e4-8067-99c2e7c6c390" />

2).

<img width="330" height="250" alt="image" src="https://github.com/user-attachments/assets/513e2e9a-f698-49de-83e9-e91398551bc2" />


3). 

<img width="336" height="248" alt="image" src="https://github.com/user-attachments/assets/e2a7dd61-4366-4740-b458-6149c9b0f830" />


### MUJERES

1).

<img width="320" height="251" alt="image" src="https://github.com/user-attachments/assets/f42ac7bd-b7fb-42de-8773-893c8a0ca3c1" />


2). 

<img width="281" height="248" alt="image" src="https://github.com/user-attachments/assets/d97fdce4-59d9-4df9-8973-38897b7d9a2a" />


3). 

<img width="282" height="249" alt="image" src="https://github.com/user-attachments/assets/8e86bce6-54f3-4cd3-aabd-11e6e5a5422f" />





## Medición de Jitter y Shimmer (Parte B)
Para cada grabación se aplicó un filtro pasa-banda (80–400 Hz para hombres, 150–500 Hz para mujeres) previo a la detección de ciclos. La frecuencia fundamental ciclo a ciclo se estimó mediante cruces por cero, extrayendo los períodos Ti. El jitter se calculó como la variación promedio normalizada de períodos consecutivos. El shimmer se obtuvo de manera análoga a partir de los picos de amplitud Ai en cada ciclo. Los valores de referencia para voces sanas son jitter relativo ≤ 1 % y shimmer relativo ≤ 3–5 %.
## Comparación y Conclusiones (Parte C)
1. ¿Qué diferencias se observan en la frecuencia fundamental?
La frecuencia fundamental es el parámetro que muestra la diferencia más pronunciada entre géneros. 

2. ¿Qué otras diferencias notan en términos de brillo, media o intensidad?
   
4. Redactar conclusiones sobre el comportamiento de la voz en hombres y mujeres a partir de los análisis realizados.
5. Discuta la importancia clínica del jitter y shimmer en el análisis de la voz. 


 
