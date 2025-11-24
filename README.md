<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>NLP-Powered Text Insights — README</title>
  <style>
    :root{
      --bg:#ffffff;
      --card:#f8fafc;
      --accent:#4CAF50;
      --muted:#6b7280;
      --mono: 'Courier New', monospace;
      --radius:10px;
      --maxw:960px;
    }
    body{
      margin:0;
      font-family: Inter, Arial, Helvetica, sans-serif;
      background: linear-gradient(135deg,#ffffff 0%, #f2f4f8 100%);
      color:#0f172a;
      display:flex;
      justify-content:center;
      padding:40px 16px;
    }
    .container{
      width:100%;
      max-width:var(--maxw);
    }
    .card{
      background:var(--card);
      padding:28px;
      border-radius:var(--radius);
      box-shadow:0 6px 24px rgba(15,23,42,0.06);
      margin-bottom:18px;
    }
    h1{ margin:0 0 6px 0; font-size:26px; }
    p.lead{ margin:0 0 18px 0; color:var(--muted); }
    h2{ margin-top:18px; color:#0b1220; }
    ul{ margin:8px 0 12px 20px; color:#0b1220; }
    pre{ background:#0b1220; color:#e6fffa; padding:12px; border-radius:8px; overflow:auto; font-family:var(--mono); font-size:13px; }
    code{ background:#eef2ff; padding:2px 6px; border-radius:6px; font-family:var(--mono); }
    .badge{ display:inline-block; background:var(--accent); color:white; padding:6px 10px; border-radius:999px; font-size:13px; margin-right:8px; }
    .muted{ color:var(--muted); font-size:14px; }
    .grid{ display:grid; grid-template-columns:1fr 1fr; gap:12px; }
    @media(max-width:720px){ .grid{ grid-template-columns:1fr; } }
    .code-title{ font-weight:600; margin-bottom:6px; }
    .footer{ text-align:center; margin-top:10px; color:var(--muted); font-size:13px; }
    .screenshot{ width:100%; border-radius:8px; border:1px solid #e6eef6; }
  </style>
</head>
<body>
  <div class="container">
    <div class="card">
      <h1>NLP-Powered Text Insights</h1>
      <p class="lead">A simple, clean Streamlit web app that analyzes text using NLP. It provides sentiment analysis, keyword extraction, text statistics, and Named Entity Recognition (NER).</p>

      <div style="margin:12px 0;">
        <span class="badge">Streamlit</span>
        <span class="badge" style="background:#0066cc">spaCy</span>
        <span class="badge" style="background:#ff7a59">TextBlob</span>
      </div>

      <h2>Features</h2>
      <ul>
        <li>Sentiment Analysis (Positive / Negative / Neutral)</li>
        <li>Top Keywords extraction</li>
        <li>Word count, sentence count, character count</li>
        <li>Estimated reading time and most frequent word</li>
        <li>Named Entity Recognition (NER) with visual highlighting</li>
        <li>Upload <code>.txt</code> files for analysis</li>
      </ul>

      <h2>Project Structure</h2>
      <pre>
NLP-Powered-Text-Insights/
├── app.py
├── generate_report.py
├── requirements.txt
├── README.html
└── (optional) NLP_Powered_Text_Insights_Report.pdf
      </pre>

      <h2>Installation & Setup</h2>
      <p class="muted">Follow these commands in your terminal (Windows example shown).</p>

      <div class="grid">
        <div>
          <div class="code-title">1. Create & activate venv</div>
          <pre>
python -m venv .venv
.venv\Scripts\activate
          </pre>
        </div>

        <div>
          <div class="code-title">2. Install dependencies</div>
          <pre>
pip install -r requirements.txt
python -m textblob.download_corpora
python -m spacy download en_core_web_sm
          </pre>
        </div>
      </div>

      <h2>Run the App</h2>
      <pre>streamlit run app.py</pre>
      <p class="muted">If a browser doesn't open automatically, visit <code>http://localhost:8501</code>.</p>

      <h2>Generate PDF Report (Optional)</h2>
      <pre>
pip install fpdf2
python generate_report.py
# Output: NLP_Powered_Text_Insights_Report.pdf
  </pre>

  <h2>How It Works (Short)</h2>
      <p class="muted">User input (typed or uploaded) → processed by TextBlob (sentiment) and spaCy (NER, tokens) → metrics computed (counts, reading time, keywords) → results shown in Streamlit UI → NER visualized with displaCy.</p>

  <h2>Usage Tips</h2>
      <ul>
        <li>Use short to medium paragraphs for best keyword results.</li>
        <li>Large files may take longer to process — test with smaller samples first.</li>
        <li>If you see NLTK/punkt errors, run: <code>python -m nltk.downloader punkt</code> (only if needed).</li>
      </ul>

  <h2>Screenshots</h2>
      <p class="muted">Add screenshots of your running app here (optional).</p>
      <!-- Replace src with your screenshot path if available -->
      <img class="screenshot" src="" alt="Screenshot (add file path if you have one)">

  <h2>License & Author</h2>
      <p class="muted">Author: Pavana C — B.E. in Artificial Intelligence</p>
      <p class="muted">License: MIT (recommended)</p>

  <div class="footer">Made with ❤️ • NLP-Powered Text Insights</div>
    </div>
  </div>
</body>
</html>
