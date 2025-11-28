#!/usr/bin/env python3
"""
Table 16: Test Success Rate by Tool and Feature
Calculates the average Test Success Rate for each tool (Copilot, Cursor)
grouped by features (LearningBlock, CommentOnBlock, NotifyReviewer, ExportReviewCatalog)
"""

import csv
from collections import defaultdict

def calculate_sr_by_tool_and_feature():
    """
    Calculates Test Success Rate by tool and feature
    """
    # Collect data: tool -> feature -> [SR values]
    data = defaultdict(lambda: defaultdict(list))

    # Read CSV file
    with open('../../data/processed/pr_new_code_metrics_normalized.csv', 'r') as f:
        reader = csv.DictReader(f, delimiter=';')

        for row in reader:
            variant = row['Variant']
            feature = row['Feature']
            sr = row['Test Success Density %']

            # Only relevant rows (skip Reference and empty values)
            if not variant or variant == 'Reference' or not feature or not sr or sr == '':
                continue

            # Determine tool
            if 'Copilot' in variant:
                tool = 'Copilot'
            elif 'Cursor' in variant:
                tool = 'Cursor'
            else:
                continue

            # Add SR value
            data[tool][feature].append(float(sr))

    # Calculate averages
    results = {}
    for tool in ['Copilot', 'Cursor']:
        results[tool] = {}
        for feature in ['LearningBlock', 'CommentOnBlock', 'NotifyReviewer', 'ExportReviewCatalog']:
            if feature in data[tool] and len(data[tool][feature]) > 0:
                results[tool][feature] = sum(data[tool][feature]) / len(data[tool][feature])
            else:
                results[tool][feature] = None

    return results


def print_latex_table(results):
    """
    Outputs the table in LaTeX format
    """
    print("\\begin{table}[htbp]")
    print("\\centering")
    print("\\caption{Test Success Rate nach Werkzeug und Feature}")
    print("\\label{tab:tool_comparison_features}")
    print("\\small")
    print("\\begin{tabular}{lrr}")
    print("\\toprule")
    print("\\textbf{Feature} & \\textbf{Copilot SR \\%} & \\textbf{Cursor SR \\%} \\\\")
    print("\\midrule")

    for feature in ['LearningBlock', 'CommentOnBlock', 'NotifyReviewer', 'ExportReviewCatalog']:
        copilot_sr = results['Copilot'][feature]
        cursor_sr = results['Cursor'][feature]

        copilot_str = f"{copilot_sr:.1f}" if copilot_sr is not None else "--"
        cursor_str = f"{cursor_sr:.1f}" if cursor_sr is not None else "--"

        print(f"{feature} & {copilot_str} & {cursor_str} \\\\")

    print("\\bottomrule")
    print("\\end{tabular}")
    print("\\end{table}")


def print_human_readable(results):
    """
    Outputs the table in human-readable format
    """
    print("=" * 80)
    print("TABLE 16: TEST SUCCESS RATE BY TOOL AND FEATURE")
    print("=" * 80)
    print(f"{'Feature':<25} | {'Copilot SR %':<15} | {'Cursor SR %':<15}")
    print("-" * 80)

    for feature in ['LearningBlock', 'CommentOnBlock', 'NotifyReviewer', 'ExportReviewCatalog']:
        copilot_sr = results['Copilot'][feature]
        cursor_sr = results['Cursor'][feature]

        copilot_str = f"{copilot_sr:.1f}" if copilot_sr is not None else "--"
        cursor_str = f"{cursor_sr:.1f}" if cursor_sr is not None else "--"

        print(f"{feature:<25} | {copilot_str:>15} | {cursor_str:>15}")

    print("=" * 80)


def main():
    """
    Main function
    """
    print("\n### CALCULATION STARTING ###\n")

    # Calculate table
    results = calculate_sr_by_tool_and_feature()

    # Output in human-readable format
    print_human_readable(results)

    # Output in LaTeX format
    print("\n\n### LATEX FORMAT ###\n")
    print_latex_table(results)

    print("\n### DONE ###\n")


if __name__ == "__main__":
    main()
