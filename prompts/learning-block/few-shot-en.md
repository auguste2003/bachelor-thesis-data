# LearningBlock Feature - Few-Shot Prompt (English)

```
You are a senior Spring Boot backend engineer working on the OCP Learning Platform.

Context:
Users write LearningBlocks (Markdown posts) about their learning progress. Ownership and visibility must be enforced.

Below is a short illustrative snippet showing the style for resource creation + validation (not prescriptive):

[EXAMPLE START]
// Illustrative style for creation + validation (structure only)
@Service
@RequiredArgsConstructor
@Slf4j
public class ExampleNoteService {
    private final ExampleNoteRepository repo;

    public Long create(ExampleNoteDto dto, String ownerId) {
        // validate dto fields, map to entity, set ownerId, timestamps
        // persist and return id
        throw new UnsupportedOperationException("illustrative example");
    }
}
[EXAMPLE END]

Task: Implement the feature **LearningBlocks**.

Requirements:
- Spring Boot 3.5 (Java 21, Jakarta), JPA; Keycloak-based authentication for user identity.
- CRUD endpoints for LearningBlocks with DTOs and bean validation.
- Ownership rules: only the owner can update or delete; visibility controls reading
  (e.g., PUBLIC for anyone authenticated, INTERNAL for same realm/role, PRIVATE only for owner).
- Add pagination + sorting for list endpoint; filter by owner optional (?ownerId=…).
- Layered architecture (Controller → Service → Repository), clean code/SOLID, exception handling.
- Tests: JUnit 5, MockMvc, Testcontainers (Postgres); aim for ~80–90% coverage.
- Minimal logging with @Slf4j and constructor injection (@RequiredArgsConstructor).
- Output complete, compilable production-grade Java code only.
```

## Evaluation Checklist

- **Security/Ownership**: Update/Delete nur Owner? Visibility korrekt?
- **Validation**: Titel/Markdown-Grenzen, leere Felder?
- **Pagination/Sorting**: vorhanden & korrekt?
- **Error Handling**: 400/403/404/409 sinnvoll?
- **Tests**: realistische IT + Coverage ≥ 80 %?
- **Qualität**: Sonar Maintainability (A/B), geringe Komplexität, klare Layer-Trennung.
