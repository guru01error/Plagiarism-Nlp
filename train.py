from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import nltk 
from nltk.tokenize import sent_tokenize

# NLTK data download check (safely handling pre-downloads)
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download("punkt_tab", quiet=True)

# Load SBERT Model (Pre-trained Semantic Transformer)
model = SentenceTransformer("all-MiniLM-L6-v2")

def plagarism_check(text1, text2, threshold=0.75):
    """
    Calculates semantic similarity between two texts using SBERT & Cosine Similarity.
    Returns overall plagiarism percentage and matched sentence pairs.
    """
    sentence1 = sent_tokenize(text1)
    sentence2 = sent_tokenize(text2)

    # Edge Case: Handle empty input strings
    if not sentence1 or not sentence2:
        return 0.0, []

    # Generate Dense Vector Embeddings
    embeddings1 = model.encode(sentence1, convert_to_tensor=False)
    embeddings2 = model.encode(sentence2, convert_to_tensor=False)

    # Calculate Cosine Similarity Matrix
    similarity_matrix = cosine_similarity(embeddings1, embeddings2)

    match_sentences = []
    total_similarity = 0.0

    for i in range(len(sentence1)):
        max_similarity = float(max(similarity_matrix[i]))
        total_similarity += max_similarity

        # Capture high-similarity matches above threshold
        if max_similarity >= threshold:
            best_match_idx = similarity_matrix[i].argmax()

            match_sentences.append({
                "Sentence 1": sentence1[i],
                "Sentence 2": sentence2[best_match_idx],
                "Similarity": round(max_similarity * 100, 2)
            })

    # Average similarity percentage across all sentences
    plagiarism_percent = (total_similarity / len(sentence1)) * 100

    return round(plagiarism_percent, 2), match_sentences