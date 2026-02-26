# Simple Embedding-based Retrieval

<img width="2880" height="1800" alt="Image" src="https://github.com/user-attachments/assets/b6fcfca4-6144-43a5-b3a5-db96be9020d8" />

This demo shows how to convert text to vector embeddings and find the document(s) most similar to a user query using cosine similarity.

## Run
1. Install dependencies (embedding model + numpy).
2. Compute and save document embeddings.
3. For each query, compute its embedding and compare with saved document embeddings.
4. Return the highest-scoring document(s).

## Example query

Input: "What is the capital of Germany?"
Output: "Berlin is Germany's capital, rich in history and culture."

