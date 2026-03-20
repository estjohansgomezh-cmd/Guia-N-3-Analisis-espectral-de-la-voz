# Guia-N-3-Analisis-espectral-de-la-voz
---
## Descripción
En este repositorio se presenta el informe y los resultados de la Práctica de Laboratorio #3 de Análisis espectral de la voz.

En esta práctica de laboratorio se tuvo como propósito central estudiar las características espectrales de señales de voz humana y emplearlas para diferenciar patrones entre géneros. Para ello se capturaron grabaciones de seis hablantes (tres hombres y tres mujeres) pronunciando la misma frase corta, las cuales fueron posteriormente procesadas en Python mediante técnicas de análisis en frecuencia.
El trabajo se estructuró en tres partes. La Parte A se enfocó en la adquisición de las señales y su análisis espectral mediante la Transformada de Fourier, extrayendo parámetros clave como la frecuencia fundamental (F0), la frecuencia media, el brillo espectral (centroide) y la intensidad (RMS). La Parte B abordó la medición de la variabilidad vocal a través de los índices de jitter y shimmer. Finalmente, la Parte C concentró la comparación entre géneros y la discusión de las implicaciones clínicas de los resultados.
## Metodología
Las grabaciones se realizaron con los micrófonos integrados de teléfonos inteligentes, con el fin de garantizar condiciones comparables entre los seis participantes. Cada grabador pronunció la misma frase corta durante aproximadamente cinco segundos en un entorno sin ruido ambiental significativo.
Los archivos resultantes fueron nombrados de forma sistemática (hombre1.wav, hombre2.wav, hombre3.wav, mujer1.wav, mujer2.wav, mujer3.wav).
Las señales fueron importadas en Python mediante la librería scipy.io.wavfile. En caso de que algún archivo presentara dos canales (estéreo), se promedió entre ambos canales para obtener una señal monoaural. Posteriormente, cada señal se normalizó a la unidad dividiendo por el valor máximo absoluto, eliminando diferencias de ganancia entre grabadoras y facilitando la comparación directa de amplitudes.

##  Adquisición de las señales de voz (Parte A)
Mediante el script parte A.py disponible en el repositorio se ejecutaron las siguientes etapas:
- Representación temporal: Se graficó cada señal en el dominio del tiempo junto con la media, la mediana y las bandas de ±1 desviación estándar.
- Transformada de Fourier (FFT): Se calculó la FFT de cada señal usando numpy.fft.rfft, obteniendo el espectro de magnitudes y el espectro de fase en escala logarítmica.
- Densidad Espectral de Potencia (PSD): Se estimó como |X(f)|² / (N · Fs) para caracterizar la distribución de energía en frecuencia.
- Extracción de características: Frecuencia fundamental (F0) por autocorrelación normalizada en el rango 50–300 Hz (hombres) y 100–500 Hz (mujeres); frecuencia media y brillo espectral (centroide) como promedios ponderados por la magnitud; intensidad como valor RMS de la señal temporal.

### Graficas de dominio en el tiempo de las notas de voz 

<img width="2685" height="1219" alt="A1_tiempo_20260319_135541" src="https://github.com/user-attachments/assets/7b136003-53c4-494f-bd77-8b0e7627ce84" />

### Transformada de Fourier y Espectro de fase

#### HOMBRES

<img width="2085" height="1037" alt="A2_fft_hombre1_20260319_135541" src="https://github.com/user-attachments/assets/78a839b4-9994-4428-88bf-2f2b2b5bf787" />
<img width="2085" height="1037" alt="A2_fft_hombre2_20260319_135541" src="https://github.com/user-attachments/assets/742c5430-cff8-4f30-b2f6-6a8be4466912" />
<img width="2085" height="1037" alt="A2_fft_hombre3_20260319_135541" src="https://github.com/user-attachments/assets/139c44f8-0a30-44bf-b695-57effdcd0d63" />


#### MUJERES

<img width="2085" height="1037" alt="A2_fft_mujer1_20260319_135541" src="https://github.com/user-attachments/assets/75848bdc-b5ac-4d43-aed0-a0d68a59b154" />
<img width="2085" height="1037" alt="A2_fft_mujer2_20260319_135541" src="https://github.com/user-attachments/assets/3f92239b-222b-47ff-8ad9-49d20b69cfd2" />
<img width="2085" height="1037" alt="A2_fft_mujer3_20260319_135541" src="https://github.com/user-attachments/assets/96959558-1099-4904-bda4-02309312a3c0" />

#### DENSIDADES ESPECTRALES DE POTENCIA

<img width="2685" height="1220" alt="A3_psd_20260319_135541" src="https://github.com/user-attachments/assets/81a30782-8fbd-4c2c-9147-fdaf83067d0e" />

### Datos obtenidos.
#### HOMBRES
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

### Registro de características espectrales

