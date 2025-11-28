# Prompts

This directory contains all prompts used in the bachelor thesis study.

## Structure

Each feature has its own subdirectory with prompt variants:
- `zero-shot-en.md` – Zero-Shot prompt in English
- `zero-shot-de.md` – Zero-Shot prompt in German
- `few-shot-en.md` – Few-Shot prompt in English (with code examples)
- `few-shot-de.md` – Few-Shot prompt in German (with code examples)

## Features

1. **learning-block** – CRUD operations for LearningBlock entity
   - Zero-Shot: English only
   - Few-Shot: English only

2. **comment-on-block** – Comment functionality for LearningBlocks
   - Zero-Shot: English only
   - Few-Shot: English only

3. **notify-reviewer** – Email notification system with Keycloak integration
   - Zero-Shot: German only
   - Few-Shot: German only

4. **export-review-catalog** – Export/Import of review catalogs as JSON
   - Zero-Shot: English only
   - Few-Shot: English only

## Prompt Structure

All prompts follow a consistent structure:
1. Role definition (Senior Spring Boot Backend Engineer)
2. Functional requirements (Entities, Endpoints, Validation)
3. Technical constraints (Clean Code, SOLID, JWT authentication)
4. Quality criteria (Test coverage ≥80%, no placeholders)
5. Few-Shot: Two code examples from reference implementation

## Usage

These prompts were used with various AI coding assistants (GitHub Copilot, Cursor AI, etc.) to generate backend code for the OCP Learning Platform.

For details about the experimental setup and results, see Chapter 5 of the thesis.

## Note

The Few-Shot prompts include concrete code examples from the reference implementation to guide the AI models. These examples demonstrate:
- Proper layered architecture (Controller → Service → Repository)
- Security best practices (JWT authentication, role-based access control)
- Exception handling patterns
- Testing strategies
