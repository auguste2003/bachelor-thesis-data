# ExportReviewCatalog Feature - Zero-Shot Prompt (English)

```
You are a senior Java backend engineer working on the OCP Learning Platform.

Implement a backend feature called "ReviewCatalogExportImport".

Goal:
Authorized reviewers should be able to **export and import**
all questions that are currently in **review status**, including their related answers, for backup, migration, or restoration purposes.

Requirements:
- Implement the feature in Spring Boot 3.5 (Java 21).
- Integrate it into the existing REST-based architecture.
- Include two REST endpoints:
   1. **Export Review Catalog** → Exports all questions with status = "REVIEW"
     and their related answers into a downloadable JSON file.
  2. **Import Review Catalog** → Allows uploading a JSON file to restore or migrate
     review questions and their answers into the system.
- The import process should:
  - Validate the file structure and data consistency.
  - Avoid duplicate entries (match by question text or ID if present).
- Handle security properly: only users with role `REVIEWER` may access these endpoints.
- Follow clean architecture and SOLID principles.
- Include meaningful logging and exception handling.
- Provide comprehensive unit and integration tests with at least 80–90% coverage.
- The code must be complete, compilable, and production-ready.
```
