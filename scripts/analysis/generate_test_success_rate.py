#!/usr/bin/env python3
"""
Script: generate_test_success_rate.py
Beschreibung: Erstellt das Test Success Rate Diagramm nach Feature und Variante
Eingabe: branches_overall_metrics_normalized.csv oder manuelle Daten
Ausgabe: test_success_rate.pdf
"""

import matplotlib.pyplot as plt
import numpy as np

# Daten (aus der Arbeit)
features = ['LearningBlock', 'CommentOnBlock', 'NotifyReviewer', 'ExportReviewCatalog']
variants = ['Referenz', 'Copilot-Zero', 'Copilot-Few', 'Cursor-Zero', 'Cursor-Few']

# Test Success Rates (in Prozent)
# Zeilen = Features, Spalten = Varianten
data = np.array([
    [100.0, 70.0, 100.0, 54.5, 83.3],  # LearningBlock
    [100.0, 96.2, 75.9, np.nan, np.nan],  # CommentOnBlock
    [100.0, 0.0, 96.2, np.nan, 100.0],  # NotifyReviewer
    [100.0, 67.9, 84.8, 90.9, 29.4]   # ExportReviewCatalog
])

# Farben für die Varianten
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Erstelle Diagramm
fig, ax = plt.subplots(figsize=(12, 6))

x = np.arange(len(features))
width = 0.15

# Plotte Balken für jede Variante
for i, variant in enumerate(variants):
    offset = (i - 2) * width
    bars = ax.bar(x + offset, data[:, i], width, label=variant, color=colors[i])
    
    # Füge Werte auf den Balken hinzu
    for j, bar in enumerate(bars):
        height = bar.get_height()
        if not np.isnan(height):
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}%',
                   ha='center', va='bottom', fontsize=8)

# Formatierung
ax.set_xlabel('Feature', fontsize=12, fontweight='bold')
ax.set_ylabel('Test Success Rate (%)', fontsize=12, fontweight='bold')
ax.set_title('Test Success Rate nach Feature und Implementierungsvariante', 
             fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(features, rotation=0)
ax.set_ylim(0, 110)
ax.legend(loc='upper right', frameon=True, shadow=True)
ax.grid(axis='y', alpha=0.3, linestyle='--')

# Layout optimieren
plt.tight_layout()

# Speichern
plt.savefig('test_success_rate.pdf', format='pdf', dpi=300, bbox_inches='tight')
print("✅ Diagramm erstellt: test_success_rate.pdf")

plt.show()
