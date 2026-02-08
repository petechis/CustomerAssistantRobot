# 🇩🇪

# Kundenservice Assistent 🤖

![Einsatz](https://img.shields.io/badge/Einsatz-Kundenservice%20KI-0A66C2)
![Methode](https://img.shields.io/badge/Methode-Retrieval%20Augmented%20Generation-FF6F00)
![LLM Betrieb](https://img.shields.io/badge/LLM%20Ops-Grounding-6A1B9A)
![Risiko](https://img.shields.io/badge/Risiko-Halluzinationskontrolle-AD1457)
![Fähigkeit](https://img.shields.io/badge/Fähigkeit-Mehrstufiger%20Dialog-00897B)
![Deployment](https://img.shields.io/badge/Deployment-Streamlit%20Prototyp-2E7D32)

Übersetzung: [English](../EN/README.md) | [German](README.md)


## 📸 Anwendungsvorschau

> <font color="orange"><i>Hier werde ich später mit den Bildscreenshots ersetzen.</i></font>

| Chat Oberfläche | Beispiel |
| --- | --- |
| ![Produkt name?](../../docs/images/app_home.png) | ![Siavonga Schokolade.](../../docs/images/chat_example.png) |

---

## 📌 Projektziel

Das Projekt zeigt, wie **LLMs** mithilfe von  
**Retrieval Augmented Generation (RAG)** sicher mit Unternehmensdaten verbunden werden.

Der Assistent antwortet **ausschließlich auf Basis freigegebener Produktinformationen**.

Ein realistisches Szenario für:

- Handel  
- Service Center  
- interne Wissenssysteme  
- Vertriebsunterstützung  

---

## 🧠 Visuelle RAG Pipeline

```

Nutzerfrage
↓
Konversationsspeicher
↓
Produkt-Retrieval
↓
Kontext im Prompt
↓
OpenAI LLM via LangChain
↓
Kurze, kontrollierte Antwort
```

## ⚙️ Funktionsweise

### Retrieval
Produktdaten kommen aus `product.py`.

### Grounding
`product_info.py` erzeugt daraus den Kontext.

### Guardrails
Der Prompt verbietet:
- Halluzinationen  
- Annahmen außerhalb des Katalogs  
- Off-Topic Antworten  

### Generierung
LangChain kombiniert Kontext, Verlauf und Frage.

### Memory
Ermöglicht Dialoge über mehrere Schritte.

### UI
Streamlit liefert eine sofort nutzbare Oberfläche.

---

## 🗂 Projektstruktur

```

.
├── app.py
├── product.py
├── product_info.py
├── sidebar_component.py
├── requirements.txt
├── LICENSE
└── README.md

````

---

## 🚀 Funktionen

✅ KI-Verkaufsberater  
✅ Faktenbasierte Antworten dank RAG  
✅ Halluzinationskontrolle  
✅ Promptsteuerung  
✅ Mehrstufige Dialoge  
✅ Schnell einsetzbare Demo  

---

## ▶️ Anwendung starten

```bash
pip install -r requirements.txt
streamlit run app.py
````

API-Key links einfügen.

---

## 🎯 Für Recruiter – Warum relevant?

Beweist Kompetenz in:

✔ Entwicklung produktionsnaher GenAI Systeme

✔ Anbindung strukturierter Daten an LLMs

✔ Prompt Engineering

✔ State Management

✔ nutzerorientierte AI Interfaces

Typische Anforderungen moderner **Applied AI Teams**.

---

## 🧩 ATS / Skill Keywords

`LLM` `RAG` `LangChain` `OpenAI API` `Prompt Engineering`  `Conversational AI` `Grounded Generation` `Streamlit` `Python` `AI Produktentwicklung`

---

## 🔒 Datenschutz

Keine Speicherung von API-Keys oder Gesprächen.

---

## 👤 Autor

**Pete Chisamba**
Applied AI | Data & GenAI Solutions

💡 My project showcases:
**real product thinking • safety • enterprise relevance • GenAI maturity**

