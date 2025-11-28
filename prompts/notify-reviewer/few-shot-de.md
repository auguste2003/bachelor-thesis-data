# NotifyReviewer Feature - Few-Shot Prompt (Deutsch)

```
AK:

Wenn ein Nutzer über "Frage erstellen" eine Frage in Review gegeben hat (eine Frage erstellt hat), dann sollen die Reviewer mit einer Email benachrichtigt werden.

Inhalt der Email
Absender: noreplay-ocplernplattform@adesso.de
Empfänger: <Reviewer Name>
in den Empfängern sollen nicht alle Reviewer stehen.
als Empfänger steht nur die Person, die die Nachricht enthält.
Betreff: 'Eine neue Frage wurde erstellt "<Name der Frage>"'
Inhalt:
Hallo Reviewer <Vorname/username>,

es wurde eine neue Frage in der OCP-Lernplattform erstellt. Du als Reviewer kannst die erstellte Frage prüfen. Wenn alles korrekt ist, dann gerne genehmigen, so dass die Frage in den Fragenkatalog aufgenommen wird. Falls es Verbesserungsvorschläge, hinterlasse gerne dem Frage-Ersteller einen Kommentar und sende die Frage zurück.

Link: <erstellte Frage im Status Review>

Viele Grüße,

Dein OCP-Lernplattform Team

Falls der Nutzer keinen Vornamen eingetragen hat, wird der username genommen.

**Hier sind ein paar Beispiele, die dabei helfen können:**

- KeyCloak Client erstellen
```java
@Bean
    public Keycloak keycloak() {
        KeycloakBuilder builder = KeycloakBuilder.builder()
                .serverUrl(serverUrl)
                .realm(adminRealm)
                .clientId(clientId)
                .resteasyClient(new ResteasyClientBuilderImpl().connectionPoolSize(10).build());

        // Production: Service Account (client_credentials)
        if (clientSecret != null && !clientSecret.isEmpty()) {
            log.info("Initializing Keycloak Admin Client with CLIENT_CREDENTIALS grant (Production mode)");
            return builder
                    .grantType("client_credentials")
                    .clientSecret(clientSecret)
                    .build();
        }

        // Development: Username/Password
        if (username != null && !username.isEmpty() && password != null && !password.isEmpty()) {
            log.warn("Initializing Keycloak Admin Client with PASSWORD grant (Development mode) - NOT FOR PRODUCTION!");
            return builder
                    .username(username)
                    .password(password)
                    .build();
        }

        throw new IllegalStateException(
            "Keycloak admin client configuration incomplete. " +
            "Either set 'keycloak.admin.client-secret' (production) or " +
            "'keycloak.admin.username' and 'keycloak.admin.password' (development)."
        );
    }
```

- Einen Reviewer benachrichtigen

```java
 private void sendReviewerNotification(String reviewerEmail, String reviewerName,
                                         UUID questionId, String questionTitle, String questionType) throws MessagingException {

        String questionLink = String.format("%s/fragen/%s/%s?source=review", frontendUrl, questionType, questionId);

        Map<String, Object> templateVariables = new HashMap<>();
        templateVariables.put("reviewerName", reviewerName);
        templateVariables.put("questionTitle", questionTitle);
        templateVariables.put("questionLink", questionLink);
        templateVariables.put("appName", appName);

        String emailContent = emailTemplateService.renderTemplate(
            "email/reviewer-notification",
            templateVariables
        );

        String subject = String.format("Eine neue Frage wurde erstellt \"%s\"", questionTitle);

        emailService.sendHtmlEmail(reviewerEmail, subject, emailContent);
  }
```

- Wir wollen die Implementierung so produktionsnah wie möglich machen
- Die Clean Code Regeln wollen wir auch folgen
- Unsere Implementierung sollte zwischen 80-90% schön getestet werden
- Du kannst natürlich deine eigene Logik brauchen. Wir brauchen die beste Lösung.

**WICHTIG:**
Die gezeigten Beispiele sind nur Beispiele und dienen NICHT als Implementierungsauftrag.

Analysiere ausschließlich den existierenden Code und arbeite innerhalb der bestehenden Architektur.
Best Practices sollen nur innerhalb der bestehenden Struktur angewendet werden.

Implementiere NUR das beschriebene Feature in der vorhandenen Codebasis.
```
