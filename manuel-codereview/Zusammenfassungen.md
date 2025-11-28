# Copilot Zusammenfassungen
## copilot-claude45-zero-commentonblock
## copilot-claude45-zero-learningblock
### LearningBlock
- Die Implementierung hat 17 Minuten gedauert
- Hier ist die Antort von der KI
  10 unit tests for service layer (100% pass rate)
  10 integration tests with Testcontainers and PostgreSQL
  Estimated 80-90% coverage as requested

- Aber 14 von 20 Tests sind dann erfolreich durchgelaufen
- Die Validierungen laufen sehr gut und die Exceptions sind nicht getestet worden.
- Die Fehlermeldung nach der Validierung ist für den Frontendentwickler nicht so eindeutig
- Das Erstell- und Aktualisierungsdatum sind nicht beim Erstellen des Blocks gesetzt
- Für unbefügte Zugriffe zu Blöke kriegt man eher ``500`` an der Stelle von einem 403
- Man kriegt auch eine 500, wenn man einen anderen Block bearbeiten will
- LearningBlockCreteRequest und LearningBlockUpdateRequest sind duplicate
- Man kann Blöcke duplicate hinzufügen

### CommentOn LearningBlock
- von 10 Junittetss sind 0 fehlgeschlagen und 18 Integrationsstests, die erfolgreich waren. Also die 28 Tests sin durchgelaufen
- Die IMPLEMENTIERUNG HAT 20 Minuten gedauert
- Es gab allerding ein paar Exceptions, die nicht abgedeckt worden sind.(BlockNotFoundException)
- Die Implementierung erfüllt alle Anforderungen
- Die Fehlermelungen sind sehr verständlich
- Man siht duplicate in der `BloackCommentIntegrationTest` Klasse. Die Datenbank wird da noch neu initialisiert. Es gab schon Testdaten in dem Script und der Agent hat diese Logik nicht verstanden, weil ich das nicht explizit gesagt habe.


## copilot-claude45-zero-exportreviewcatalog
Man muss die KI schon genauer sagen, was mer nicht machen soll.

- Die Generierung hat 10 Minuten gedauten.
- Die KI hat den Import und Export robust implementierung
- Die Abnahmetests sind gut
- Es werde keine duplizierten Fragen importiert
- Die Rückmeldungen und Fehlermeldungen sind sehr gut dokumentiert ohne komplizierte und unverständliche straces

Implementierung:
- Nur der Reviewer importiert und exportiert die Fragen.
- Es gibt formulierte Antworten für 401,403, 500, 400 und 200
- Die Datei ist als Multipart hinterlegt und muss maximal 10 Mo groß sein
- Man kriegt ein Json zurück
- Ignoriert werden alle Fragen, die schon in der Datenbank stehen.
- Neue DTO für import und export
- zentrale Verwaltung von Exceptions
- Es werden 9 neue Klassen erstellt
- 2 DTOs, 1 Service, 1 Controller, 3 Exceptions, 1 Exceptionshandler, 1 Unitest , 1 Integrationstest
- Der Code kompiliert
- 13 von 14 Unit Tests passen (Problem mit der Konfiguration von einem Mock)
- 7 von 15 Integration Tests passen (Problem mit Security Config)

Bemerkungen:
- Der Agent hat sich wirklich an den Informationen angehalten und einen Clean Code mit Tests dazu produziert
- Der Rückgabetype beim Export ist anders als den von dem Katalog und das ist, weil wir im Prompt nicht explizit gesagt haben.
- Die Implementierung ist auch gut Dokumentiert aber die Testethoden brauchen auch Dokumentationen
- Der Agent erstellt am Ende immer ein Bericht in Form einer Dokumentation von seinen Implementierungen

Verbesserungen:
- Der Rückgabetyp von allen Imports muss gleich sein
- Der Agent sollte Code ändern dürfen, aber mit Begründung und vor allem nur, wenn er feststellt, dass diese eventuelle Duplikationen vermeidet. Er muss den Code anpassen und nicht die Logikimplementation von anderen Features ändern.

