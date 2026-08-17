from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import nltk 
from nltk.tokenize import sent_tokenize

# NLTK setup
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

# Load Model
model = SentenceTransformer("all-MiniLM-L6-v2")

def plagarism_check(text1, text2, threshold=0.75):
    try:
        sentence1 = sent_tokenize(text1)
        sentence2 = sent_tokenize(text2)
    except Exception:
        sentence1 = [s.strip() for s in text1.split('.') if s.strip()]
        sentence2 = [s.strip() for s in text2.split('.') if s.strip()]

    if not sentence1 or not sentence2:
        return 0.0, []

    # convert_to_numpy=True se VS Code ki red line hat jayegi
    embeddings1 = model.encode(sentence1, convert_to_numpy=True)
    embeddings2 = model.encode(sentence2, convert_to_numpy=True)

    similarity_matrix = cosine_similarity(embeddings1, embeddings2)

    match_sentences = []
    total_similarity = 0.0

    for i in range(len(sentence1)):
        max_similarity = float(max(similarity_matrix[i]))
        total_similarity += max_similarity

        if max_similarity >= threshold:
            best_match_idx = int(similarity_matrix[i].argmax())

            match_sentences.append({
                "Sentence 1": sentence1[i],
                "Sentence 2": sentence2[best_match_idx],
                "Similarity": round(max_similarity * 100, 2)
            })

    plagiarism_percent = (total_similarity / len(sentence1)) * 100

    return round(plagiarism_percent, 2), match_sentences