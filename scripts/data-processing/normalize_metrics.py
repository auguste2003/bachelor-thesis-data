#!/usr/bin/env python3
"""
Normalization script for Bachelor Thesis metrics
Normalizes code quality metrics according to methodology (Section 4.4.3)
"""

import pandas as pd
import numpy as np

def normalize_overall_metrics(df):
    """
    Normalize Overall Code Metrics from branches
    
    Normalization formulas:
    - Code Smells / KLOC = (Code Smells / NCLOC) * 1000
    - Cyclomatic Complexity / KLOC = (Complexity / NCLOC) * 1000
    - Cognitive Complexity / Function = Cognitive Complexity / Functions
    - Duplication % = already normalized (no change)
    - Test Density = (Tests / NCLOC) * 1000
    """
    df_norm = df.copy()
    
    # Convert comma decimal separator to dot (if present)
    for col in ['Duplication %', 'Test Success Rate %', 'Coverage %']:
        if col in df_norm.columns:
            df_norm[col] = df_norm[col].astype(str).str.replace(',', '.').astype(float)
    
    # Calculate normalized metrics
    df_norm['Smells_per_KLOC'] = (df_norm['Code Smells'] / df_norm['NCLOC']) * 1000
    df_norm['CC_per_KLOC'] = (df_norm['Complexity'] / df_norm['NCLOC']) * 1000
    df_norm['CogC_per_Function'] = df_norm['Cognitive Complexity'] / df_norm['Functions']
    df_norm['Test_Density_per_KLOC'] = (df_norm['Tests'] / df_norm['NCLOC']) * 1000
    
    # Round to 2 decimal places for readability
    df_norm['Smells_per_KLOC'] = df_norm['Smells_per_KLOC'].round(2)
    df_norm['CC_per_KLOC'] = df_norm['CC_per_KLOC'].round(2)
    df_norm['CogC_per_Function'] = df_norm['CogC_per_Function'].round(2)
    df_norm['Test_Density_per_KLOC'] = df_norm['Test_Density_per_KLOC'].round(2)
    
    # Reorder columns: original metrics first, then normalized
    original_cols = ['Branch', 'Code Smells', 'Complexity', 'Cognitive Complexity', 
                     'Duplication %', 'NCLOC', 'Tests', 'Test Success Rate %', 
                     'Test Failures', 'Coverage %', 'Functions']
    normalized_cols = ['Smells_per_KLOC', 'CC_per_KLOC', 'CogC_per_Function', 
                       'Test_Density_per_KLOC']
    
    df_norm = df_norm[original_cols + normalized_cols]
    
    return df_norm


