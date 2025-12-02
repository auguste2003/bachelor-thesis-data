"""
Visualisierung Tabelle 15: Vergleich der Implementierungsmethoden
Gruppiertes Balkendiagramm mit 5 Metriken
"""

import matplotlib.pyplot as plt
import numpy as np

# Daten aus Tabelle 15
metriken = ['SR %', 'TD/LOC', 'CC/KLOC', 'CogC/Func', 'Smells/KLOC']
methoden = ['Reference', 'Copilot', 'Cursor']

# Werte aus der Tabelle
data = {
    'SR %': [100.0, 73.9, 71.6],
    'TD/LOC': [0.1191, 0.1055, 0.1261],
    'CC/KLOC': [100.01, 57.44, 118.14],
    'CogC/Func': [1.18, 1.43, 1.26],
    'Smells/KLOC': [22.81, 15.09, 16.16]
}

# Farben (colorblind-friendly)
colors = {
    'Reference': '#2E7D32',    # Dunkelgrün
    'Copilot': '#1976D2',      # Blau
    'Cursor': '#F57C00'        # Orange
}

# Figur mit 5 Subplots (eine Zeile, 5 Spalten)
fig, axes = plt.subplots(1, 5, figsize=(16, 4))
fig.subplots_adjust(wspace=0.3)

# Balkenbreite und Positionen
x = np.arange(len(methoden))
bar_width = 0.6

# Für jede Metrik ein Subplot
for idx, (ax, metrik) in enumerate(zip(axes, metriken)):
    values = data[metrik]
    
    # Balken zeichnen
    bars = ax.bar(x, values, bar_width, 
                   color=[colors[m] for m in methoden],
                   edgecolor='black',
                   linewidth=0.8)
    
    # Werte über Balken
    for bar, value in zip(bars, values):
        height = bar.get_height()
        # Formatierung je nach Metrik
        if metrik == 'SR %':
            label = f'{value:.1f}%'
        elif metrik in ['TD/LOC', 'CogC/Func']:
            label = f'{value:.3f}'
        else:
            label = f'{value:.1f}'
        
        ax.text(bar.get_x() + bar.get_width()/2., height,
               label, ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    # Achsenbeschriftung
    ax.set_ylabel(metrik, fontsize=10, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(methoden, fontsize=9, rotation=0)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Y-Achse bei 0 starten
    ax.set_ylim(bottom=0)

# Layout optimieren
plt.tight_layout()

# Speichern
plt.savefig('/mnt/user-data/outputs/implementierungsmethoden_vergleich.pdf', 
            dpi=300, bbox_inches='tight')
plt.savefig('/mnt/user-data/outputs/implementierungsmethoden_vergleich.png', 
            dpi=300, bbox_inches='tight')

print("✅ Grafik 1 erstellt: Vergleich der Implementierungsmethoden")
print("   - implementierungsmethoden_vergleich.pdf")
print("   - implementierungsmethoden_vergleich.png")

plt.show()
