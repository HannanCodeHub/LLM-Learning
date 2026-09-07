import numpy as np
from google import genai

client = genai.Client()

documents = [
    "Refund requests are allowed within 7 days",
    "Python classes happen Monday to Friday",
    "Students get 4 interview opportunities",
    "Course access is available for 6 months"
]

question = "how many interview opportunities can i have?"

# Document embeddings
document_vectors = []

for document in documents:
    result = client.models.embed_content(
        model="gemini-embedding-2",
        contents=document
    )

    document_vectors.append(result.embeddings[0].values)

# Question embedding
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

# Retrieve the most relevant chunk
scores = []

for document, vector in zip(documents, document_vectors):
    score = cosine_similarity(question_vector, vector)
    scores.append(score)

best_index = np.argmax(scores)
best_doc = documents[best_index]

print("Retrieved chunk:", best_doc)

# Generate answer from retrieved context
prompt = f"""
Answer the question using only the information in the context.

Context:
{best_doc}

Question:
{question}

If the context contains enough information to answer the question, answer it directly.
Do not use outside knowledge.

If the answer cannot be determined from the context, say:
"I don't know based on the provided context."
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

print("\nAnswer:")
print(response.text)