## copilot-claude45-zero-notifyreviewer
- Die implementierung hat ungefähr 20 Minuten gedauert
- Das Verstanden von  dem Code hat 2 Stunden gedauert
- Die Qualität sieht insgesamt gut aus aber der Mailversand funktioniert nicht. Ich kriege ständig eine 401.
- Man muss sich mit dem Clienttoken zuerst authentifizieren und danach einen AccessToken holen, mit dem man
  auf die Liste von Nutzen mit einer bestimmten Rolle holen kann.

Man kann den Token so holen
````
curl -X POST "http://localhost:8081/realms/ocpRealm/protocol/openid-connect/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  -d "client_id=ocp-admin-client" \
  -d "client_secret=NqriqJmXEfsgW6lXeOr4BFGodGYkeHSr"
````

- Danach kann man das in den .env hinzufügen

### Bewertung
- Der vorgeschlagene Code ist nicht für die Produktion robust genug, das kann nur für Test eingesetzt werden.
- Die Methode ist allerdings eine sehr gute, weil man fügt keine unnötige große Bibliotheke, die die Sachen erschwert.
- Vielleicht muss ich in einer zweiten Iteration mir dem Agent noch mal über die Fehlermeldung sprechen.
- Man sieht hiermit, dass der Agent nicht eigenständig beim Backendentwicklung arbeiten kann. Es gibt die Wahl zwischen sehr vielen Methoden und best practices. Man kann Bibliotheken vermeiden und die Aufgabe immer lösen. Also
  ein menschliche Unterstützung.
- Die Mail wird hier schon asynchron gesendet und man braucht dafür nicht zwingend ein Event

## copilot-claude45-few-commentonblock
## copilot-claude45-few-learningblock

11:22 - 11:42 -> 20
- Die Implementierung hat 20  Minuten gedauert.
- Der Code ist sehr gut kommentiert. Das muss ich ehrlich sagen.
- Der TestCode ist mit @Nested struktuiriert und das verbessert die Lesbarkeit von dem Code.
- In jedem @Nested Klasse werden private Variablen definiert.
- von 23 Unit Tests sind 23 erfolgreich
- von 23 Integrationstests sind 23 erfolgreich
- Also 46/46 laufen und `passrate=100%`
- Der Line Coverage ist vielleicht zwischen 90-100%
-  Man braucht ehlich keine JUnit Tests mehr in diesem Code. die 23 Integrationstests waren schon ausreichend
- Die Implementierung wurde mit `Postman` getestet und funktioniert sehr gut.

## Zum Code
**Kurzbewertung des KI-Codes (LearningBlockController):**

**Stärken:**

* Sehr sauber strukturiert, klar dokumentiert, gute REST-Konventionen.
* Sinnvolle Trennung von Verantwortlichkeiten (Service → AuthZ-Logik).
* Vollständige Exception-Handler → konsistente API-Fehlerstruktur.
* Saubere Nutzung von `@AuthenticationPrincipal`, DTOs und Validation.
* Logging konsistent und hilfreich.

**Schwächen / Verbesserbar:**

* Controller etwas lang → könnte modularer werden (z. B. ErrorHandler als @ControllerAdvice auslagern).
* `getCurrentUserId()` enthält Test-Fallback – besser in Test-Konfiguration packen, nicht im Produktivcode.
* Das *UpdateAt* Datum ist immer null

**Fazit:**
**Sehr gute Qualität für KI-Code: klar, robust, verständlich, production-tauglich.** Nur kleine Architektur-Verbesserungen möglich.
**Kurzbewertung des KI-Codes (LearningBlockService):**

* Der Code ist sehr sauber strukturiert und klar lesbar
* Gute Trennung der Beziehungen
* Hilfreiche Warnungen bei `Unauthorized und Duplicate`
* Pagination und Visibility sind sehr sauber integriert
* Die Schreib-und Leseoperationen sind in einer ``Transaction order readOnly`` das verhindert `Race Condition`
* Der Flyway-Skript ist ausgezeichnet, professionell und sauber gestaltet.

## CommentOnBlock

