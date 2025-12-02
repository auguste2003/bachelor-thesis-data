"""
Visualisierung der Test Success Rate (Tabelle 7)
Gruppiertes Balkendiagramm für Bachelorarbeit

Erstellt eine hochwertige, publikationsreife Grafik
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Daten aus Tabelle 7 (New Code Metrics – Testmetriken)
data = {
    'Feature': [
        'LearningBlock', 'LearningBlock', 'LearningBlock', 'LearningBlock', 'LearningBlock',
        'CommentOnBlock', 'CommentOnBlock', 'CommentOnBlock',
        'NotifyReviewer', 'NotifyReviewer', 'NotifyReviewer', 'NotifyReviewer',
        'ExportReview', 'ExportReview', 'ExportReview', 'ExportReview', 'ExportReview'
    ],
    'Variante': [
        'Reference', 'Copilot-Zero', 'Copilot-Few', 'Cursor-Zero', 'Cursor-Few',
        'Reference', 'Copilot-Zero', 'Copilot-Few',
        'Reference', 'Copilot-Zero', 'Copilot-Few', 'Cursor-Few',
        'Reference', 'Copilot-Zero', 'Copilot-Few', 'Cursor-Zero', 'Cursor-Few'
    ],
    'SR%': [
        100.0, 70.0, 100.0, 54.5, 83.3,
        100.0, 96.2, 75.9,
        100.0, np.nan, 96.2, 100.0,  # Copilot-Zero hat keine Tests
        100.0, 67.9, 84.8, 90.9, 29.4
    ]
}

df = pd.DataFrame(data)

# Features und Varianten
features = ['LearningBlock', 'CommentOnBlock', 'NotifyReviewer', 'ExportReview']
varianten = ['Reference', 'Copilot-Zero', 'Copilot-Few', 'Cursor-Zero', 'Cursor-Few']

# Farben (colorblind-friendly palette)
colors = {
    'Reference': '#2E7D32',      # Dunkelgrün
    'Copilot-Zero': '#64B5F6',   # Hellblau
    'Copilot-Few': '#1976D2',    # Dunkelblau
    'Cursor-Zero': '#FFB74D',    # Hellorange
    'Cursor-Few': '#F57C00'      # Dunkelorange
}

# Figur erstellen
fig, ax = plt.subplots(figsize=(12, 6))

# Balkenbreite und Position
bar_width = 0.15
x = np.arange(len(features))

# Balken zeichnen
for i, variante in enumerate(varianten):
    values = []
    for feature in features:
        mask = (df['Feature'] == feature) & (df['Variante'] == variante)
        if mask.any():
            value = df.loc[mask, 'SR%'].values[0]
            values.append(value if not np.isnan(value) else 0)
        else:
            values.append(0)
    
    offset = (i - 2) * bar_width
    bars = ax.bar(x + offset, values, bar_width, 
                   label=variante, 
                   color=colors[variante],
                   edgecolor='black',
                   linewidth=0.5)
    
    # Werte über den Balken anzeigen
    for j, (bar, value) in enumerate(zip(bars, values)):
        if value > 0:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                   f'{value:.1f}%' if value < 100 else '100%',
                   ha='center', va='bottom', fontsize=8)

# Gestaltung
ax.set_xlabel('Feature', fontsize=12, fontweight='bold')
ax.set_ylabel('Test Success Rate (%)', fontsize=12, fontweight='bold')
# Kein Titel - wird in LaTeX caption hinzugefügt
ax.set_xticks(x)
ax.set_xticklabels(features, fontsize=10)
ax.set_ylim(0, 110)
ax.set_yticks(range(0, 101, 10))
ax.legend(loc='lower right', fontsize=9, framealpha=0.9)
ax.grid(axis='y', alpha=0.3, linestyle='--')

# Horizontale Linie bei 100%
ax.axhline(y=100, color='gray', linestyle='--', linewidth=0.8, alpha=0.5)

# Layout optimieren
plt.tight_layout()

# Speichern
plt.savefig('test_success_rate.pdf', dpi=300, bbox_inches='tight')
plt.savefig('test_success_rate.png', dpi=300, bbox_inches='tight')

print("✅ Grafiken erstellt:")
print("   - test_success_rate.pdf (für LaTeX)")
print("   - test_success_rate.png (für Vorschau)")

plt.show()
