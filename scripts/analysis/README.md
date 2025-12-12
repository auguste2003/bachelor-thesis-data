# Python Scripts für Bachelorarbeit: Codequalitätsanalyse

## Übersicht

Dieses Verzeichnis enthält alle Python-Scripts zur Generierung von Diagrammen und Tabellen für die Bachelorarbeit:

**"Analyse der Codequalität KI-generierten Codes im Vergleich zu manuell entwickeltem Code in der Webentwicklung"**

---

## Voraussetzungen

### Python-Pakete installieren:

```bash
pip install matplotlib numpy pandas
```

### Benötigte Dateien:

Stelle sicher, dass die folgenden CSV-Dateien im selben Verzeichnis sind:

- `branches_overall_metrics_normalized.csv`
- `pr_new_code_metrics_normalized.csv`
- `summary_new_code_metrics.csv`
- `summary_overall_metrics.csv`

---

## Scripts Übersicht

### 1. **generate_test_success_rate.py**
- **Ausgabe:** `test_success_rate.pdf`
- **Verwendung:** Kapitel 6.2 - Funktionale Korrektheit
- **Beschreibung:** Erstellt das Balkendiagramm mit Test Success Rate nach Feature und Variante

**Ausführen:**
```bash
python3 scripts/analysis/generate_test_success_rate.py
```

---

### 2. **generate_maintainability_overview.py**
- **Ausgabe:** `maintainability_metrics_overview.pdf`
- **Verwendung:** Kapitel 6.3 - Wartbarkeit des neuen Codes (Abbildung vor Tabelle 10)
- **Beschreibung:** Erstellt das 2×3 Subplot-Grid mit allen Wartbarkeitsmetriken

**Ausführen:**
```bash
python3 generate_maintainability_overview.py
```

---

### 3. **generate_delta_structural_quality.py**
- **Ausgabe:** `delta_structural_quality.pdf`
- **Verwendung:** Kapitel 6.4.2 (ursprünglich, wurde durch Tabelle ersetzt)
- **Beschreibung:** Erstellt Delta-Diagramm (Baseline → Overall) für strukturelle Qualität
- **Status:** Optional - in finaler Arbeit durch Tabelle ersetzt

**Ausführen:**
```bash
cd scripts/analysis &&  python3 generate_delta_structural_quality.py
```

---

### 4. **analyze_metrics_and_create_tables.py**
- **Ausgabe:** Console Output mit LaTeX-Code
- **Verwendung:** Alle Kapitel - Generiert LaTeX-Tabellen-Code
- **Beschreibung:** 
  - Analysiert alle CSV-Dateien
  - Berechnet Deltas (Baseline → Overall)
  - Generiert LaTeX-Code für Tabellen 10, 11, 12, 13, 14
  - Zeigt statistische Zusammenfassungen

**Ausführen:**
```bash
cd scripts/analysis &&  python3 analyze_metrics_and_create_tables.py > tables_latex_code.txt
```

---

### 5. **generate_all_visualizations.py** (MASTER-SCRIPT)
- **Beschreibung:** Führt alle anderen Scripts nacheinander aus
- **Verwendung:** Wenn du alle Diagramme auf einmal generieren willst

**Ausführen:**
```bash
python3 generate_all_visualizations.py
```

---

## Verwendung der Scripts in der Arbeit

### Kapitel 6.2 - Funktionale Korrektheit
- **Abbildung:** `test_success_rate.pdf`
- **Script:** `generate_test_success_rate.py`
- **Tabelle 6:** Daten manuell aus CSV

### Kapitel 6.3 - Wartbarkeit des neuen Codes
- **Abbildung:** `maintainability_metrics_overview.pdf`
- **Script:** `generate_maintainability_overview.py`
- **Tabelle 10:** LaTeX-Code aus `analyze_metrics_and_create_tables.py`

### Kapitel 6.4 - Einfluss auf die Gesamtcodebase
- **Tabelle 11 (∆-Werte):** LaTeX-Code aus `analyze_metrics_and_create_tables.py`
- **Diagramm (optional):** `delta_structural_quality.pdf`

### Kapitel 6.5 - Einfluss der Prompt-Strategie
- **Tabelle 12 & 13:** Daten aus `analyze_metrics_and_create_tables.py`

### Kapitel 6.6 - Vergleich der Implementierungsmethoden
- **Tabelle 14 & 15:** Daten aus `analyze_metrics_and_create_tables.py`

---

## Anpassungen

### Farben ändern:

In jedem Script findest du die Farbdefinitionen:

```python
colors = {
    'Referenz': '#1f77b4',      # Blau
    'Copilot-Zero': '#ff7f0e',  # Orange
    'Copilot-Few': '#9467bd',   # Violett
    'Cursor-Zero': '#2ca02c',   # Grün
    'Cursor-Few': '#d62728'     # Rot
}
```

### Daten ändern:

Die Daten können entweder aus den CSV-Dateien geladen werden oder sind direkt im Script definiert.

**CSV-basiert:**
```python
df = pd.read_csv('branches_overall_metrics_normalized.csv', sep=';')
```

**Manuell definiert:**
```python
data = np.array([
    [100.0, 70.0, 100.0, 54.5, 83.3],  # LearningBlock
    # ...
])
```

---

## Troubleshooting

### Problem: `ModuleNotFoundError: No module named 'matplotlib'`

**Lösung:**
```bash
pip install matplotlib numpy pandas
```

### Problem: CSV-Dateien nicht gefunden

**Lösung:**
Stelle sicher, dass die CSV-Dateien im selben Verzeichnis wie die Scripts liegen:

```bash
ls -la *.csv
```

### Problem: Diagramme werden nicht angezeigt

**Lösung:**
Wenn `plt.show()` nichts anzeigt, überprüfe dein Matplotlib-Backend:

```python
import matplotlib
print(matplotlib.get_backend())
```

Für Headless-Server (ohne GUI):
```python
import matplotlib
matplotlib.use('Agg')  # Backend für Dateien ohne Anzeige
```

---

## Kontakt & Support

Bei Fragen zu den Scripts:
- Überprüfe zuerst die Fehlerausgabe
- Stelle sicher, dass alle Pakete installiert sind
- Überprüfe die Datenpfade

---

## Lizenz

Diese Scripts sind Teil der Bachelorarbeit und für akademische Zwecke erstellt.

**Autor:** Teo  
**Datum:** Dezember 2024  
**Version:** 1.0
