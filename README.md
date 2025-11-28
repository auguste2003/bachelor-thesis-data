# Bachelor Thesis Data: AI Coding Assistants Evaluation

This repository contains the data, prompts, and analysis scripts for a bachelor thesis evaluating AI coding assistants in backend development.

## Overview

This study compares different AI coding assistants (GitHub Copilot, Cursor AI, etc.) in generating Spring Boot backend code using various prompt engineering techniques (Zero-Shot vs Few-Shot, English vs German).

## Repository Structure

```
.
├── data/               # Raw and processed data
│   ├── raw/           # Original data collected from experiments
│   └── processed/     # Normalized and cleaned data
├── prompts/           # Prompt variants used in the study
│   ├── learning-block/
│   ├── comment-on-block/
│   ├── notify-reviewer/
│   └── export-review-catalog/
├── scripts/           # Data collection and analysis scripts
│   ├── data-collection/
│   ├── data-processing/
│   └── analysis/
├── results/           # Analysis results and visualizations
└── manuel-codereview/ # Manual code review summaries
```

## Features Evaluated

The study evaluates AI-generated code for four backend features:

1. **learning-block** – CRUD operations for LearningBlock entity
2. **comment-on-block** – Comment functionality for LearningBlocks
3. **notify-reviewer** – Email notification system with Keycloak integration
4. **export-review-catalog** – Export/Import of review catalogs as JSON

## Prompt Variants

Each feature was implemented using different prompt strategies:
- **Zero-Shot** (English/German) – Direct task description without examples
- **Few-Shot** (English/German) – Task description with code examples

See [`prompts/README.md`](prompts/README.md) for detailed information about prompt structure.

## Data Collection

The `scripts/data-collection/` directory contains scripts for:
- Fetching branch data from GitHub repositories
- Extracting pull request code changes
- Collecting metrics from AI-generated implementations

## Data Processing

The `scripts/data-processing/` directory contains:
- `normalize_metrics.py` – Normalize and clean collected metrics

## Analysis

The `scripts/analysis/` directory contains scripts for generating thesis tables:
- `table_09_complexity_increase.py` – Analyze code complexity metrics
- `table_15_tool_comparison.py` – Compare AI tool performance
- `table_16_test_sr_by_tool_feature.py` – Test success rates by tool and feature

## Requirements

- Python 3.x
- Bash shell (for data collection scripts)
- Git
- Access to evaluated GitHub repositories

## Usage

### Data Collection

```bash
cd scripts/data-collection
./fetch_branches_overall.sh
./fetch_pr_new_code.sh
```

### Data Processing

```bash
cd scripts/data-processing
python normalize_metrics.py
```

### Analysis

```bash
cd scripts/analysis
python table_09_complexity_increase.py
python table_15_tool_comparison.py
python table_16_test_sr_by_tool_feature.py
```

## Evaluation Criteria

The generated code was evaluated based on:
- **Functionality** – Correctness and completeness
- **Code Quality** – Clean Code, SOLID principles
- **Test Coverage** – ≥80% coverage requirement
- **Security** – JWT authentication, input validation
- **Complexity** – Cyclomatic complexity, lines of code

## License

This data is part of a bachelor thesis and is provided for academic purposes.

## Author

Auguste Sonfack Dongmo

## Related

For the complete thesis and detailed methodology, see Chapter 5 of the thesis document.
