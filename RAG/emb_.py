import numpy as np
from google import genai

client = genai.Client()

documents = [
    "Refund requests are allowed within 7 days",
    "Python classes happen Monday to Friday",
    "Students get 4 interview opportunities"
]

question = "Can I get my money back after 5 days?"

document_vectors = []

# Create embeddings for each document
for document in documents:
    result = client.models.embed_content(
        model="gemini-embedding-2",
        contents=document
    )

    vector = result.embeddings[0].values
    document_vectors.append(vector)


# Create embedding for the question
question_result = client.models.embed_content(
    model="gemini-embedding-2",
    contents=question
)

question_vector = question_result.embeddings[0].values


# Cosine similarity
def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (
        np.linalg.norm(a) * np.linalg.norm(b)
    )


# Compare question with every document
for document, vector in zip(documents, document_vectors):

    score = cosine_similarity(
        question_vector,
        vector
    )

    print(round(score, 3), document)