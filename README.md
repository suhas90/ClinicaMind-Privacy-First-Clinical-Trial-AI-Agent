# ClinicaMind-Privacy-First-Clinical-Trial-AI-Agent


ClinicaMind is a fully offline, secure, and private AI Agent designed to analyze complex clinical trial studies and medical research documents. Powered by **LangChain**, **ChromaDB**, and **Ollama**, this system runs entirely on your local machine, ensuring 100% data confidentiality and zero data leaks to third-party cloud servers.

Optimized to leverage local compute capabilities, including the **Intel Core Ultra 7 NPU (Neural Processing Unit)** and **32GB RAM**.

---

##  Key Features
- **100% Private & Offline:** No internet required after setup. Your sensitive clinical data stays on your machine.
- **RAG Architecture:** Uses Retrieval-Augmented Generation to eliminate AI hallucinations and provide evidence-backed answers.
- **Hardware Optimized:** Ready to run efficiently on high-end laptops without needing dedicated Nvidia GPUs.
- **Clean Web Interface:** Simple, easy-to-use UI built with semantic HTML and CSS.

---

## 📂 Project Architecture

```text
Clinical-AI-Agent/
│
├── backend/
│   ├── app.py              # Main Flask Backend API
│   ├── chroma_db/          # Local Vector Database (Auto-generated)
│   └── documents/          # Place your Clinical Trial PDF/Text files here
│
├── frontend/
│   └── index.html          # Web User Interface (UI)
│
├── requirements.txt        # Python Dependencies
└── README.md               # Documentation
```

---

##  Installation & Setup (Step-by-Step)

### Prerequisites
1. **Python 3.10+** installed on your system.
2. **Ollama** installed from [ollama.com](https://ollama.com).

### Step 1: Initialize the Local AI Model
Open your Command Prompt (CMD) or Terminal and pull the Llama 3 model:
```bash
ollama run llama3:8b
```
*Keep this terminal running or ensure the Ollama service is active.*

### Step 2: Clone the Project & Install Dependencies
Open your project directory in terminal and install the required Python packages:
```bash
pip install -r requirements.txt
```

### Step 3: Add Your Clinical Data
Place your clinical trial documents, research papers, or FDA submission reports (in **PDF** format) into the `backend/documents/` folder.

---

##  How to Run

### 1. Start the Backend API
Navigate to the root folder and start the Flask server:
```bash
python backend/app.py
```
You should see the server running on `http://127.0.0.1:5000`. Do not close this terminal.

### 2. Launch the Web Interface
- Open the `frontend/index.html` file by double-clicking it in your file explorer. It will open in your default web browser (Chrome, Edge, Brave, etc.).
- Click the blue button: **"Step 1: Update the new clinical database"** (Update Database). This will process your PDFs, split the text, and generate secure local vector embeddings in ChromaDB.
- Type your query in the chatbox below (e.g., *"What are the primary endpoints of the study?"*) and click **"Ask."** (Ask).

---

## 🔒 Safety & Disclaimer
This tool is an AI assistant developed for academic and data analysis optimization purposes. Always cross-verify critical medical/clinical findings with certified domain experts and official trial registries.

