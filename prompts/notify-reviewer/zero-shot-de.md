# NotifyReviewer Feature - Zero-Shot Prompt (Deutsch)

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
```

## Offene Fragen

- Ereignisgesteuert oder direkt im Service?
- Welches Mail-Framework?
- Synchronous vs. Async?
- Wie viel Testabdeckung?
- Wie wird Security berücksichtigt?
