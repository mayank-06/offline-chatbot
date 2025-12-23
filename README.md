✨ Offline AI Customer Support Chatbot
<p align="center"> <img src="https://github.com/mayank-06/offline-chatbot/blob/main/ChatGPT%20Image%20Nov%2017,%202025,%2001_06_28%20AM.png?raw=true" alt="Offline AI Customer Support Chatbot Banner" width="90%" style="border-radius: 15px;"/> </p> <p align="center"> <img src="https://skillicons.dev/icons?i=python,streamlit,pytorch,git,github" height="60" /> </p>
<p align="center" style="font-size: 18px;"> A powerful <b>Offline Customer Support Chatbot</b> built using <b>Local LLM + RAG (Retrieval Augmented Generation)</b>. This chatbot works entirely <b>offline</b> without any API key — providing fast, secure, and accurate support responses using your own FAQ knowledge base. </p>
🚀 Features

⚡ Fully Offline — No API, No Internet

🧠 RAG-powered intelligent answers

📄 FAQ Upload + Auto Index Rebuild

🔍 FAISS Vector Search (Ultra Fast)

🎤 Voice Input (optional)

🔊 Voice Output (optional)

🎨 Modern Streamlit UI

📚 Reference-based answers

🧩 Modular code structure

📝 Auto chat history export

📊 Chat statistics dashboard

🧠 Tech Stack
<p align="center"> <img src="https://skillicons.dev/icons?i=python,streamlit,pytorch,vscode,git,github" height="70"/> </p> <p align="center"> <img src="https://img.shields.io/badge/RAG-Retrieval%20Augmented%20Generation-blueviolet?style=for-the-badge" /> <img src="https://img.shields.io/badge/FAISS-Vector%20DB-blue?style=for-the-badge" /> <img src="https://img.shields.io/badge/Local%20LLM-FLAN--T5-orange?style=for-the-badge" /> </p>


🏗 Project Structure
```
offline-chatbot/
│── app.py
│── main.py
│── README.md
│── requirements.txt
│
├── chains/
│ ├── retrieval_chain.py
│ └── response_chain.py
│
├── utils/
│ ├── db_utils.py
│ ├── memory_utils.py
│ ├── voice_utils.py
│ └── tts_test.py
│
├── data/
│ └── faqs.txt
│
└── faiss_index/
```

🔧 Installation:
```
git clone https://github.com/mayank-06/offline-chatbot.git
cd offline-chatbot

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```
Rebuild FAISS index:
```
python utils/db_utils.py

```
Run the app:
```
streamlit run app.py
```
🧩 How RAG System Works
1. Upload FAQ file  
2. Text → small chunks  
3. Embeddings generated (MiniLM)  
4. FAISS Vector DB stores embeddings  
5. User asks a question  
6. System retrieves relevant chunks  
7. Local LLM generates answer  
8. References returned

🔮 Future Enhancements
- PDF / DOCX based indexing  
- Multi-language responses  
- Offline Whisper for STT  
- Analytics dashboard  
- Advanced conversational memory

👨‍💻 Author
<p align="center"> <b>Mayank (mayank-06)</b> </p> <p align="center"> <a href="https://github.com/mayank-06"> <img src="https://skillicons.dev/icons?i=github" height="50"> </a> &nbsp;&nbsp; <a href="mailto:mayanksunny402@gmail.com"> <img src="https://skillicons.dev/icons?i=gmail" height="50"> </a> &nbsp;&nbsp; <a href="[https://www.linkedin.com/in/your-link-here/](https://www.linkedin.com/in/mayank-bodgujar-b89497319/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3Bzr2KbXjTRZKq9AFB3hMfSg%3D%3D)"> <img src="https://skillicons.dev/icons?i=linkedin" height="50"> </a> </p>
