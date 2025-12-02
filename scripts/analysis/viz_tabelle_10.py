"""
Visualisierung Tabelle 10: Wartbarkeitsmetriken des neu hinzugefügten Codes
5 Metriken × 5 Varianten
"""

import matplotlib.pyplot as plt
import numpy as np

# Daten aus Tabelle 10
metriken = ['TD/LOC', 'Smells/KLOC', 'CC/KLOC', 'CogC/Func', 'Dup. %']
varianten = ['Reference', 'Copilot-Zero', 'Copilot-Few', 'Cursor-Zero', 'Cursor-Few']

# Werte aus der Tabelle
data = {
    'TD/LOC': [0.1191, 0.1225, 0.0885, 0.1196, 0.1304],
    'Smells/KLOC': [22.81, 17.22, 12.96, 14.21, 17.47],
    'CC/KLOC': [100.01, 74.66, 40.22, 91.19, 136.11],
    'CogC/Func': [1.18, 1.68, 1.18, 1.13, 1.35],
    'Dup. %': [0.00, 0.98, 0.86, 0.00, 2.49]
}

# Farben (colorblind-friendly)
colors = {
    'Reference': '#2E7D32',
    'Copilot-Zero': '#64B5F6',
    'Copilot-Few': '#1976D2',
    'Cursor-Zero': '#FFB74D',
    'Cursor-Few': '#F57C00'
}

# Figur mit 5 Subplots
fig, axes = plt.subplots(1, 5, figsize=(16, 4))
fig.subplots_adjust(wspace=0.35)

# Für jede Metrik ein Subplot
for idx, (ax, metrik) in enumerate(zip(axes, metriken)):
    values = data[metrik]
    x = np.arange(len(varianten))
    bar_width = 0.7
    
    # Balken zeichnen
    bars = ax.bar(x, values, bar_width, 
                   color=[colors[v] for v in varianten],
                   edgecolor='black',
                   linewidth=0.8)
    
    # Werte über Balken
    for bar, value in zip(bars, values):
        height = bar.get_height()
        if metrik in ['TD/LOC', 'CogC/Func']:
            label = f'{value:.3f}'
        elif metrik == 'Dup. %':
            label = f'{value:.2f}'
        else:
            label = f'{value:.1f}'
        
        ax.text(bar.get_x() + bar.get_width()/2., height,
               label, ha='center', va='bottom', fontsize=7, fontweight='bold')
    
    # Achsenbeschriftung
    ax.set_ylabel(metrik, fontsize=10, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(varianten, fontsize=7, rotation=45, ha='right')
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_ylim(bottom=0)

# Layout optimieren
plt.tight_layout()

# Speichern
plt.savefig('/mnt/user-data/outputs/wartbarkeitsmetriken.pdf', 
            dpi=300, bbox_inches='tight')
plt.savefig('/mnt/user-data/outputs/wartbarkeitsmetriken.png', 
            dpi=300, bbox_inches='tight')

print("✅ Grafik 3 erstellt: Wartbarkeitsmetriken")
print("   - wartbarkeitsmetriken.pdf")
print("   - wartbarkeitsmetriken.png")

plt.show()
