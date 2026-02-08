
# 🇬🇧 `README.md`

# Customer Service Assistant 🤖

![Use Case](https://img.shields.io/badge/Use%20Case-Customer%20Support%20AI-0A66C2)
![Method](https://img.shields.io/badge/Method-Retrieval%20Augmented%20Generation-FF6F00)
![LLM Ops](https://img.shields.io/badge/LLM%20Ops-Grounded%20Responses-6A1B9A)
![Risk Control](https://img.shields.io/badge/Risk-Hallucination%20Mitigation-AD1457)
![Memory](https://img.shields.io/badge/Capability-Multi--Turn%20Dialogue-00897B)
![Deployment](https://img.shields.io/badge/Deployment-Streamlit%20Prototype-2E7D32)
---

Translations: [English](README.md) | [German](./translations/DE/README.md)

## 📸 Application Preview

> Here I'll replace the image screenshots later.

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

## 👤 Autor

**Pete Chisamba**
Applied AI | Data & GenAI Solutions

💡 My project showcases:
**real product thinking • safety • enterprise relevance • GenAI maturity**