# ExportReviewCatalog Feature - Few-Shot Prompt (English)

```
You are a senior Java backend engineer on the OCP Learning Platform.

## Task
Implement **ReviewCatalog Export/Import** for questions with `status = "REVIEW"`.

---

## Existing Implementation (Reference)

**Export Endpoint: This is the actual Endpoint for the approved questions**

```java
  @GetMapping("/export-katalog")
  @PreAuthorize("hasRole('ADMIN')")
  public ResponseEntity<Resource> exportKatalog() throws JsonProcessingException {
    List<QuestionExportDTO> exportData =  katalogService.exportKatalog() ;

    // Formatierte JSON-Ausgabe erzeugen
    String json = objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(exportData);

    // Katalog in einer Datei speichern
    ByteArrayResource resource = new ByteArrayResource(json.getBytes(StandardCharsets.UTF_8)) ;

    return ResponseEntity.ok()
      .contentType(MediaType.APPLICATION_JSON)
      .body(resource);
  }
```

**Import Endpoint Example: You can base on this**
```java
  @PostMapping("/import-review-katalog")
  @PreAuthorize("hasRole('REVIEWER')")
  public ResponseEntity<String> importReviewKatalog(@RequestParam("file") MultipartFile file) {
    // We can customize the Exception handling
    try {
      katalogService.importQuestions(file, "REVIEW"); // "REVIEW" indicates review catalog
      return ResponseEntity.ok("Katalog imported successfully.");
    } catch (Exception e) {
      return ResponseEntity.status(HttpStatusCode.valueOf(400)).body("Error while importing katalog. Please check the format of the file : " + e.getMessage());
    }
  }
```

**Expected JSON format** (based on `QuestionExportDTO`):
```json
[
  {
    "type": "MULTIPLE_CHOICE",
    "title": "Multiple Choice 3",
    "questionText": "Wer ist das?",
    "quellenNachweis": "Seite 3",
    "keywords": ["MT"],
    "answer": {
      "options": {
        "der": false,
        "das": true
      }
    }
  }
]
```

---

## Requirements

1. **Implement two endpoints** for ReviewCatalog (status = "REVIEW"):
   - Export: Returns JSON file with all review questions.
   - Import: Accepts JSON file, validates structure, avoids duplicates.

2. **Code Quality:**
   - Follow **Clean Code** and **DRY principles**.
   - Security: Only `REVIEWER` role access.
   - Use existing architecture patterns.
   - You can define ExceptionsHandler, if necessary.

3. **Testing:**
   - Unit and integration tests with **80–90% coverage**.
   - Cover: success paths, error cases, edge cases (invalid JSON, duplicates, unauthorized access).

4. **Refactoring:**
   - You may refactor common logic if it reduces duplication.
   - Do NOT modify existing QuestionCatalog logic (status = "APPROVED").
   - Document refactoring decisions inline.

---

**Deliverables:** Complete, production-ready code (controllers, services, tests).
```
