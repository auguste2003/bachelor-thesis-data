#!/usr/bin/env python3
"""
Script: generate_delta_structural_quality.py
Beschreibung: Erstellt Delta-Diagramm für strukturelle Qualität (Baseline → Overall)
              HINWEIS: In finaler Arbeit durch Tabelle ersetzt
Eingabe: branches_overall_metrics_normalized.csv
Ausgabe: delta_structural_quality.pdf
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Daten aus branches_overall_metrics_normalized.csv
# Baseline (Main Branch)
baseline = {
    'Smells_per_KLOC': 80.08,
    'CC_per_KLOC': 81.52,
    'CogC_per_Function': 1.48,
    'Duplication_pct': 5.50
}

# Overall Durchschnitte (aus Analyse)
overall = {
    'Copilot-Few': {
        'Smells_per_KLOC': 76.76,
        'CC_per_KLOC': 84.62,
        'CogC_per_Function': 1.30,
        'Duplication_pct': 4.80
    },
    'Copilot-Zero': {
        'Smells_per_KLOC': 71.93,
        'CC_per_KLOC': 84.12,
        'CogC_per_Function': 1.38,
        'Duplication_pct': 4.57
    },
    'Cursor-Few': {
        'Smells_per_KLOC': 74.55,
        'CC_per_KLOC': 90.70,
        'CogC_per_Function': 1.36,
        'Duplication_pct': 5.40
    },
    'Cursor-Zero': {
        'Smells_per_KLOC': 75.07,
        'CC_per_KLOC': 89.02,
        'CogC_per_Function': 1.44,
        'Duplication_pct': 5.07
    },
    'Referenz': {
        'Smells_per_KLOC': 83.39,
        'CC_per_KLOC': 84.16,
        'CogC_per_Function': 1.31,
        'Duplication_pct': 4.77
    }
}

# Berechne Deltas
variants = ['Copilot-Few', 'Copilot-Zero', 'Cursor-Few', 'Cursor-Zero', 'Referenz']
metrics = ['Smells_per_KLOC', 'CC_per_KLOC', 'CogC_per_Function', 'Duplication_pct']
metric_labels = ['∆ Smells/KLOC', '∆ CC/KLOC', '∆ CogC/Func', '∆ Dup%']

deltas = {}
for variant in variants:
    deltas[variant] = {}
    for metric in metrics:
        deltas[variant][metric] = overall[variant][metric] - baseline[metric]

# Erstelle Subplot (2x2)
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Durchschnittliche Änderung struktureller Qualitätsmetriken (Baseline → Overall)',
             fontsize=14, fontweight='bold')

colors = ['#9467bd', '#ff7f0e', '#d62728', '#2ca02c', '#1f77b4']

for idx, (metric, label) in enumerate(zip(metrics, metric_labels)):
    row = idx // 2
    col = idx % 2
    ax = axes[row, col]
    
    values = [deltas[v][metric] for v in variants]
    bar_colors = ['green' if v < 0 else 'red' for v in values]
    
    bars = ax.barh(range(len(variants)), values, color=bar_colors, alpha=0.7, edgecolor='black')
    
    # Werte auf Balken
    for i, (bar, val) in enumerate(zip(bars, values)):
        width = bar.get_width()
        ax.text(width, bar.get_y() + bar.get_height()/2.,
               f'{val:+.2f}',
               ha='left' if width > 0 else 'right',
               va='center', fontsize=10, fontweight='bold')
    
    ax.set_title(label, fontsize=12, fontweight='bold')
    ax.set_yticks(range(len(variants)))
    ax.set_yticklabels(variants, fontsize=10)
    ax.axvline(0, color='black', linewidth=1.5)
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    ax.set_xlabel('Änderung', fontsize=10)

plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.savefig('delta_structural_quality.pdf', format='pdf', dpi=300, bbox_inches='tight')
print("✅ Diagramm erstellt: delta_structural_quality.pdf")
print("⚠️  HINWEIS: In finaler Arbeit durch Tabelle ersetzt (siehe 6.4.2)")

plt.show()
