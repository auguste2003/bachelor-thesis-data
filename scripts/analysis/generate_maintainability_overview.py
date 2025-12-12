#!/usr/bin/env python3
"""
Script: generate_maintainability_overview.py
Beschreibung: Erstellt das Wartbarkeitsmetriken-Überblicks-Diagramm (Abbildung in 6.3)
Eingabe: pr_new_code_metrics_normalized.csv oder summary_new_code_metrics.csv
Ausgabe: maintainability_metrics_overview.pdf
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Daten aus der Arbeit (Tabelle 10)
variants = ['Referenz', 'Copilot-Zero', 'Copilot-Few', 'Cursor-Zero', 'Cursor-Few']

data = {
    'TD/LOC': [0.1191, 0.1225, 0.0885, 0.1196, 0.1304],
    'Smells/KLOC': [22.81, 17.22, 12.96, 14.21, 17.47],
    'CC/KLOC': [100.01, 74.66, 40.22, 91.19, 136.11],
    'CogC/Func': [1.18, 1.68, 1.18, 1.13, 1.35],
    'Dup%': [0.00, 0.98, 0.86, 0.00, 2.49]
}

df = pd.DataFrame(data, index=variants)

# Farben (wie in der Arbeit beschrieben)
colors = {
    'Referenz': '#1f77b4',
    'Copilot-Zero': '#ff7f0e', 
    'Copilot-Few': '#9467bd',  # violett (dominiert)
    'Cursor-Zero': '#2ca02c',
    'Cursor-Few': '#d62728'    # orange (schlechteste)
}

# Erstelle Subplot-Grid (2x3)
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Wartbarkeitsmetriken des neu hinzugefügten Codes nach Implementierungsmethode',
             fontsize=16, fontweight='bold', y=0.995)

metrics = list(data.keys())
metric_labels = ['Technical Debt / LOC', 'Code Smells / KLOC', 
                'Cyclomatic Complexity / KLOC', 'Cognitive Complexity / Funktion',
                'Duplikation (%)']

# Plotte jede Metrik
for idx, (metric, label) in enumerate(zip(metrics, metric_labels)):
    row = idx // 3
    col = idx % 3
    ax = axes[row, col]
    
    values = df[metric]
    bars = ax.bar(range(len(variants)), values, 
                  color=[colors[v] for v in variants],
                  edgecolor='black', linewidth=1.2)
    
    # Werte auf Balken
    for i, (bar, val) in enumerate(zip(bars, values)):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{val:.2f}' if metric != 'Smells/KLOC' else f'{val:.1f}',
               ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    ax.set_title(label, fontsize=11, fontweight='bold', pad=10)
    ax.set_xticks(range(len(variants)))
    ax.set_xticklabels(variants, rotation=45, ha='right', fontsize=9)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_ylabel('Wert', fontsize=10)

# Letzte Subplot leer lassen (nur 5 Metriken)
axes[1, 2].axis('off')

# Layout
plt.tight_layout(rect=[0, 0, 1, 0.98])

# Speichern
plt.savefig('maintainability_metrics_overview.pdf', format='pdf', dpi=300, bbox_inches='tight')
print("✅ Diagramm erstellt: maintainability_metrics_overview.pdf")

plt.show()
