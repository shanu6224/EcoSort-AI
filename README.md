# EcoSort AI 🌱

### AI-Powered Waste Segregation & Sustainable Disposal Assistant

**Identify. Segregate. Sustain.**

EcoSort AI is a sustainability-focused AI prototype designed to help users identify waste items and understand how they should be segregated and disposed of responsibly.

---

## 🌍 SDG Alignment

### Primary SDG
**SDG 12 – Responsible Consumption and Production**

### Secondary SDG
**SDG 11 – Sustainable Cities and Communities**

EcoSort AI supports responsible waste handling and promotes sustainable practices within educational and community environments.

---

## 🚨 Problem Statement

Improper waste segregation at the source is a common sustainability challenge. People may be uncertain about how to classify unfamiliar items such as plastic packaging, food waste, batteries, electronic accessories, and potentially hazardous materials.

When different types of waste are mixed, recyclable materials can become difficult to recover and unsuitable disposal can create environmental and safety concerns.

EcoSort AI aims to provide simple, item-specific guidance at the point of disposal.

---

## 💡 Proposed Solution

EcoSort AI provides an interactive interface where users can upload an image of a waste item.

The proposed AI workflow:

1. User uploads a waste image
2. AI analyzes the image
3. Waste item is identified
4. Waste is classified into an appropriate category
5. Disposal guidance is provided
6. A sustainability tip is displayed
7. Uncertain or potentially hazardous items receive appropriate caution

### Waste Categories

- ♻️ Recyclable
- 🍃 Organic
- 🗑️ General Waste
- 🔋 E-Waste
- ⚠️ Hazardous / Special
- ❓ Uncertain

---

## 🤖 AI Elements

The proposed AI architecture uses:

- **IBM Granite Vision** – multimodal image understanding
- **IBM watsonx.ai** – AI model platform
- **IBM BOB** – conversational AI layer
- **RAG (Retrieval-Augmented Generation)** – campus/local waste-disposal guidelines
- **Prompt Engineering** – structured and responsible AI responses
- **Confidence & Uncertainty Handling** – avoids forced classifications

---

## 🔄 AI Workflow

```text
Waste Image
     ↓
Image Analysis
     ↓
IBM Granite Vision
     ↓
Waste Identification
     ↓
Waste Classification
     ↓
RAG / Local Waste Guidelines
     ↓
IBM BOB
     ↓
Disposal Guidance
     ↓
Sustainability Tip
