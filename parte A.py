# -*- coding: utf-8 -*-
"""
=============================================================================
PRÁCTICA DE LABORATORIO – ANÁLISIS ESPECTRAL DE LA VOZ
Universidad Militar Nueva Granada
Asignatura: Procesamiento Digital de Señales

PARTE A – Adquisición y análisis espectral de señales de voz

Este script:
  1. Lee señales de voz desde archivos .wav (3 hombres, 3 mujeres)
  2. Grafica las señales en el dominio del tiempo
  3. Calcula y grafica la Transformada de Fourier (magnitud y fase)
  4. Grafica la Densidad Espectral de Potencia (PSD)
  5. Extrae y reporta:
       - Frecuencia fundamental (F0)
       - Frecuencia media espectral
       - Brillo (centroide espectral)
       - Intensidad / energía (RMS)

=============================================================================
INSTRUCCIONES:
  1. Coloca tus archivos .wav en la misma carpeta que este script.
  2. Edita la lista ARCHIVOS_VOZ con los nombres reales de tus archivos.
  3. Ejecuta: python parteA_adquisicion_espectral.py

DEPENDENCIAS:
  pip install numpy scipy matplotlib
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
"""from scipy import signal as scipy_signal"""
from datetime import datetime
import os
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# ██  CONFIGURACIÓN – EDITAR AQUÍ LOS NOMBRES DE TUS ARCHIVOS  ██
# =============================================================================
# Formato: ('nombre_archivo.wav', 'género', 'etiqueta para gráficas')
# género: 'M' = Masculino,  'F' = Femenino

ARCHIVOS_VOZ = [
    ('hombre1.wav', 'M', 'Hombre 1'),
    ('hombre2.wav', 'M', 'Hombre 2'),
    ('hombre3.wav', 'M', 'Hombre 3'),
    ('mujer1.wav',  'F', 'Mujer 1'),
    ('mujer2.wav',  'F', 'Mujer 2'),
    ('mujer3.wav',  'F', 'Mujer 3'),
]

CARPETA_SALIDA = 'resultados_parteA'
os.makedirs(CARPETA_SALIDA, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

COLOR_M = '#1565C0'   # azul – masculino
COLOR_F = '#C62828'   # rojo  – femenino

# =============================================================================
# FUNCIONES
# =============================================================================

def cargar_wav(archivo):
    """
    Lee un archivo .wav y devuelve (fs, señal normalizada en float64).
    Convierte a mono si es estéreo.
    """
    fs, datos = wavfile.read(archivo)
    if datos.ndim > 1:
        datos = datos.mean(axis=1)
    datos = datos.astype(np.float64)
    maximo = np.max(np.abs(datos))
    if maximo > 0:
        datos /= maximo
    return fs, datos


def frecuencia_fundamental(senal, fs, genero='M'):
    """
    Estima F0 por autocorrelación normalizada.
    Rango: 50–300 Hz (hombres), 100–500 Hz (mujeres).
    """
    f_min, f_max = (50, 300) if genero == 'M' else (100, 500)
    lag_min = int(fs / f_max)
    lag_max = int(fs / f_min)

    corr = np.correlate(senal, senal, mode='full')
    corr = corr[len(corr)//2:]
    if corr[0] != 0:
        corr /= corr[0]

    segmento = corr[lag_min:lag_max]
    if len(segmento) == 0:
        return 0.0
    idx_pico = np.argmax(segmento) + lag_min
    return fs / idx_pico if idx_pico > 0 else 0.0


def brillo_espectral(freqs, magnitud):
    """Centroide espectral – indica el 'brillo' percibido de la voz."""
    suma = magnitud.sum()
    return np.sum(freqs * magnitud) / suma if suma > 0 else 0.0


def frecuencia_media(freqs, magnitud):
    """Frecuencia media ponderada por la magnitud espectral."""
    suma = magnitud.sum()
    return np.sum(freqs * magnitud) / suma if suma > 0 else 0.0


def intensidad_rms(senal):
    """Energía RMS de la señal (proporcional a la intensidad)."""
    return np.sqrt(np.mean(senal ** 2))


# =============================================================================
# PROCESAMIENTO PRINCIPAL
# =============================================================================
print("=" * 65)
print("  PARTE A – ADQUISICIÓN Y ANÁLISIS ESPECTRAL DE LA VOZ")
print("  Universidad Militar Nueva Granada – PDS")
print("=" * 65)

resultados = []

for archivo, genero, etiqueta in ARCHIVOS_VOZ:
    if not os.path.exists(archivo):
        print(f"\n⚠  Archivo no encontrado: {archivo}  (se omite)")
        continue

    print(f"\n{'─'*55}")
    print(f"  Procesando: {etiqueta}  [{archivo}]")
    print(f"{'─'*55}")

    # ── Cargar señal ──────────────────────────────────────────────────────
    fs, senal = cargar_wav(archivo)
    N        = len(senal)
    t        = np.arange(N) / fs
    duracion = N / fs
    f_nyquist = fs / 2

    print(f"  Fs (muestreo)     : {fs} Hz")
    print(f"  Frecuencia Nyquist: {f_nyquist} Hz")
    print(f"  Duración          : {duracion:.3f} s")
    print(f"  Muestras          : {N}")

    # ── Estadísticos temporales ───────────────────────────────────────────
    mu   = np.mean(senal)
    me   = np.median(senal)
    s    = np.std(senal, ddof=1)
    vmax = senal.max()
    vmin = senal.min()
    rms  = intensidad_rms(senal)

    print(f"  Media             : {mu:.6f}")
    print(f"  Mediana           : {me:.6f}")
    print(f"  Desv. estándar    : {s:.6f}")
    print(f"  Máximo            : {vmax:.6f}")
    print(f"  Mínimo            : {vmin:.6f}")
    print(f"  RMS (Intensidad)  : {rms:.6f}")

    # ── Transformada de Fourier ───────────────────────────────────────────
    Y        = np.fft.rfft(senal)
    freqs    = np.fft.rfftfreq(N, d=1/fs)
    magnitud = np.abs(Y)
    fase     = np.angle(Y)
    psd      = (magnitud ** 2) / (N * fs)

    # ── Características espectrales ───────────────────────────────────────
    f0      = frecuencia_fundamental(senal, fs, genero)
    f_med   = frecuencia_media(freqs, magnitud)
    brillo  = brillo_espectral(freqs, magnitud)

    print(f"  F0 fundamental    : {f0:.2f} Hz")
    print(f"  Frecuencia media  : {f_med:.2f} Hz")
    print(f"  Brillo (centroid) : {brillo:.2f} Hz")

    resultados.append({
        'archivo' : archivo,
        'etiqueta': etiqueta,
        'genero'  : genero,
        'fs'      : fs,
        'N'       : N,
        'duracion': duracion,
        't'       : t,
        'senal'   : senal,
        'freqs'   : freqs,
        'magnitud': magnitud,
        'fase'    : fase,
        'psd'     : psd,
        'mu'      : mu,
        'me'      : me,
        's'       : s,
        'vmax'    : vmax,
        'vmin'    : vmin,
        'rms'     : rms,
        'f0'      : f0,
        'f_media' : f_med,
        'brillo'  : brillo,
    })

if not resultados:
    print("\n✗ No se encontraron archivos .wav. Verifica ARCHIVOS_VOZ.")
    exit(1)

# =============================================================================
# GRÁFICA 1 – SEÑALES EN EL DOMINIO DEL TIEMPO
# =============================================================================
print(f"\n{'='*65}")
print("  GENERANDO GRÁFICAS")
print(f"{'='*65}")

n_cols = 3
n_rows = (len(resultados) + n_cols - 1) // n_cols

fig1, axes = plt.subplots(n_rows, n_cols, figsize=(18, 4 * n_rows))
fig1.suptitle("Señales de Voz – Dominio del Tiempo",
              fontsize=15, fontweight='bold', y=1.01)
axes = np.array(axes).flatten()

for i, r in enumerate(resultados):
    ax    = axes[i]
    color = COLOR_M if r['genero'] == 'M' else COLOR_F

    ax.plot(r['t'], r['senal'], color=color, lw=0.6, alpha=0.85)
    ax.axhline(r['mu'], color='black', ls='--', lw=1.1,
               label=f"Media = {r['mu']:.5f}")
    ax.axhline(r['mu'] + r['s'], color='green', ls=':', lw=1.0,
               label=f"μ+σ = {r['mu']+r['s']:.4f}")
    ax.axhline(r['mu'] - r['s'], color='green', ls=':', lw=1.0,
               label=f"μ-σ = {r['mu']-r['s']:.4f}")

    ax.set_title(
        f"{r['etiqueta']}  |  Fs={r['fs']} Hz  |  {r['duracion']:.2f} s",
        fontsize=10, fontweight='bold')
    ax.set_xlabel("Tiempo (s)", fontsize=9)
    ax.set_ylabel("Amplitud norm.", fontsize=9)
    ax.legend(fontsize=7, loc='upper right')
    ax.grid(True, alpha=0.3)

for j in range(len(resultados), len(axes)):
    axes[j].set_visible(False)

plt.tight_layout()
ruta1 = os.path.join(CARPETA_SALIDA, f"A1_tiempo_{timestamp}.png")
plt.savefig(ruta1, dpi=150, bbox_inches='tight')
plt.show()
print(f"  ✓ Señales en el tiempo  → {ruta1}")

# =============================================================================
# GRÁFICA 2 – FFT (magnitud + fase) por señal
# =============================================================================
for r in resultados:
    color   = COLOR_M if r['genero'] == 'M' else COLOR_F
    xlim_hz = min(r['fs'] / 2, 8000)

    fig2, axes2 = plt.subplots(2, 1, figsize=(14, 7))
    fig2.suptitle(f"Transformada de Fourier  –  {r['etiqueta']}",
                  fontsize=13, fontweight='bold')

    # Magnitud – eje X logarítmico (dominio frecuencia)
    freqs_pos = r['freqs'][r['freqs'] > 0]
    mag_pos   = r['magnitud'][r['freqs'] > 0]
    axes2[0].plot(freqs_pos, mag_pos, color=color, lw=0.8)
    axes2[0].axvline(r['f0'],      color='#2E7D32', ls='--', lw=1.5,
                     label=f"F0 = {r['f0']:.1f} Hz")
    axes2[0].axvline(r['f_media'], color='#E65100', ls=':',  lw=1.4,
                     label=f"F. media = {r['f_media']:.1f} Hz")
    axes2[0].axvline(r['brillo'],  color='#F9A825', ls='-.', lw=1.4,
                     label=f"Brillo = {r['brillo']:.1f} Hz")
    axes2[0].set_title("|X(f)| – Espectro de Magnitud", fontsize=11, fontweight='bold')
    axes2[0].set_xlabel("Frecuencia (Hz) – escala logarítmica", fontsize=10)
    axes2[0].set_ylabel("Magnitud", fontsize=10)
    axes2[0].set_xscale('log')
    axes2[0].set_xlim(20, xlim_hz)
    axes2[0].legend(fontsize=9)
    axes2[0].grid(True, alpha=0.3, which='both')

    # Fase – eje X logarítmico (dominio frecuencia)
    fase_pos = r['fase'][r['freqs'] > 0]
    axes2[1].plot(freqs_pos, fase_pos, color='#6A1B9A', lw=0.7)
    axes2[1].set_title("∠X(f) – Espectro de Fase", fontsize=11, fontweight='bold')
    axes2[1].set_xlabel("Frecuencia (Hz) – escala logarítmica", fontsize=10)
    axes2[1].set_ylabel("Fase (rad)", fontsize=10)
    axes2[1].set_xscale('log')
    axes2[1].set_xlim(20, xlim_hz)
    axes2[1].grid(True, alpha=0.3, which='both')

    plt.tight_layout()
    nombre = r['archivo'].replace('.wav', '')
    ruta2  = os.path.join(CARPETA_SALIDA, f"A2_fft_{nombre}_{timestamp}.png")
    plt.savefig(ruta2, dpi=150, bbox_inches='tight')
    plt.show()
    print(f"  ✓ FFT {r['etiqueta']:12}    → {ruta2}")

# =============================================================================
# GRÁFICA 3 – PSD todas las señales
# =============================================================================
fig3, axes3 = plt.subplots(n_rows, n_cols, figsize=(18, 4 * n_rows))
fig3.suptitle("Densidad Espectral de Potencia (PSD)",
              fontsize=15, fontweight='bold', y=1.01)
axes3 = np.array(axes3).flatten()

for i, r in enumerate(resultados):
    ax    = axes3[i]
    color = COLOR_M if r['genero'] == 'M' else COLOR_F
    xlim_hz = min(r['fs'] / 2, 8000)

    freqs_pos = r['freqs'][r['freqs'] > 0]
    psd_pos   = r['psd'][r['freqs'] > 0]
    ax.semilogy(freqs_pos, psd_pos, color=color, lw=0.8)
    ax.axvline(r['f0'], color='#2E7D32', ls='--', lw=1.3,
               label=f"F0 = {r['f0']:.1f} Hz")
    ax.set_title(r['etiqueta'], fontsize=10, fontweight='bold')
    ax.set_xlabel("Frecuencia (Hz) – escala logarítmica", fontsize=9)
    ax.set_ylabel("V²/Hz", fontsize=9)
    ax.set_xscale('log')
    ax.set_xlim(20, xlim_hz)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3, which='both')

for j in range(len(resultados), len(axes3)):
    axes3[j].set_visible(False)

plt.tight_layout()
ruta3 = os.path.join(CARPETA_SALIDA, f"A3_psd_{timestamp}.png")
plt.savefig(ruta3, dpi=150, bbox_inches='tight')
plt.show()
print(f"  ✓ PSD                   → {ruta3}")

# =============================================================================
# GRÁFICA 4 – TABLA RESUMEN DE CARACTERÍSTICAS
# =============================================================================
fig4, ax4 = plt.subplots(figsize=(14, 4))
ax4.axis('off')
fig4.suptitle("Tabla Resumen – Características Espectrales (Parte A)",
              fontsize=13, fontweight='bold')

col_labels = ['Señal', 'Género', 'Fs (Hz)', 'F0 (Hz)',
              'F. Media (Hz)', 'Brillo (Hz)', 'RMS']
tabla_data = []
for r in resultados:
    gen_txt = 'Masculino' if r['genero'] == 'M' else 'Femenino'
    tabla_data.append([
        r['etiqueta'], gen_txt, str(r['fs']),
        f"{r['f0']:.1f}", f"{r['f_media']:.1f}",
        f"{r['brillo']:.1f}", f"{r['rms']:.5f}"
    ])

tabla = ax4.table(
    cellText=tabla_data,
    colLabels=col_labels,
    cellLoc='center',
    loc='center'
)
tabla.auto_set_font_size(False)
tabla.set_fontsize(10)
tabla.scale(1.2, 1.8)

# Colorear encabezado y filas por género
for j in range(len(col_labels)):
    tabla[0, j].set_facecolor('#37474F')
    tabla[0, j].set_text_props(color='white', fontweight='bold')

for i, r in enumerate(resultados):
    color_fila = '#BBDEFB' if r['genero'] == 'M' else '#FFCDD2'
    for j in range(len(col_labels)):
        tabla[i+1, j].set_facecolor(color_fila)

plt.tight_layout()
ruta4 = os.path.join(CARPETA_SALIDA, f"A4_tabla_{timestamp}.png")
plt.savefig(ruta4, dpi=150, bbox_inches='tight')
plt.show()
print(f"  ✓ Tabla resumen         → {ruta4}")

# =============================================================================
# RESUMEN EN CONSOLA
# =============================================================================
print(f"\n{'='*65}")
print("  RESUMEN PARTE A")
print(f"{'='*65}")
header = f"  {'Señal':<12} {'Gén':^4} {'Fs':>6}  {'F0(Hz)':>8}  {'FMedia':>8}  {'Brillo':>8}  {'RMS':>9}"
print(header)
print("  " + "─" * (len(header)-2))
for r in resultados:
    print(f"  {r['etiqueta']:<12} {r['genero']:^4} {r['fs']:>6}  "
          f"{r['f0']:>8.1f}  {r['f_media']:>8.1f}  "
          f"{r['brillo']:>8.1f}  {r['rms']:>9.5f}")

print(f"\n  ✓ Todas las figuras guardadas en: '{CARPETA_SALIDA}/'")
print(f"{'='*65}\n")