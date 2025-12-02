"""
Visualisierung Tabelle 13: Einfluss der Prompt-Strategie
Vergleich Zero-Shot vs. Few-Shot mit Delta-Visualisierung
"""

import matplotlib.pyplot as plt
import numpy as np

# Daten aus Tabelle 13
metriken = ['SR %', 'TD/LOC', 'CC/KLOC', 'CogC/Func', 'Smells/KLOC']

# Copilot
copilot_zero = [58.5, 0.1225, 74.66, 1.68, 17.22]
copilot_few = [89.2, 0.0885, 40.22, 1.18, 12.96]

# Cursor
cursor_zero = [72.7, 0.1196, 91.19, 1.13, 14.21]
cursor_few = [70.9, 0.1304, 136.11, 1.35, 17.47]

# Figur mit 5 Subplots
fig, axes = plt.subplots(1, 5, figsize=(16, 4))
fig.subplots_adjust(wspace=0.3)

# Farben
color_zero = '#64B5F6'  # Hellblau/Orange für Zero-Shot
color_few = '#1976D2'   # Dunkelblau/Orange für Few-Shot

# Für jede Metrik ein Subplot
for idx, (ax, metrik) in enumerate(zip(axes, metriken)):
    # Copilot-Werte
    cop_zero_val = copilot_zero[idx]
    cop_few_val = copilot_few[idx]
    
    # Cursor-Werte
    cur_zero_val = cursor_zero[idx]
    cur_few_val = cursor_few[idx]
    
    # Balkenbreite und Positionen
    x = np.array([0, 1, 3, 4])  # Copilot: 0,1 | Cursor: 3,4
    bar_width = 0.8
    
    # Copilot-Balken
    ax.bar(0, cop_zero_val, bar_width, color='#90CAF9', 
           edgecolor='black', linewidth=0.8, label='Zero-Shot')
    ax.bar(1, cop_few_val, bar_width, color='#1976D2', 
           edgecolor='black', linewidth=0.8, label='Few-Shot')
    
    # Cursor-Balken
    ax.bar(3, cur_zero_val, bar_width, color='#FFB74D', 
           edgecolor='black', linewidth=0.8)
    ax.bar(4, cur_few_val, bar_width, color='#F57C00', 
           edgecolor='black', linewidth=0.8)
    
    # Werte über Balken
    for pos, val in zip([0, 1, 3, 4], [cop_zero_val, cop_few_val, cur_zero_val, cur_few_val]):
        if metrik == 'SR %':
            label = f'{val:.1f}%'
        elif metrik in ['TD/LOC', 'CogC/Func']:
            label = f'{val:.3f}'
        else:
            label = f'{val:.1f}'
        ax.text(pos, val, label, ha='center', va='bottom', fontsize=8, fontweight='bold')
    
    # Pfeile für Veränderung (nur für Copilot und Cursor getrennt)
    # Copilot-Delta
    cop_delta = cop_few_val - cop_zero_val
    cop_color = 'green' if (metrik == 'SR %' and cop_delta > 0) or \
                           (metrik != 'SR %' and cop_delta < 0) else 'red'
    ax.annotate('', xy=(1, cop_few_val * 0.95), xytext=(0, cop_zero_val * 0.95),
                arrowprops=dict(arrowstyle='->', color=cop_color, lw=2, alpha=0.6))
    
    # Cursor-Delta
    cur_delta = cur_few_val - cur_zero_val
    cur_color = 'green' if (metrik == 'SR %' and cur_delta > 0) or \
                           (metrik != 'SR %' and cur_delta < 0) else 'red'
    ax.annotate('', xy=(4, cur_few_val * 0.95), xytext=(3, cur_zero_val * 0.95),
                arrowprops=dict(arrowstyle='->', color=cur_color, lw=2, alpha=0.6))
    
    # Achsenbeschriftung
    ax.set_ylabel(metrik, fontsize=10, fontweight='bold')
    ax.set_xticks([0.5, 3.5])
    ax.set_xticklabels(['Copilot', 'Cursor'], fontsize=9)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_ylim(bottom=0)
    
    # Legende nur beim ersten Subplot
    if idx == 0:
        ax.legend(loc='upper left', fontsize=8, framealpha=0.9)

# Layout optimieren
plt.tight_layout()

# Speichern
plt.savefig('/mnt/user-data/outputs/prompt_strategie_effekt.pdf', 
            dpi=300, bbox_inches='tight')
plt.savefig('/mnt/user-data/outputs/prompt_strategie_effekt.png', 
            dpi=300, bbox_inches='tight')

print("✅ Grafik 2 erstellt: Einfluss der Prompt-Strategie")
print("   - prompt_strategie_effekt.pdf")
print("   - prompt_strategie_effekt.png")

plt.show()
