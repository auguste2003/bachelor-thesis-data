#!/bin/bash

# ==========================================
# Script: Analyze PRs (New Code Only)
# ==========================================
# This script analyzes ONLY the code added
# by each Pull Request (new code)
# ==========================================

# Configuration
SONARQUBE_URL="http://localhost:9000"
TOKEN="sqp_2cc52cea21406ce0387acf7e75ca6b8d442de8a8"
PROJECT_KEY="OCP-Backend"

# NEW metrics (new code only)
NEW_METRICS="new_lines,new_lines_to_cover,new_code_smells,new_bugs,new_vulnerabilities,new_security_hotspots,new_duplicated_lines_density,new_coverage,new_technical_debt,new_reliability_rating,new_security_rating,new_maintainability_rating"

# OVERALL metrics (for complexity and structure - no new_* available)
OVERALL_METRICS="complexity,cognitive_complexity,functions,classes,statements"

# Output file
OUTPUT_FILE="../../data/raw/pr_new_code_metrics.csv"

# Function to extract a metric from JSON
extract_metric() {
    local json="$1"
    local metric_name="$2"
    echo "$json" | jq -r ".component.measures[] | select(.metric==\"$metric_name\") | .value // \"N/A\""
}

# Function to extract a "period" metric (new_*)
extract_period_metric() {
    local json="$1"
    local metric_name="$2"
    echo "$json" | jq -r ".component.measures[] | select(.metric==\"$metric_name\") | .period.value // \"N/A\""
}

echo "========================================="
echo "SonarQube - PULL REQUESTS (New Code)"
echo "========================================="
echo ""

# Create CSV header (separator: semicolon for Excel DE)
echo "PR Key;New Lines;New Lines to Cover;New Code Smells;New Bugs;New Vulnerabilities;New Security Hotspots;New Duplication %;New Coverage %;New Technical Debt (min);New Reliability Rating;New Security Rating;New Maintainability Rating;Complexity (Overall);Cognitive Complexity (Overall);Functions (Overall);Classes (Overall);Statements (Overall)" > "$OUTPUT_FILE"

# Loop over PRs from 13 to 28
pr_count=0
total_prs=17

for pr in {12..28}; do
    pr_count=$((pr_count + 1))
    echo "[$pr_count/$total_prs] Fetching metrics for PR #$pr"

    # API call for NEW metrics
    response_new=$(curl -s -u "$TOKEN:" \
        "$SONARQUBE_URL/api/measures/component?component=$PROJECT_KEY&pullRequest=$pr&metricKeys=$NEW_METRICS")

    # API call for OVERALL metrics (complexity)
    response_overall=$(curl -s -u "$TOKEN:" \
        "$SONARQUBE_URL/api/measures/component?component=$PROJECT_KEY&pullRequest=$pr&metricKeys=$OVERALL_METRICS")

    # Check if the response contains errors
    if echo "$response_new" | jq -e '.errors' > /dev/null 2>&1; then
        echo "  ⚠️  Error fetching PR #$pr: $(echo "$response_new" | jq -r '.errors[0].msg')"
        # Write a line with N/A for this PR
        echo "$pr;N/A;N/A;N/A;N/A;N/A;N/A;N/A;N/A;N/A;N/A;N/A;N/A;N/A;N/A;N/A;N/A;N/A" >> "$OUTPUT_FILE"
        continue
    fi

    # Extract NEW metrics (with .period.value)
    new_lines=$(extract_period_metric "$response_new" "new_lines")
    new_lines_to_cover=$(extract_period_metric "$response_new" "new_lines_to_cover")
    new_code_smells=$(extract_period_metric "$response_new" "new_code_smells")
    new_bugs=$(extract_period_metric "$response_new" "new_bugs")
    new_vulnerabilities=$(extract_period_metric "$response_new" "new_vulnerabilities")
    new_security_hotspots=$(extract_period_metric "$response_new" "new_security_hotspots")
    new_duplicated_lines=$(extract_period_metric "$response_new" "new_duplicated_lines_density")
    new_coverage=$(extract_period_metric "$response_new" "new_coverage")
    new_technical_debt=$(extract_period_metric "$response_new" "new_technical_debt")
    new_reliability_rating=$(extract_period_metric "$response_new" "new_reliability_rating")
    new_security_rating=$(extract_period_metric "$response_new" "new_security_rating")
    new_maintainability_rating=$(extract_period_metric "$response_new" "new_maintainability_rating")

    # Extract OVERALL metrics (complexity and structure)
    complexity=$(extract_metric "$response_overall" "complexity")
    cognitive_complexity=$(extract_metric "$response_overall" "cognitive_complexity")
    functions=$(extract_metric "$response_overall" "functions")
    classes=$(extract_metric "$response_overall" "classes")
    statements=$(extract_metric "$response_overall" "statements")

    # Write to CSV
    echo "$pr;$new_lines;$new_lines_to_cover;$new_code_smells;$new_bugs;$new_vulnerabilities;$new_security_hotspots;$new_duplicated_lines;$new_coverage;$new_technical_debt;$new_reliability_rating;$new_security_rating;$new_maintainability_rating;$complexity;$cognitive_complexity;$functions;$classes;$statements" >> "$OUTPUT_FILE"
    
    echo "  ✓ Done (New Lines: $new_lines, New Code Smells: $new_code_smells, New Coverage: $new_coverage%)"
    
done

echo ""
echo "✅ PR metrics saved to: $OUTPUT_FILE"
echo ""
echo "========================================="
echo "New Code Analysis Complete!"
echo "========================================="
echo ""
echo "📊 Note: 'Complexity' and 'Cognitive Complexity' are OVERALL metrics"
echo "   (no 'new_complexity' available in SonarQube)"
