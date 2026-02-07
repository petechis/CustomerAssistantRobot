
# 🇬🇧 `README.md`

# Customer Service Assistant 🤖

![Use Case](https://img.shields.io/badge/Use%20Case-Customer%20Support%20AI-0A66C2)
![Method](https://img.shields.io/badge/Method-Retrieval%20Augmented%20Generation-FF6F00)
![LLM Ops](https://img.shields.io/badge/LLM%20Ops-Grounded%20Responses-6A1B9A)
![Risk Control](https://img.shields.io/badge/Risk-Hallucination%20Mitigation-AD1457)
![Memory](https://img.shields.io/badge/Capability-Multi--Turn%20Dialogue-00897B)
![Deployment](https://img.shields.io/badge/Deployment-Streamlit%20Prototype-2E7D32)
---

## 📸 Application Preview

> Replace the images with your own screenshots later.

| Chat Interface | Example Conversation |
|---|---|
| ![](docs/images/app_home.png) | ![](docs/images/chat_example.png) |

---

## 📌 Purpose of the Project

This project demonstrates how **Large Language Models (LLMs)** can be safely connected to **external knowledge sources** using **Retrieval Augmented Generation (RAG)**.

Instead of guessing, the assistant answers **strictly from approved product data**.

This mirrors how real enterprise AI systems are deployed in:

- retail  
- support centers  
- internal knowledge systems  
- sales environments  

---

## 🧠 Visual RAG Pipeline

```

User Question
↓
Conversation Memory
↓
Product Retrieval (allowed categories)
↓
Context Injection into Prompt
↓
OpenAI LLM via LangChain
↓
Short, Controlled Answer

```

---

## ⚙️ How It Works

### Retrieval
Structured catalog data is stored in `product.py`.

### Grounding
`product_info.py` filters allowed categories and transforms them into a context string.

### Guardrails
The prompt forces the model to:
- stay inside the catalog  
- avoid assumptions  
- decline unrelated topics  

### Generation
`LLMChain` combines:
✔ context  
✔ chat history  
✔ user input  

to produce helpful, concise responses.

### Memory
`ConversationBufferMemory` enables multi-turn dialogue.

### UI
Streamlit delivers a quick deployable interface with API key management.

---

## 🗂 Project Structure

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

## 🚀 Features

✅ Conversational AI shopping assistant  
✅ Enterprise-style RAG grounding  
✅ Hallucination reduction  
✅ Prompt-constrained responses  
✅ Multi-turn conversations  
✅ Follow-up questioning  
✅ Rapid prototype → production pattern  

---

## ▶️ How to Run

### Install
```bash
pip install -r requirements.txt
````

### Launch

```bash
streamlit run app.py
```

### Authenticate

Paste your OpenAI API key in the sidebar.

---

## 💬 Example Questions

* What products do you sell?
* Show laptops.
* Price of MacBook Pro?
* Do you offer wireless audio devices?

Outside knowledge →

> Sorry! I am unable to complete this request.

---

## 🎯 Recruiter – Why This Matters

This project proves practical capability in:

✔ building **grounded GenAI systems**
✔ reducing hallucinations
✔ connecting LLMs to structured data
✔ prompt engineering with behavioral control
✔ managing conversation state
✔ delivering usable business interfaces

It reflects real tasks inside **GenAI, Applied AI, and AI Product teams**.

---

## 🏢 Real-World Extensions

The same pattern scales to:

* enterprise search
* policy assistants
* technical documentation bots
* customer support automation
* retail & robotics interfaces
* sales copilots

---

## 🧩 ATS / Skill Keywords


`LLM` `RAG` `LangChain` `OpenAI API` `Prompt Engineering`
`Conversational AI` `Grounded Generation` `Hallucination Mitigation`
`Streamlit` `Python` `AI Product Development`
`Chatbot Architecture` `Context Injection`

---

## 🔒 Privacy

No API keys or conversations are stored.

---

## 👤 Author

**Pete Chisamba**
Applied AI | Data & GenAI Solutions
# 🇩🇪

# Kundenservice Assistent 🤖

![Einsatz](https://img.shields.io/badge/Einsatz-Kundenservice%20KI-0A66C2)
![Methode](https://img.shields.io/badge/Methode-Retrieval%20Augmented%20Generation-FF6F00)
![LLM Betrieb](https://img.shields.io/badge/LLM%20Ops-Grounding-6A1B9A)
![Risiko](https://img.shields.io/badge/Risiko-Halluzinationskontrolle-AD1457)
![Fähigkeit](https://img.shields.io/badge/Fähigkeit-Mehrstufiger%20Dialog-00897B)
![Deployment](https://img.shields.io/badge/Deployment-Streamlit%20Prototyp-2E7D32)

---

## 📸 Anwendungsvorschau

> Screenshots können später ergänzt werden.

| Chat Oberfläche | Beispiel |
|---|---|
| ![](../../docs/images/app_home.png) | ![](../../docs/images/chat_example.png) |

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

`LLM` `RAG` `LangChain` `OpenAI API` `Prompt Engineering`
`Conversational AI` `Grounded Generation`
`Streamlit` `Python` `AI Produktentwicklung`

---

## 🔒 Datenschutz

Keine Speicherung von API-Keys oder Gesprächen.

---

## 👤 Autor

**Pete Chisamba**
Applied AI | Data & GenAI Solutions

💡 My project showcases:
**real product thinking • safety • enterprise relevance • GenAI maturity**

