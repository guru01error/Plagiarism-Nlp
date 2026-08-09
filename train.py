from flask import Flask, render_template, request
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import nltk 
from nltk.tokenize import sent_tokenize
nltk.download("punkt_tab")
model = SentenceTransformer("all-MiniLM-L6-v2")

def plagarism_check(text1, text2):

    sentence1 = sent_tokenize(text1)
    sentence2 = sent_tokenize(text2)

    if len(sentence1) == 0 or len(sentence2) == 0:
        return 0, []

    embeddings1 = model.encode(sentence1)
    embeddings2 = model.encode(sentence2)

    similarity_matrix = cosine_similarity(embeddings1, embeddings2)

    match_sentences = []
    total = 0

    for i in range(len(sentence1)):

        max_similarity = max(similarity_matrix[i])
        total += max_similarity

        if max_similarity > 0.75:

            index = similarity_matrix[i].argmax()

            match_sentences.append({
                "Sentence 1": sentence1[i],
                "Sentence 2": sentence2[index],
                "Similarity": round(max_similarity * 100, 2)
            })

    plagiarism_percent = (total / len(sentence1)) * 100

    return round(plagiarism_percent, 2), match_sentences