def normalize_new_code_metrics(df):
    """
    Normalize New Code Metrics from Pull Requests
    
    Normalization formulas:
    - New Code Smells / KLOC = (New Code Smells / New Lines) * 1000
    - New Technical Debt / LOC = New Technical Debt / New Lines
    - Cyclomatic Complexity / KLOC = (Complexity / New Lines) * 1000
    - Cognitive Complexity / Function = Cognitive Complexity / Functions
    """
    df_norm = df.copy()
    
    # Convert comma decimal separator to dot (if present)
    for col in ['New Duplication %', 'New Coverage %', 'Test Success Density %']:
        if col in df_norm.columns:
            df_norm[col] = df_norm[col].astype(str).str.replace(',', '.').astype(float)
    
    # Handle missing values (cursor-zero-notifyreviewer has no data)
    df_norm['New Lines'] = pd.to_numeric(df_norm['New Lines'], errors='coerce')
    df_norm['New Code Smells'] = pd.to_numeric(df_norm['New Code Smells'], errors='coerce')
    df_norm['New Technical Debt (min)'] = pd.to_numeric(df_norm['New Technical Debt (min)'], errors='coerce')
    
    # Calculate normalized metrics (only where data exists)
    df_norm['New_Smells_per_KLOC'] = (df_norm['New Code Smells'] / df_norm['New Lines']) * 1000
    df_norm['TD_per_LOC'] = df_norm['New Technical Debt (min)'] / df_norm['New Lines']
    df_norm['New_CC_per_KLOC'] = (df_norm['Complexity'] / df_norm['New Lines']) * 1000
    df_norm['New_CogC_per_Function'] = df_norm['Cognitive Complexity'] / df_norm['Functions']
    df_norm['Test_Density_per_KLOC'] = (df_norm['Test Count'] / df_norm['New Lines']) * 1000
    
    # Round to 2 decimal places
    df_norm['New_Smells_per_KLOC'] = df_norm['New_Smells_per_KLOC'].round(2)
    df_norm['TD_per_LOC'] = df_norm['TD_per_LOC'].round(4)  # TD is small, need more precision
    df_norm['New_CC_per_KLOC'] = df_norm['New_CC_per_KLOC'].round(2)
    df_norm['New_CogC_per_Function'] = df_norm['New_CogC_per_Function'].round(2)
    df_norm['Test_Density_per_KLOC'] = df_norm['Test_Density_per_KLOC'].round(2)
    
    # Reorder columns
    original_cols = ['Branch', 'PR Key', 'New Lines', 'New Code Smells', 'New Duplication %', 
                     'New Coverage %', 'Test Count', 'Test Success Density %', 'Test Failures',
                     'New Technical Debt (min)', 'Complexity', 'Cognitive Complexity', 'Functions']
    normalized_cols = ['New_Smells_per_KLOC', 'TD_per_LOC', 'New_CC_per_KLOC', 
                       'New_CogC_per_Function', 'Test_Density_per_KLOC']
    
    df_norm = df_norm[original_cols + normalized_cols]
    
    return df_norm


def extract_variant_type(branch_name):
    """
    Extract variant type from branch name
    Returns: 'Reference', 'Copilot-Zero', 'Copilot-Few', 'Cursor-Zero', 'Cursor-Few', 'Main'
    """
    if branch_name == 'main':
        return 'Main'
    elif 'reference' in branch_name:
        return 'Reference'
    elif 'copilot' in branch_name and 'zero' in branch_name:
        return 'Copilot-Zero'
    elif 'copilot' in branch_name and 'few' in branch_name:
        return 'Copilot-Few'
    elif 'cursor' in branch_name and 'zero' in branch_name:
        return 'Cursor-Zero'
    elif 'cursor' in branch_name and 'few' in branch_name:
        return 'Cursor-Few'
    else:
        return 'Unknown'


def extract_feature_name(branch_name):
    """
    Extract feature name from branch name
    """
    if 'learningblock' in branch_name:
        return 'LearningBlock'
    elif 'commentonblock' in branch_name:
        return 'CommentOnBlock'
    elif 'notifyreviewer' in branch_name:
        return 'NotifyReviewer'
    elif 'exportreviewcatalog' in branch_name:
        return 'ExportReviewCatalog'
    elif branch_name == 'main':
        return 'Main'
    else:
        return 'Unknown'


