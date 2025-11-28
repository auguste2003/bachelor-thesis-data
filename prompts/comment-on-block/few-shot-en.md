# CommentOnBlock Feature - Few-Shot Prompt (English)

```
You are a senior Spring Boot engineer working on the OCP Learning Platform.

Context:
Users can comment on LearningBlocks. Comments are tied to a specific block and
to the authenticated user who created them. Only the author can delete their own comment.

Below is a short illustrative snippet showing our typical style for resource creation + ownership checks.
It is only an example for structure and tone, not a strict template.

[EXAMPLE START]
// Illustrative style for ownership-based creation
@Service
@RequiredArgsConstructor
@Slf4j
public class ExampleCommentService {

    private final ExampleCommentRepository repo;

    public CommentDto addComment(CreateCommentDto dto, String currentUserId) {
        // map DTO to entity, set owner = currentUserId, createdAt = now
        // persist entity and return DTO
        throw new UnsupportedOperationException("illustrative example");
    }
}
[EXAMPLE END]

Task: Implement the feature **CommentOnBlock**.

Requirements:
- Spring Boot 3.5 (Java 21, Jakarta EE 9) with JPA and Keycloak authentication.
- Allow authenticated users to post comments on LearningBlocks, view comments per block,
  and delete their own comments.
- Enforce ownership: only the author of a comment may delete it.
- Include validation for comment content (`@NotBlank`, `@Size(max=1000)`).
- Fetch comments by block ID ordered by creation time.
- Optional: support pagination for comment lists.
- Follow layered architecture (Controller → Service → Repository) and clean code / SOLID.
- Add unit and integration tests with ≈ 80–90 % coverage (JUnit 5 + MockMvc + Testcontainers).
- Use @Slf4j for logging and @RequiredArgsConstructor for constructor injection.
- Output fully compilable, production-ready Java code only.
```

## Evaluation Checklist

| Kategorie | Erwartung / Prüfkriterium |
|-----------|---------------------------|
| **Security** | Ownership über User-ID aus JWT korrekt enforced |
| **Validation** | @NotBlank + @Size vorhanden |
| **Layer-Trennung** | Controller / Service / Repository sauber getrennt |
| **Tests** | CRUD + Ownership abgedeckt, ≥ 80 % Coverage |
| **Maintainability** | Sonar Rating A–B, geringe Komplexität |
| **Architecture-Entscheidung** | Pagination? DTO-Mapping? Exception-Handling? |