* Der Code ist sehr gut kommentiert
* Die ExceptionsHandler können ausgeparkt werden. Diese werden alle in dem Controller implementiert und brechen die berühmten Regeln von `Separation of concerns`.
* Die Flyway Migration ist auch sehr sauber
* Es werden sehr wichtige und sinnvolle Tests geschrieben
* 18 von 18 JUnit Tests sind erfolgreich durchgelaufen
* 23 von 23 Integrationstests sind erfolgreich.
* Der `Passrate` väre ungefähr `100%`

**Schwächen**

* Der Agent hätte Testdaten für die Migration benutzen sollen
* JunitTests sind nicht mehr wichtig

## copilot-claude45-few-exportreviewcatalog

- Die Implementierung hat 10 Minuten gedauert
- Die Implementierung ist funktional korrekt und man kriegt auch eine Fehlermeldung
- Duplikate werden ignoriert
- Der Agent hat vielleicht mit *Duplication* in dem Promt nur Duplication von Daten verstanden und nicht von Code auch. Der aktuelle Code zeigt sehr viele Duplikate
- von 11 Unit Tests werden 2 schlagen fehl 2/11
- von 14 Integrations Tests schlagen 3 fehl 3/14

## copilot-claude45-few-notifyreviewer
- Der Code kompiliert nicht.
- Es fehlt ein @Bean für KeyCloak
- Die Implementierung sieht sehr gut aus.
- Die Tests laufen sehr gut und nur ein von dem schlägt fehl
- Über 26 Tests ist 1 fehlgeschlagen.
- Der Emailversand ist nicht ansychron und blockiert das Erstellen der Fragen. Es ist kein Problem, wenn der Mailversand nicht erfolgreich ist.

# Cursor Zusammenfassungen
## cursor-auto-zero-commentBlock
## **cursor-auto-zero-learningblock**
- Die Implementierung hat 5 Minuten gedauert
- Der Code ist kompakt und sauber.
- Jeder kann die gesamte Liste von Blöcken holen, wenn er authentifiziert ist.
- Das heit die `PRIVATE` Blöcke werden zusammen mit den `PUBLIC` Blöcken zurückgegeben
- Es gibt eine sehr gute Trennung zwischen den Controller und Service.
- Man extrahiert den Nutzername aus dem Token eher in dem Service.
- Es gibt duplikate beim Blocks

**Test**
* 1/1 Integration ist erefolgreich durchgelaufen
* Dabie hätte er die Instanz von dem TestContainer aus der TestContainerConfig Klasse nutzen können.
* 6/6 Unitest sind erfolgreich

**Postman**
* Hier ist die Liste von Blocks, die `bob` kriegt. Dabei sieht man die privaten Blöcke von `admin`
````json
[
    {
        "blockId": "179e0b7e-c522-477b-b47a-54bbd140f600",
        "blockTitle": "Introduction to Spring Boot",
        "description": "# Spring Boot Basics\n\nLearn the fundamentals of Spring Boot framework.",
        "visibility": "PRIVATE",
        "createdBy": "admin",
        "createdAt": "2025-11-16T14:03:12.053327"
    },
    {
        "blockId": "3ae8644f-79b2-4bb3-8e6e-e4916e9edd55",
        "blockTitle": "Introduction to Spring Boot",
        "description": "",
        "visibility": "PRIVATE",
        "createdBy": "admin",
        "createdAt": "2025-11-16T14:03:28.292944"
    },
    {
        "blockId": "55082b20-1242-4bac-9117-13eecf15e95a",
        "blockTitle": "Introduction to Spring Boot",
        "description": null,
        "visibility": "PRIVATE",
        "createdBy": "admin",
        "createdAt": "2025-11-16T14:03:43.837212"
    },
    {
        "blockId": "9e376773-b756-47b7-b370-12b0cdb23541",
        "blockTitle": "Introduction to Spring Boot",
        "description": null,
        "visibility": "PRIVATE",
        "createdBy": "admin",
        "createdAt": "2025-11-16T14:04:41.763514"
    },
    {
        "blockId": "bc532ea7-ddb7-4a86-897c-bb50f759b6c9",
        "blockTitle": "Introduction to Spring Boot",
        "description": null,
        "visibility": "PRIVATE",
        "createdBy": "admin",
        "createdAt": "2025-11-16T14:04:54.416558"
    },
    {
        "blockId": "257685c1-31e4-4f61-a546-b530ed86e749",
        "blockTitle": "Introduction to Spring Boot",
        "description": null,
        "visibility": "PRIVATE",
        "createdBy": "admin",
        "createdAt": "2025-11-16T14:04:56.485901"
    },
    {
        "blockId": "dba5af90-0ffe-41ee-9a59-735c1a328e36",
        "blockTitle": "Introduction to Spring Boot",
        "description": null,
        "visibility": "PRIVATE",
        "createdBy": "bob",
        "createdAt": "2025-11-16T14:06:56.676742"
    },
    {
        "blockId": "a4e9ffb9-644e-49fe-8807-0237d736fb53",
        "blockTitle": "Introduction to Spring Boot",
        "description": null,
        "visibility": "PRIVATE",
        "createdBy": "bob",
        "createdAt": "2025-11-16T14:07:00.101305"
    }
]
````

