#!/usr/bin/env python3
"""
Script: analyze_metrics_and_create_tables.py
Beschreibung: Analysiert alle CSV-Dateien und erstellt Tabellendaten für LaTeX
Eingabe: Alle CSV-Dateien (branches_overall_metrics_normalized.csv, etc.)
Ausgabe: LaTeX-Tabellen-Code und statistische Zusammenfassungen
"""

import pandas as pd
import numpy as np

print("=" * 80)
print("ANALYSE DER CODEQUALITÄTSMETRIKEN")
print("=" * 80)

# ===========================
# 1. BRANCHES OVERALL METRICS
# ===========================
print("\n[1] BRANCHES OVERALL METRICS ANALYSIS")
print("-" * 80)

df_branches = pd.read_csv('../../data/processed/branches_overall_metrics_normalized.csv', sep=';')

# Baseline extrahieren
baseline = df_branches[df_branches['Branch'] == 'main'].iloc[0]
print(f"\n✓ BASELINE (Main Branch):")
print(f"  Smells/KLOC: {baseline['Smells_per_KLOC']:.2f}")
print(f"  CC/KLOC: {baseline['CC_per_KLOC']:.2f}")
print(f"  CogC/Function: {baseline['CogC_per_Function']:.2f}")
print(f"  Duplication %: {baseline['Duplication %']:.2f}")

# Features filtern (ohne Main)
features = df_branches[df_branches['Variant'] != 'Main'].copy()

# Delta berechnen
features['Delta_Smells'] = features['Smells_per_KLOC'] - baseline['Smells_per_KLOC']
features['Delta_CC'] = features['CC_per_KLOC'] - baseline['CC_per_KLOC']
features['Delta_CogC'] = features['CogC_per_Function'] - baseline['CogC_per_Function']
features['Delta_Dup'] = features['Duplication %'] - baseline['Duplication %']

# Gruppieren nach Variante
summary = features.groupby('Variant').agg({
    'Delta_Smells': 'mean',
    'Delta_CC': 'mean',
    'Delta_CogC': 'mean',
    'Delta_Dup': 'mean',
    'Test_Success_Rate': 'mean'
}).round(2)

variants_order = ['Copilot-Few', 'Copilot-Zero', 'Cursor-Few', 'Cursor-Zero', 'Reference']
summary = summary.reindex(variants_order)

print(f"\n✓ DELTA-TABELLE (Baseline → Overall):")
print(summary)

# LaTeX-Tabelle erstellen
print("\n✓ LaTeX-Code für Tabelle (6.4.2):")
print("\\begin{table}[htbp]")
print("\\centering")
print("\\caption{Durchschnittliche Änderung struktureller Qualitätsmetriken (Baseline → Overall)}")
print("\\label{tab:delta_structural_quality}")
print("\\small")
print("\\begin{tabular}{lrrrr}")
print("\\toprule")
print("\\textbf{Variante} & \\textbf{∆ Smells/KLOC} & \\textbf{∆ CC/KLOC} & \\textbf{∆ CogC/Func} & \\textbf{∆ Dup\\,\\%} \\\\")
print("\\midrule")

for variant in variants_order:
    row = summary.loc[variant]
    print(f"{variant:15} & ${row['Delta_Smells']:+6.2f}$ & ${row['Delta_CC']:+6.2f}$ & ${row['Delta_CogC']:+6.2f}$ & ${row['Delta_Dup']:+6.2f}$ \\\\")

print("\\bottomrule")
print("\\end{tabular}")
print("\\smallskip\n")
print("\\footnotesize")
print("\\textit{Anmerkung:} Negative Werte = Verbesserung, positive Werte = Verschlechterung. \\\\")
print("Fett markiert: Beste/schlechteste Werte pro Metrik.")
print("\\end{table}")

# ===========================
# 2. PR NEW CODE METRICS
# ===========================
print("\n\n[2] PR NEW CODE METRICS ANALYSIS")
print("-" * 80)

df_pr = pd.read_csv('../../data/processed/pr_new_code_metrics_normalized.csv', sep=';')

# Nach Variante gruppieren
pr_summary = df_pr.groupby('Variant').agg({
    'TD_per_LOC': 'mean',
    'Smells_per_KLOC': 'mean',
    'CC_per_KLOC': 'mean',
    'CogC_per_Function': 'mean',
    'Duplication %': 'mean',
    'Test_Success_Rate': 'mean'
}).round(2)

print(f"\n✓ NEW CODE METRIKEN (Mittelwerte):")
print(pr_summary)

# LaTeX-Tabelle für Wartbarkeit (Tabelle 10)
print("\n✓ LaTeX-Code für Tabelle 10 (Wartbarkeitsmetriken):")
print("\\begin{table}[H]")
print("\\centering")
print("\\caption{Wartbarkeitsmetriken des neu hinzugefügten Codes (Mittelwerte)}")
print("\\label{tab:new_code_maintainability}")
print("\\small")
print("\\begin{tabular}{lrrrrr}")
print("\\toprule")
print("\\textbf{Variante} & \\textbf{TD/LOC} & \\textbf{Smells/KLOC} & \\textbf{CC/KLOC} & \\textbf{CogC/Func} & \\textbf{Dup. \\%} \\\\")
print("\\midrule")

for variant in variants_order:
    if variant in pr_summary.index:
        row = pr_summary.loc[variant]
        print(f"{variant:15} & {row['TD_per_LOC']:.4f} & {row['Smells_per_KLOC']:.2f} & {row['CC_per_KLOC']:.2f} & {row['CogC_per_Function']:.2f} & {row['Duplication %']:.2f} \\\\")

print("\\bottomrule")
print("\\end{tabular}")
print("\\smallskip\n")
print("\\footnotesize")
print("\\textit{Anmerkung:} Fett markiert: Beste/schlechteste Werte pro Metrik.")
print("\\end{table}")

# ===========================
# 3. PROMPT-STRATEGIE VERGLEICH
# ===========================
print("\n\n[3] PROMPT-STRATEGIE VERGLEICH")
print("-" * 80)

# Gruppiere nach Tool und Prompt-Strategie
df_pr['Tool'] = df_pr['Variant'].apply(lambda x: 'Copilot' if 'Copilot' in x else 'Cursor' if 'Cursor' in x else 'Referenz')
df_pr['Prompt'] = df_pr['Variant'].apply(lambda x: 'Few-Shot' if 'Few' in x else 'Zero-Shot' if 'Zero' in x else 'Manual')

prompt_comparison = df_pr[df_pr['Tool'] != 'Referenz'].groupby(['Tool', 'Prompt']).agg({
    'Test_Success_Rate': 'mean',
    'TD_per_LOC': 'mean',
    'CC_per_KLOC': 'mean',
    'CogC_per_Function': 'mean',
    'Smells_per_KLOC': 'mean'
}).round(2)

print("\n✓ PROMPT-STRATEGIE VERGLEICH:")
print(prompt_comparison)

# ===========================
# 4. TOOL VERGLEICH
# ===========================
print("\n\n[4] TOOL VERGLEICH (ZUSAMMENFASSUNG)")
print("-" * 80)

tool_comparison = df_pr.groupby('Tool').agg({
    'Test_Success_Rate': 'mean',
    'TD_per_LOC': 'mean',
    'CC_per_KLOC': 'mean',
    'CogC_per_Function': 'mean',
    'Smells_per_KLOC': 'mean'
}).round(2)

print("\n✓ TOOL-VERGLEICH (Mittelwerte über alle Features):")
print(tool_comparison)

print("\n" + "=" * 80)
print("✅ ANALYSE ABGESCHLOSSEN")
print("=" * 80)
