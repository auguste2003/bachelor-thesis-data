#!/usr/bin/env python3
"""
Table 15: Tool Comparison: Copilot vs. Cursor (Averages over all features)
Calculates the average quality metrics for Copilot and Cursor
across all features and prompt strategies
"""

import csv
from collections import defaultdict

def calculate_tool_comparison():
    """
    Calculates averages for SR%, TD/LOC, CogC/Func, Smells/KLOC by tool
    """
    # Collect data: tool -> metric -> [values]
    data = defaultdict(lambda: defaultdict(list))

    # Read CSV file
    with open('../../data/processed/pr_new_code_metrics_normalized.csv', 'r') as f:
        reader = csv.DictReader(f, delimiter=';')

        for row in reader:
            variant = row['Variant']

            # Only Copilot and Cursor (skip Reference)
            if not variant or variant == 'Reference':
                continue

            # Determine tool
            if 'Copilot' in variant:
                tool = 'Copilot'
            elif 'Cursor' in variant:
                tool = 'Cursor'
            else:
                continue

            # SR% (Test Success Density)
            if row['Test Success Density %']:
                data[tool]['sr'].append(float(row['Test Success Density %']))

            # TD/LOC
            if row['TD_per_LOC']:
                data[tool]['td'].append(float(row['TD_per_LOC']))

            # CogC/Function (calculated from Cognitive Complexity / Functions)
            if row['Cognitive Complexity'] and row['Functions'] and float(row['Functions']) > 0:
                cogc = float(row['Cognitive Complexity'])
                funcs = float(row['Functions'])
                data[tool]['cogc'].append(cogc / funcs)

            # Smells/KLOC
            if row['New_Smells_per_KLOC']:
                data[tool]['smells'].append(float(row['New_Smells_per_KLOC']))

    # Calculate averages
    results = {}
    for tool in ['Copilot', 'Cursor']:
        results[tool] = {
            'sr': sum(data[tool]['sr']) / len(data[tool]['sr']) if data[tool]['sr'] else 0,
            'td': sum(data[tool]['td']) / len(data[tool]['td']) if data[tool]['td'] else 0,
            'cogc': sum(data[tool]['cogc']) / len(data[tool]['cogc']) if data[tool]['cogc'] else 0,
            'smells': sum(data[tool]['smells']) / len(data[tool]['smells']) if data[tool]['smells'] else 0
        }

    return results


def print_latex_table(results):
    """
    Outputs the table in LaTeX format
    """
    print("\\begin{table}[htbp]")
    print("\\centering")
    print("\\caption{Tool-Vergleich: Copilot vs. Cursor (Mittelwerte über alle Features)}")
    print("\\label{tab:tool_comparison}")
    print("\\small")
    print("\\begin{tabular}{lrrrr}")
    print("\\toprule")
    print("\\textbf{Tool} & \\textbf{SR \\%} & \\textbf{TD/LOC} & \\textbf{CogC/Func} & \\textbf{Smells/KLOC} \\\\")
    print("\\midrule")

    for tool in ['Copilot', 'Cursor']:
        sr = results[tool]['sr']
        td = results[tool]['td']
        cogc = results[tool]['cogc']
        smells = results[tool]['smells']

        print(f"{tool} & {sr:.1f} & {td:.4f} & {cogc:.2f} & {smells:.2f} \\\\")

    print("\\bottomrule")
    print("\\end{tabular}")
    print("\\end{table}")


def print_human_readable(results):
    """
    Outputs the table in human-readable format
    """
    print("=" * 100)
    print("TABLE 15: TOOL COMPARISON - COPILOT VS. CURSOR")
    print("=" * 100)
    print(f"{'Tool':<10} | {'SR %':<10} | {'TD/LOC':<10} | {'CogC/Func':<12} | {'Smells/KLOC':<12}")
    print("-" * 100)

    for tool in ['Copilot', 'Cursor']:
        sr = results[tool]['sr']
        td = results[tool]['td']
        cogc = results[tool]['cogc']
        smells = results[tool]['smells']

        print(f"{tool:<10} | {sr:>10.1f} | {td:>10.4f} | {cogc:>12.2f} | {smells:>12.2f}")

    print("=" * 100)


def main():
    """
    Main function
    """
    print("\n### CALCULATION STARTING ###\n")

    # Calculate table
    results = calculate_tool_comparison()

    # Output in human-readable format
    print_human_readable(results)

    # Output in LaTeX format
    print("\n\n### LATEX FORMAT ###\n")
    print_latex_table(results)

    print("\n### DONE ###\n")


if __name__ == "__main__":
    main()
