#!/usr/bin/env python3
"""
Script: generate_all_visualizations.py
Beschreibung: Master-Script zum Generieren aller Diagramme und Analysen
Führt alle anderen Scripts aus
"""

import subprocess
import sys
import os

print("=" * 80)
print("MASTER-SCRIPT: Generierung aller Visualisierungen")
print("=" * 80)

scripts = [
    {
        'name': 'Test Success Rate Diagramm',
        'file': 'generate_test_success_rate.py',
        'output': 'test_success_rate.pdf',
        'chapter': '6.2 - Funktionale Korrektheit'
    },
    {
        'name': 'Wartbarkeitsmetriken Überblick',
        'file': 'generate_maintainability_overview.py',
        'output': 'maintainability_metrics_overview.pdf',
        'chapter': '6.3 - Wartbarkeit des neuen Codes'
    },
    {
        'name': 'Delta Strukturelle Qualität',
        'file': 'generate_delta_structural_quality.py',
        'output': 'delta_structural_quality.pdf',
        'chapter': '6.4.2 - Einfluss auf strukturelle Qualität (durch Tabelle ersetzt)'
    },
    {
        'name': 'Metriken-Analyse und Tabellen',
        'file': 'analyze_metrics_and_create_tables.py',
        'output': 'Console Output (LaTeX-Code)',
        'chapter': 'Alle Kapitel - Generiert LaTeX-Tabellen-Code'
    }
]

print("\nFolgende Scripts werden ausgeführt:\n")
for i, script in enumerate(scripts, 1):
    print(f"{i}. {script['name']}")
    print(f"   Script: {script['file']}")
    print(f"   Output: {script['output']}")
    print(f"   Verwendung: {script['chapter']}")
    print()

print("=" * 80)
# input("Drücke ENTER zum Starten...")  # Commented out for non-interactive execution
print()

for i, script in enumerate(scripts, 1):
    print(f"\n[{i}/{len(scripts)}] Führe aus: {script['name']}")
    print("-" * 80)
    
    if not os.path.exists(script['file']):
        print(f"❌ FEHLER: Script nicht gefunden: {script['file']}")
        continue
    
    try:
        result = subprocess.run([sys.executable, script['file']], 
                              capture_output=False, 
                              text=True)
        
        if result.returncode == 0:
            print(f"✅ Erfolgreich abgeschlossen: {script['output']}")
        else:
            print(f"⚠️  Warnung: Script endete mit Code {result.returncode}")
            
    except Exception as e:
        print(f"❌ FEHLER beim Ausführen: {e}")

print("\n" + "=" * 80)
print("✅ ALLE SCRIPTS ABGESCHLOSSEN")
print("=" * 80)
print("\nGenerierte Dateien:")
print("  - test_success_rate.pdf")
print("  - maintainability_metrics_overview.pdf")
print("  - delta_structural_quality.pdf (optional)")
print("\nLaTeX-Code wurde in der Konsole ausgegeben.")
print("=" * 80)