def calculate_summary_statistics(df_overall, df_new):
    """
    Calculate summary statistics grouped by variant type
    """
    # Add variant and feature columns
    df_overall['Variant'] = df_overall['Branch'].apply(extract_variant_type)
    df_overall['Feature'] = df_overall['Branch'].apply(extract_feature_name)
    
    df_new['Variant'] = df_new['Branch'].apply(extract_variant_type)
    df_new['Feature'] = df_new['Branch'].apply(extract_feature_name)
    
    # Exclude 'Main' and 'Unknown' from aggregations
    df_overall_filtered = df_overall[~df_overall['Variant'].isin(['Main', 'Unknown'])]
    df_new_filtered = df_new[~df_new['Variant'].isin(['Main', 'Unknown'])]
    
    # Calculate mean and median for overall metrics
    overall_stats = df_overall_filtered.groupby('Variant').agg({
        'Smells_per_KLOC': ['mean', 'median', 'std'],
        'CC_per_KLOC': ['mean', 'median', 'std'],
        'CogC_per_Function': ['mean', 'median', 'std'],
        'Duplication %': ['mean', 'median', 'std'],
        'Test Success Rate %': ['mean', 'median', 'std'],
        'Coverage %': ['mean', 'median', 'std'],
        'Test_Density_per_KLOC': ['mean', 'median', 'std']
    }).round(2)
    
    # Calculate mean and median for new code metrics
    new_code_stats = df_new_filtered.groupby('Variant').agg({
        'New_Smells_per_KLOC': ['mean', 'median', 'std'],
        'TD_per_LOC': ['mean', 'median', 'std'],
        'New_CC_per_KLOC': ['mean', 'median', 'std'],
        'New_CogC_per_Function': ['mean', 'median', 'std'],
        'New Duplication %': ['mean', 'median', 'std'],
        'New Coverage %': ['mean', 'median', 'std'],
        'Test Success Density %': ['mean', 'median', 'std'],
        'Test_Density_per_KLOC': ['mean', 'median', 'std']
    }).round(4)
    
    return overall_stats, new_code_stats


def main():
    """
    Main execution function
    """
    print("=== Code Quality Metrics Normalization ===\n")
    
    # Read input files
    print("Reading input files...")
    df_overall = pd.read_csv('../../data/raw/branches_overall_metrics.csv', sep=';')
    df_new = pd.read_csv('../../data/raw/pr_new_code_metrics.csv', sep=';')

    print(f"  ✓ branches_overall_metrics.csv: {len(df_overall)} rows")
    print(f"  ✓ pr_new_code_metrics.csv: {len(df_new)} rows\n")
    
    # Normalize metrics
    print("Normalizing overall metrics...")
    df_overall_norm = normalize_overall_metrics(df_overall)
    print("  ✓ Smells/KLOC, CC/KLOC, CogC/Function calculated\n")
    
    print("Normalizing new code metrics...")
    df_new_norm = normalize_new_code_metrics(df_new)
    print("  ✓ New Smells/KLOC, TD/LOC, New CC/KLOC calculated\n")
    
    # Calculate summary statistics
    print("Calculating summary statistics...")
    overall_stats, new_code_stats = calculate_summary_statistics(df_overall_norm, df_new_norm)
    print("  ✓ Mean, median, std calculated per variant\n")
    
    # Export results
    print("Exporting results...")
    df_overall_norm.to_csv('../../data/processed/branches_overall_metrics_normalized.csv',
                           sep=';', index=False)
    df_new_norm.to_csv('../../data/processed/pr_new_code_metrics_normalized.csv',
                       sep=';', index=False)

    # Export summary statistics
    overall_stats.to_csv('../../data/processed/summary_overall_metrics.csv', sep=';')
    new_code_stats.to_csv('../../data/processed/summary_new_code_metrics.csv', sep=';')
    
    print("  ✓ branches_overall_metrics_normalized.csv")
    print("  ✓ pr_new_code_metrics_normalized.csv")
    print("  ✓ summary_overall_metrics.csv")
    print("  ✓ summary_new_code_metrics.csv\n")
    
    # Print quick overview
    print("=== Quick Overview ===")
    print("\nMean Smells/KLOC by Variant (Overall Code):")
    print(df_overall_norm.groupby(df_overall_norm['Branch'].apply(extract_variant_type))['Smells_per_KLOC'].mean().round(2))
    
    print("\nMean TD/LOC by Variant (New Code):")
    new_with_variant = df_new_norm.copy()
    new_with_variant['Variant'] = new_with_variant['Branch'].apply(extract_variant_type)
    print(new_with_variant.groupby('Variant')['TD_per_LOC'].mean().round(4))
    
    print("\n=== Normalization Complete ===")
    print("\nFiles are ready in ../../data/processed/")
    print("You can now use these normalized metrics for analysis in Chapter 6.")


if __name__ == "__main__":
    main()
