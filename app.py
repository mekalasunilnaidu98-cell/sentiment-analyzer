import tkinter as tk
from tkinter import scrolledtext, messagebox
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze():
    text = input_box.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter some text.")
        return
    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]
    sentiment = "Positive" if compound >= 0.05 else "Negative" if compound <= -0.05 else "Neutral"
    result_var.set(f"Sentiment: {sentiment} | Confidence: {abs(compound):.2%}")
    scores_box.delete("1.0", tk.END)
    scores_box.insert(tk.END, str(scores))

root = tk.Tk(); root.title("Offline Sentiment Analyzer"); root.geometry("650x520")
tk.Label(root, text="Offline Sentiment Analyzer", font=("Arial", 18, "bold")).pack(pady=10)
tk.Label(root, text="Enter text:").pack(anchor="w", padx=15)
input_box = scrolledtext.ScrolledText(root, height=7, font=("Arial", 12)); input_box.pack(fill="both", expand=True, padx=15, pady=5)
tk.Button(root, text="Analyze Sentiment", command=analyze, font=("Arial", 12, "bold"), bg="#2563eb", fg="white").pack(pady=10)
result_var = tk.StringVar(); tk.Label(root, textvariable=result_var, font=("Arial", 14, "bold"), fg="#166534").pack(pady=5)
tk.Label(root, text="Sentiment Scores:").pack(anchor="w", padx=15)
scores_box = scrolledtext.ScrolledText(root, height=6, font=("Consolas", 11)); scores_box.pack(fill="both", expand=True, padx=15, pady=5)
root.mainloop()
