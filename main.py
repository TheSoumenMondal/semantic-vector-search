from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as mp

load_dotenv()

# Creating a embedding
embadding = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

document = [
            "Paris is the capital of France, known for the Eiffel Tower and art museums.",
            "Tokyo is Japan's capital, famous for its technology and traditional temples.",
            "London is the capital of the United Kingdom with historic landmarks like Big Ben.",
            "Berlin is Germany's capital, rich in history and culture.",
            "Rome is Italy's capital, home to the Colosseum and Vatican City.",
            "Madrid is Spain's capital, known for its art galleries and vibrant nightlife.",
            "Beijing is China's capital, featuring the Great Wall and Forbidden City.",
            "Moscow is Russia's capital with iconic Red-Square and historical architecture.",
            "Sydney is Australia's capital region with the famous Opera House.",
            "Cairo is Egypt's capital, gateway to the ancient pyramids of Giza."
            ]

query = "What is the capital of Germany?"

# embadings
docuemnt_embadding = embadding.embed_documents(document)
query_embadding = embadding.embed_query(query)

# cosine similarity accepts the 2-D vectors as arguments
similarity_scores = cosine_similarity([query_embadding], docuemnt_embadding)

sorted_scores = sorted(list(enumerate(similarity_scores[0])) , key=lambda x: x[1] , reverse=True)
index , score = sorted_scores[0]

print(f"Most similar document: {document[index]} with a similarity score of {score}")