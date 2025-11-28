#!/usr/bin/env python3
"""
Table 9: Impact on Overall Project Complexity
Calculates the percentage increase in Cyclomatic Complexity per KLOC
after feature implementation (compared to main branch)


"""

import csv
from collections import defaultdict

def calculate_complexity_increase():
    """
    Calculates Δ CC/KLOC % for each variant
    """
    # Find main branch CC/KLOC
    main_cc_kloc = None

    # Collect variant data: variant -> [CC/KLOC values]
    variant_data = defaultdict(list)

    # Read CSV file - first pass: find main branch
    with open('../../data/processed/branches_overall_metrics_normalized.csv', 'r') as f:
        reader = csv.DictReader(f, delimiter=';')

        for row in reader:
            branch = row['Branch']
            cc_kloc = row['CC_per_KLOC']

            if not branch or not cc_kloc:
                continue

            # Main branch as baseline
            if branch == 'main':
                main_cc_kloc = float(cc_kloc)
                break

    # Second pass: collect variant data
    with open('../../data/processed/branches_overall_metrics_normalized.csv', 'r') as f:
        reader = csv.DictReader(f, delimiter=';')

        for row in reader:
            branch = row['Branch']
            cc_kloc = row['CC_per_KLOC']

            if not branch or not cc_kloc:
                continue

            cc_kloc_val = float(cc_kloc)

            # Skip main branch
            if branch == 'main':
                continue

            # Determine variant
            if 'reference' in branch:
                variant = 'Reference'
            elif 'copilot' in branch and 'zero' in branch:
                variant = 'Copilot-Zero'
            elif 'copilot' in branch and 'few' in branch:
                variant = 'Copilot-Few'
            elif 'cursor' in branch and 'zero' in branch:
                variant = 'Cursor-Zero'
            elif 'cursor' in branch and 'few' in branch:
                variant = 'Cursor-Few'
            else:
                continue

            # Calculate percentage increase (only if main_cc_kloc was found)
            if main_cc_kloc is not None:
                increase_pct = ((cc_kloc_val - main_cc_kloc) / main_cc_kloc) * 100
                variant_data[variant].append(increase_pct)

    # Calculate averages
    results = {}
    for variant in ['Reference', 'Copilot-Zero', 'Copilot-Few', 'Cursor-Zero', 'Cursor-Few']:
        if variant in variant_data and len(variant_data[variant]) > 0:
            results[variant] = sum(variant_data[variant]) / len(variant_data[variant])
        else:
            results[variant] = None

    return results, main_cc_kloc


def print_latex_table(results):
    """
    Outputs the table in LaTeX format
    """
    print("\\begin{table}[htbp]")
    print("\\centering")
    print("\\caption{Einfluss auf die Gesamtkomplexität des Projekts}")
    print("\\label{tab:complexity_increase}")
    print("\\small")
    print("\\begin{tabular}{lr}")
    print("\\toprule")
    print("\\textbf{Variante} & \\textbf{$\\Delta$ CC/KLOC \\%} \\\\")
    print("\\midrule")

    for variant in ['Reference', 'Copilot-Zero', 'Copilot-Few', 'Cursor-Zero', 'Cursor-Few']:
        increase = results[variant]

        if increase is not None:
            print(f"{variant} & +{increase:.1f} \\\\")
        else:
            print(f"{variant} & -- \\\\")

    print("\\bottomrule")
    print("\\end{tabular}")
    print("\\end{table}")


def print_human_readable(results, main_cc_kloc):
    """
    Outputs the table in human-readable format
    """
    print("=" * 80)
    print("TABLE 9: IMPACT ON OVERALL PROJECT COMPLEXITY")
    print("=" * 80)
    print(f"\nMain Branch Baseline: {main_cc_kloc:.2f} CC/KLOC\n")
    print(f"{'Variant':<20} | {'Δ CC/KLOC %':<15}")
    print("-" * 80)

    for variant in ['Reference', 'Copilot-Zero', 'Copilot-Few', 'Cursor-Zero', 'Cursor-Few']:
        increase = results[variant]

        if increase is not None:
            print(f"{variant:<20} | +{increase:>14.1f}")
        else:
            print(f"{variant:<20} | {'--':>15}")

    print("=" * 80)


def main():
    """
    Main function
    """
    print("\n### CALCULATION STARTING ###\n")

    # Calculate table
    results, main_cc_kloc = calculate_complexity_increase()

    # Output in human-readable format
    print_human_readable(results, main_cc_kloc)

    # Output in LaTeX format
    print("\n\n### LATEX FORMAT ###\n")
    print_latex_table(results)

    print("\n### DONE ###\n")


if __name__ == "__main__":
    main()
