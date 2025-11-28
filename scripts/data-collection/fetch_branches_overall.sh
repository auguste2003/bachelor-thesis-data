#!/bin/bash

# ==========================================
# Script: Analyze BRANCHES (Overall Code)
# ==========================================
# This script analyzes the GLOBAL quality of the project
# after the integration of each feature
# ==========================================

# Configuration
SONARQUBE_URL="http://localhost:9000"
TOKEN="sqp_2cc52cea21406ce0387acf7e75ca6b8d442de8a8"
PROJECT_KEY="OCP-Backend"
BRANCH_LIST_FILE="../../data/raw/branch_list.json"

# Metrics to capture (Overall Code)
METRICS="code_smells,bugs,vulnerabilities,security_hotspots,complexity,cognitive_complexity,duplicated_lines_density,ncloc,comment_lines_density,tests,test_success_density,test_failures,test_errors,coverage,functions,classes,statements"

# Output file
OUTPUT_FILE="../../data/raw/branches_overall_metrics.csv"

# Function to extract a metric from JSON
extract_metric() {
    local json="$1"
    local metric_name="$2"
    echo "$json" | jq -r ".component.measures[] | select(.metric==\"$metric_name\") | .value // \"N/A\""
}

echo "========================================="
echo "SonarQube - BRANCHES (Overall Code)"
echo "========================================="
echo ""

# Create CSV header (separator: semicolon for Excel DE)
echo "Branch;Code Smells;Bugs;Vulnerabilities;Security Hotspots;Complexity;Cognitive Complexity;Duplication %;NCLOC;Comment Density %;Tests;Test Success Rate %;Test Failures;Test Errors;Coverage %;Functions;Classes;Statements" > "$OUTPUT_FILE"

# Read branch list from JSON file
branches=$(jq -r '.branches[].name' "$BRANCH_LIST_FILE")

branch_count=0
total_branches=$(echo "$branches" | wc -l)

# Loop over all branches
while IFS= read -r branch; do
    branch_count=$((branch_count + 1))
    echo "[$branch_count/$total_branches] Fetching metrics for branch: $branch"

    # URL-encode branch name
    encoded_branch=$(echo "$branch" | jq -sRr @uri)

    # API call
    response=$(curl -s -u "$TOKEN:" \
        "$SONARQUBE_URL/api/measures/component?component=$PROJECT_KEY&branch=$encoded_branch&metricKeys=$METRICS")

    # Check if the response contains errors
    if echo "$response" | jq -e '.errors' > /dev/null 2>&1; then
        echo "  ⚠️  Error fetching branch '$branch': $(echo "$response" | jq -r '.errors[0].msg')"
        continue
    fi

    # Extract metrics
    code_smells=$(extract_metric "$response" "code_smells")
    bugs=$(extract_metric "$response" "bugs")
    vulnerabilities=$(extract_metric "$response" "vulnerabilities")
    security_hotspots=$(extract_metric "$response" "security_hotspots")
    complexity=$(extract_metric "$response" "complexity")
    cognitive_complexity=$(extract_metric "$response" "cognitive_complexity")
    duplicated_lines=$(extract_metric "$response" "duplicated_lines_density")
    ncloc=$(extract_metric "$response" "ncloc")
    comment_density=$(extract_metric "$response" "comment_lines_density")
    tests=$(extract_metric "$response" "tests")
    test_success_rate=$(extract_metric "$response" "test_success_density")
    test_failures=$(extract_metric "$response" "test_failures")
    test_errors=$(extract_metric "$response" "test_errors")
    coverage=$(extract_metric "$response" "coverage")
    functions=$(extract_metric "$response" "functions")
    classes=$(extract_metric "$response" "classes")
    statements=$(extract_metric "$response" "statements")

    # Write to CSV (escape quotes in branch name)
    escaped_branch=$(echo "$branch" | sed 's/"/""/g')
    echo "\"$escaped_branch\";$code_smells;$bugs;$vulnerabilities;$security_hotspots;$complexity;$cognitive_complexity;$duplicated_lines;$ncloc;$comment_density;$tests;$test_success_rate;$test_failures;$test_errors;$coverage;$functions;$classes;$statements" >> "$OUTPUT_FILE"

    echo "  ✓ Done (Bugs: $bugs, Code Smells: $code_smells, Coverage: $coverage%)"

done <<< "$branches"

echo ""
echo "✅ Branch metrics saved to: $OUTPUT_FILE"
echo ""
echo "========================================="
echo "Overall Code Analysis Complete!"
echo "========================================="
