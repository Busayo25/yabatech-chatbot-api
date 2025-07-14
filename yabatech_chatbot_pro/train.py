import json
import joblib
from sentence_transformers import SentenceTransformer

with open("intents.json", "r", encoding="utf-8") as f:
    data = json.load(f)

model = SentenceTransformer('all-MiniLM-L6-v2')
patterns, tags = [], []

for intent in data["intents"]:
    tag = intent["tag"]
    for lang in intent["patterns"]:
        for p in intent["patterns"][lang]:
            patterns.append(p)
            tags.append(f"{tag}|{lang}")

embeddings = model.encode(patterns)
joblib.dump(embeddings, "models/pattern_embeddings.pkl")
joblib.dump(tags, "models/tags.pkl")
print("Training complete.")