## CommentOnRepository
* Die Implementierung hat 13 Minuten gedauert
* Der Agent hat neuen Code hinzugefügt, der scheinbar gut kompiliert
* Er hat dann Änderung an einer anderen Klasse `CommentRepository` gemacht, was eine verwechlung war.
* Nachdem er die Verwelchsung entdeckt hat, wusst er nicht mehr was davor in der Repository als Methoden gabe
* Er hat direkt ein leeres Repository erstellt und das hat dann Fehlermeldungen im Code erzeugt.
* Der Code kompiliert nicht.

## cursor-auto-zero-exportreviewcatalog
7:56 -
- Cursor versteht einscheinend kein Deutsch.
- Die Beschreibung von dem Feature und auf Deutsch und ist nicht so spezifisisch
- Der Agent sucht gerade nach einer Implementierung von dem Emailversand

Vorschlag: Ich muss in meiner Beschreibung vielleicht ein bisher spezifischer sein.
Aber ich darf die Beschreibung trotzdem nicht ändern, deshalb werde ich einen neuenn Chat öffnen und das noch mal probieren.

# Pair Programming Zusammenfassungen
## reference-learningblock
## eference-commentonblock
- Die Implementierung hat 6 Stunden gedauert
- Ich hatte vorher eine Implementierung gemacht von Entity bis zu Controller
- Dabei hatte ich noch keine FlywayMigration hinzugefügt.
- Ich hatte keine Checkliste vorbereitet
- Ich habe den Agenten gefragt, ob er die vorgeschlagene Richtung gut findet.
- Er hat meine Arbeit mit 5/10 bewerten.
- Hat einen Vorschlag von einer Checkliste unterbreitet
- Ich habe die Liste gefolgt.
- Danach habe ich weiter Implementierung gemacht, mit Validierungen aber es war mir ein bischen schwer die Exceptions und Fehlermeldungen zu catchen. Das habe ich geschafft und der Agent hat dabei Code vorgeschlagen, den ich akzeptiert und abgelehnt habe.
- Wir haben zusammen `44 Tests` geschrieben und erreichen sicherlich einen Coverage von mehr als 95% im neuen Code.
- Mir war es wichtig, dass wir nicht Line Coverage erzielen, sondern dass wir die Validierungen teste, alle Exception auch testen, die vorkommen können. Das war mir sehr wichtig.
- Wir haben vermieden, dass ein gleicher Benutzer `duplicate Fragen` erstellt
- Die Test haben wir über Flayway getestet und die Migration funktioniert sehr gut.
- Wir haben die Endpunke über postman getestet und sie funkionieren sehr gut.

## Features
- Der Nutzer kann ein Learning Book hinzufügen, aktualisieren, holen und löschen.
- Nur der Ersteller darf löschen und aktualisieren
- Der aktualle Benutzer kann die Liste von seinen Blocken `PRIVATE und PUBLIC` mit `myBlocks=true` holen. NUR sein Blöcke
- Ansonstens kriegt der Nutzer die Liste von allen `PUBLIC` Blöcken
- Der Code ist gut dokumentiert und man kriegt saubere Fehlermeldungen.



