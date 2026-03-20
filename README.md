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

### Registro de características espectrales
<img width="1600" height="372" alt="image" src="https://github.com/user-attachments/assets/ce8d6fe6-0f88-4ac6-81cb-605da0337576" />
Los índices de jitter y shimmer están elevados respecto a rangos clínicos en todas las grabaciones, lo cual refleja las limitaciones del equipo de captura más que inestabilidad vocal patológica, y demuestra la alta sensibilidad de estos parámetros a las condiciones de adquisición.

### Diagrama de flujo

<img width="1410" height="2694" alt="image" src="https://github.com/user-attachments/assets/ee63a7c7-34e2-4b39-b22f-f058d0bcb1f5" />

## Comparación y Conclusiones (Parte C)
1. ¿Qué diferencias se observan en la frecuencia fundamental?
   La F0 media de las voces masculinas fue aproximadamente 115 Hz, en contraste con los 221 Hz promedio de las voces femeninas, una diferencia de casi el doble. Esta brecha refleja las diferencias anatómicas en la laringe: las cuerdas vocales de los hombres tienen mayor longitud (17–23 mm) y masa que las de las mujeres (12–17 mm), lo que reduce la frecuencia de vibración según la relación inversamente proporcional entre masa del oscilador y frecuencia de resonancia

3. ¿Qué otras diferencias notan en términos de brillo, media o intensidad?
   El centroide espectral femenino (~2 049 Hz promedio) superó al masculino (~1 252 Hz promedio) en más de 800 Hz. Esto indica que la energía de la señal de voz femenina se distribuye hacia componentes de mayor frecuencia, incluyendo armónicos más altos. Fisiológicamente, las voces femeninas poseen una mayor cantidad de energía en las frecuencias medias y altas del espectro, lo que se percibe como un timbre más brillante y agudo.
   
5. Redactar conclusiones sobre el comportamiento de la voz en hombres y mujeres a partir de los análisis realizados.
   Las voces masculinas presentaron valores RMS ligeramente superiores (promedio 0.0848) respecto a las femeninas (0.0685). Esta diferencia puede atribuirse tanto a un mayor volumen de fonación durante la grabación como a una mayor presión subglótica en la producción vocal masculina. No obstante, la variabilidad intragrupo también puede depender del esfuerzo vocal individual de cada participante.
   
7. Discuta la importancia clínica del jitter y shimmer en el análisis de la voz.
   Las voces femeninas presentaron índices de jitter relativo levemente menores (~2.0%) en comparación con las masculinas (~2.8%). El shimmer relativo también resultó inferior en mujeres (~2.5%) frente a hombres (~3.3%). Esto podría indicar mayor estabilidad en el control vocal femenino, aunque las diferencias no son suficientemente grandes para establecer conclusiones fisiológicas definitivas con el tamaño de muestra de esta práctica.

### Preguntas para la discusión 
1. ¿Cómo es la frecuencia fundamental de la densidad espectral de potencia de una voz masculina respecto a una femenina? ¿Qué hay del valor RMS?
   La frecuencia fundamental asociada al primer pico de la densidad espectral de potencia (PSD) es significativamente menor en las voces masculinas que en las femeninas. En los resultados obtenidos, los hombres presentaron F0 entre 105 y 128 Hz, mientras que las mujeres lo hicieron entre 204 y 242 Hz. Esto se refleja en la PSD como un pico dominante desplazado hacia la izquierda (menores frecuencias) en el caso masculino, y hacia la derecha (mayores frecuencias) en el femenino. Además, los armónicos de la voz masculina se ubican más próximos entre sí en el eje de frecuencias, dado que son múltiplos de una F0 más baja.
   En cuanto al valor RMS, que es una medida directa de la intensidad o energía de la señal, los resultados mostraron valores ligeramente mayores en las voces masculinas (0.079 a 0.091) frente a las femeninas (0.065 a 0.071). Sin embargo, esta diferencia refleja principalmente el esfuerzo vocal durante la grabación y no es una propiedad fisiológica intrínseca e invariable del género. En condiciones controladas de presión sonora idéntica, las diferencias de RMS tienden a ser mínimas entre géneros.
   
2. ¿Qué limitaciones plantea el uso de jitter y shimmer para la detección de patologías como disartrias y afasias?
   El jitter y el shimmer son indicadores valiosos de la inestabilidad vocal ciclo a ciclo, y su uso está bien establecido en la evaluación de trastornos de la voz como disfonía, nódulos vocales, parálisis de cuerdas vocales y algunos trastornos neurodegenerativos (como la enfermedad de Parkinson). No obstante, su aplicación directa a la detección de disartrias y afasias presenta limitaciones importantes:
   Naturaleza del trastorno: Las disartrias son alteraciones motoras del habla que afectan la articulación, la prosodia y la resonancia, pero no exclusivamente la vibración laríngea. El jitter y el shimmer capturan únicamente variabilidad en la fuente glótica, dejando fuera los componentes articulatorios y supraglóticos que caracterizan a las disartrias. Las afasias, por su parte, son trastornos del lenguaje de origen cortical que impactan la comprensión y producción lingüística, no la mecánica de vibración de las cuerdas vocales, por lo que jitter y shimmer prácticamente no aportan información diagnóstica en este caso.
   Sensibilidad y especificidad: Los valores de jitter y shimmer pueden elevarse por causas múltiples (tensión vocal, fatiga, ruido en la grabación, algoritmo de detección de ciclos), lo que reduce su especificidad diagnóstica. Un paciente con disartria espástica puede presentar jitter elevado, pero también lo puede hacer un hablante sano grabado en condiciones subóptimas.
   Dependencia del método de cálculo: Los resultados varían considerablemente según el algoritmo de detección de períodos (cruces por cero, autocorrelación, detección de picos), la frecuencia de muestreo, el filtrado previo y el segmento analizado. Esto dificulta la comparación entre estudios y la definición de umbrales clínicos universales.
   Insuficiencia como medida aislada: Ninguno de los dos índices, por sí solo, permite diferenciar entre distintas patologías vocales o del habla. Su utilidad clínica se maximiza cuando se combinan con análisis acústicos complementarios (espectrograma, formantes, medidas de turbulencia como la relación armónico-ruido) y con evaluación perceptual y endoscópica.
   Limitaciones en habla continua: Jitter y shimmer se calculan de forma óptima sobre vocales sostenidas y estables. En habla continua, la variación natural de F0 y amplitud inherente a la prosodia del discurso contamina los estimados, dificultando la distinción entre variabilidad patológica y variabilidad lingüística normal.

En conclusión, jitter y shimmer son herramientas útiles como parte de una batería de evaluación vocal, pero resultan insuficientes como único criterio diagnóstico para trastornos complejos del habla y el lenguaje como la disartria o la afasia, donde se requiere un enfoque multidimensional que integre parámetros acústicos, lingüísticos y neurológicos.

