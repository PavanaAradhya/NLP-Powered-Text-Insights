<h1>🔍 NLP-Powered Text Insights</h1>

  <div class="box">
        <p>
            This project is a simple and interactive web-based NLP tool built using <strong>Streamlit</strong>.  
            It performs multiple natural language processing tasks like sentiment analysis, keyword extraction, 
            tokenization, POS tagging, and named-entity recognition. Designed for beginners, this project helps 
            users understand how real-world NLP applications work in a clean and user-friendly interface.
        </p>
    </div>

  <h2>📌 Features</h2>
    <ul>
        <li> Sentiment Analysis</li>
        <li> Keyword Extraction</li>
        <li>Tokenization & POS Tagging</li>
        <li>Named Entity Recognition (NER)</li>
        <li>Clean UI with separate result sections</li>
    </ul>

  <h2>📁 Project Files</h2>
    <pre>
📦 NLP-Powered-Text-Insights/
│
├── app.py              → Main Streamlit application  
├── requirements.txt     → All needed Python libraries  
├── README.html          → Project documentation  
    </pre>

  <h2>⚙️ Requirements</h2>
    <pre><code>
pip install streamlit textblob spacy
python -m spacy download en_core_web_sm
    </code></pre>

  <h2>▶️ How to Run</h2>
    <ol>
        <li>Open CMD inside the project folder.</li>
        <li>Run the Streamlit app using:</li>
    </ol>

  <pre><code>
streamlit run app.py
    </code></pre>

  <p>The browser will automatically open with your NLP tool.</p>

  <h2>📤 Output</h2>
    <ul>
        <li>Sentiment result (Positive, Negative, Neutral)</li>
        <li>Extracted keywords</li>
        <li>Tokens with POS tags</li>
        <li>Named entities highlighted</li>
    </ul>

  <h2>🔗 References</h2>
    <ul>
        <li><a href="https://streamlit.io/" target="_blank">Streamlit Documentation</a></li>
        <li><a href="https://spacy.io/" target="_blank">spaCy NLP Library</a></li>
        <li><a href="https://textblob.readthedocs.io/" target="_blank">TextBlob Guide</a></li>
    </ul>