# CommentOnLearningBlock
````
I started with the implementation of the comment on learning block. How do you find the actual implementation ? I also need a checklist with best practices that we can follow. The goal is to have a covarage between 80-90% with 100% passed Tests.
````
- Critical Issues ⚠️
    + Missing save() call in commentBlock(): Comment is created but never persisted!
    + Incorrect relationship: @OneToOne should be @ManyToOne - multiple comments per block
    + Inefficient query in getCommentsForBlock(): Loading all comments then filtering in memory
      Missing commentId in response mapping: Response expects commentId but mapper doesn't set it

    + Validation issues in Response DTO: Using @NotBlank on UUID and LocalDateTime (wrong annotation)

    + Unused import: @P import in controller

    + Test Coverage Checklist (80-90% Covera

### My anwer
````
the critical issues first
````

### Agent
Missing save() call - Comment now persists to database in commentBlock()
Wrong relationship - Changed @OneToOne → @ManyToOne (multiple comments per block)
Inefficient query - Added findByLearningBlockBlockId() repository method instead of loading all comments
Missing commentId - Response mapper now includes commentId
Wrong validation - Removed @NotBlank from Response DTO (UUIDs and dates can't use @NotBlank)
Unused import - Removed @P import from controller
Syntax error - Added missing closing brace in controller

### My answers

````
Let us do this
````

Bemerkungen
- Die Implementierung hat 05 Stunden gedauert.
- Es wurde `61 Tests` geschrieben, die sehr gut durchgelaufen sind.
- Die Tests decken fast alle Fälle.
- Exceptions Valideerung, unbefügte Zugriffe, Erfolge
- Der Test in Postman ist auch sehr gut gelaufen. 

## cursor-auto-zero-notifyreviewer
10.11
19:00- 21:30

11.11
7:10 - 12:10
16:00 - 19:00

12.11
8:00 -
1. User: POST /api/v1/lueckentext/create
   ↓
2. LueckenTextService.saveLueckenText() | MCQMultipleService.saveLueckenText()
    - Speichert Question mit Status IN_REVIEW
    - Publisht: QuestionCreatedEvent(id, title,questionTyp)
      ↓
3. QuestionEventListener.onQuestionCreated() [@Async]
    - Läuft in separatem Thread
    - Hat eine eigene Transaktion
    - Ruft ReviewNotificationService auf
      ↓
4. ReviewNotificationService.notifyReviewersOfNewQuestion()
    - Holt alle Reviewer aus Keycloak
    - Für jeden Reviewer:
      ↓
5. EmailTemplateService.renderTemplate()
    - Rendert HTML mit Thymeleaf
    - Variables: reviewerName, questionTitle, questionLink
      ↓
6. EmailService.sendHtmlEmail()
    - Sendet Email via JavaMailSender
    - An: reviewer@email.com
    - Betreff: "Eine neue Frage wurde erstellt "Titel""
      ↓
7. MailHog empfängt Email (localhost:8025)


### Email-Inhalt

Von: noreply-ocplernplattform@adesso.de
An: [einzelner Reviewer - kein CC/BCC]
Betreff: Eine neue Frage wurde erstellt "Frage Titel"

Hallo Reviewer [Vorname oder Username],

es wurde eine neue Frage in der OCP-Lernplattform erstellt...

📝 "Frage Titel"

[Button: Frage jetzt prüfen →]
→ http://localhost:4200/fragen/{id}?source=review

Viele Grüße,
Dein OCP-Lernplattform Team

### MailHug starten
````
docker run -d -p 1025:1025 -p 8025:8025 --name mailhog mailhog/mailhog

Nutzliche Kommandos 
# Status prüfen
docker ps | grep mailhog

# Logs ansehen
docker logs mailhog

# Stoppen
docker stop mailhog

# Starten (wenn schon existiert)
docker start mailhog

# Entfernen
docker rm -f mailhog

````
- Email prüfen -> http://localhost:8025

### Mit Google Mail Application kann man auch senden
````
MAIL_HOST=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=name
MAIL_PASSWORD="pass"
````
-> Email in den Benutzer's Emails prüfen
### Anwendung starten
````
./gradlew bootRun
````

## erte Analyse von dem Code
![Erste Analyse mit SonarQube: Überblick der Qualität](email_1_sonarQube.png)