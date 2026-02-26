# Simple Embedding-based Retrieval

This demo shows how to convert text to vector embeddings and find the document(s) most similar to a user query using cosine similarity.

## Run
1. Install dependencies (embedding model + numpy).
2. Compute and save document embeddings.
3. For each query, compute its embedding and compare with saved document embeddings.
4. Return the highest-scoring document(s).

## Example query

Input: "What is the capital of Germany?"
Output: "Berlin is Germany's capital, rich in history and culture."