<img width="1600" height="452" alt="image" src="https://github.com/user-attachments/assets/f109a463-78bf-4df3-a924-faf90255cd0f" />
La tabla confirma que F0 es el parámetro más discriminante entre géneros, con una separación clara de casi 100 Hz entre grupos, mientras que el RMS refleja condiciones de grabación más que diferencias fisiológicas.

### Diagrama de flujo

<img width="1410" height="3026" alt="image" src="https://github.com/user-attachments/assets/00fa01a3-6058-48b2-a32b-8dec3168caf3" />
## Medición de Jitter y Shimmer (Parte B)
Se implementó el cálculo de los índices de estabilidad vocal jitter y shimmer para las seis grabaciones. El procedimiento comenzó aplicando un filtro Butterworth pasa-banda de quinto orden a cada señal, con frecuencias de corte ajustadas al rango vocal de cada género: 80–400 Hz para hombres y 150–500 Hz para mujeres. Este paso elimina componentes de ruido fuera de la banda vocal que podrían distorsionar la detección de ciclos.

Los períodos de vibración Ti se determinaron a partir de la detección de cruces por cero con pendiente positiva en la señal filtrada. Las amplitudes de ciclo Ai se definieron como el valor máximo de la señal dentro de cada período. Con estas secuencias se aplicaron directamente las fórmulas de jitter absoluto/relativo y shimmer absoluto/relativo.

### HOMBRES

1).

<img width="1866" height="1788" alt="B1_hombre1_20260319_141126" src="https://github.com/user-attachments/assets/e73cf67c-5cd3-4c40-ad26-5bd3daee1573" /><img width="433" height="189" alt="image" src="https://github.com/user-attachments/assets/a1ed3e03-02cc-467a-a7ab-c97a4edb9a64" />

2).

<img width="1866" height="1788" alt="B1_hombre2_20260319_141126" src="https://github.com/user-attachments/assets/791480b2-591c-47f7-a087-684b1b441ed0" /><img width="435" height="193" alt="image" src="https://github.com/user-attachments/assets/f4189ac9-ea08-49cf-94cb-3dd090c079be" />

3).

<img width="1866" height="1788" alt="B1_hombre3_20260319_141126" src="https://github.com/user-attachments/assets/b0b1c43e-193b-4ff8-aecb-14db8c940d8d" /><img width="422" height="192" alt="image" src="https://github.com/user-attachments/assets/9722927a-5387-4e9f-85bb-90e60c7b6318" />

### MUJERES

1).

<img width="1866" height="1788" alt="B1_mujer1_20260319_141126" src="https://github.com/user-attachments/assets/80be3a72-3cff-4fbb-8e5a-7f757497a027" /><img width="413" height="184" alt="image" src="https://github.com/user-attachments/assets/81c95ae3-9d47-485a-8865-c554aaea46ae" />

2).

<img width="1866" height="1788" alt="B1_mujer2_20260319_141126" src="https://github.com/user-attachments/assets/527c0bc5-02c0-4414-b2d7-c0765d68596d" /><img width="424" height="191" alt="image" src="https://github.com/user-attachments/assets/23577c0a-0271-4c7d-8b51-5e65fef36689" />

3).

<img width="1874" height="1788" alt="B1_mujer3_20260319_141126" src="https://github.com/user-attachments/assets/6b009bed-a72d-4e4b-a798-f491697f647e" /><img width="422" height="191" alt="image" src="https://github.com/user-attachments/assets/7048a827-984d-41ce-88af-5f812c1dae0d" />

### Resultados de jitter y shimmer

<img width="849" height="285" alt="image" src="https://github.com/user-attachments/assets/dec6ff31-5239-4e65-bf76-782db477722a" />

### Registro de características espectrales
<img width="1600" height="372" alt="image" src="https://github.com/user-attachments/assets/ce8d6fe6-0f88-4ac6-81cb-605da0337576" />
Los índices de jitter y shimmer están elevados respecto a rangos clínicos en todas las grabaciones, lo cual refleja las limitaciones del equipo de captura más que inestabilidad vocal patológica, y demuestra la alta sensibilidad de estos parámetros a las condiciones de adquisición.

### Diagrama de flujo

<img width="1410" height="2694" alt="image" src="https://github.com/user-attachments/assets/ee63a7c7-34e2-4b39-b22f-f058d0bcb1f5" />

## Comparación y Conclusiones (Parte C)
1. ¿Qué diferencias se observan en la frecuencia fundamental?
La frecuencia fundamental es el parámetro que muestra la diferencia más pronunciada entre géneros. 

2. ¿Qué otras diferencias notan en términos de brillo, media o intensidad?
   
4. Redactar conclusiones sobre el comportamiento de la voz en hombres y mujeres a partir de los análisis realizados.
5. Discuta la importancia clínica del jitter y shimmer en el análisis de la voz. 


 
