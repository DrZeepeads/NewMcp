import os
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_textbook_data(filepath: str) -> str:
    """
    Reads the content of the file at filepath.
    Includes basic error handling for file not found.
    """
    logging.info(f"Attempting to load data from: {filepath}")
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        logging.info(f"Successfully loaded data from: {filepath}")
        return content
    except FileNotFoundError:
        logging.error(f"Error: File not found at {filepath}")
        # In a real script, you might raise the error or handle it differently
        return "" # Return empty string or raise an exception
    except Exception as e:
        logging.error(f"An unexpected error occurred while loading {filepath}: {e}")
        return ""

def chunk_text(text: str) -> List[Dict]:
    """
    Placeholder function to chunk text.
    Returns a list of dictionaries, where each dictionary represents a chunk.
    """
    logging.info("Chunking text... (placeholder)")
    if not text:
        logging.warning("Input text for chunking is empty.")
        return []
    # Placeholder implementation
    return [
        {"id": "chunk1", "text": "This is the first placeholder chunk from the textbook.", "metadata": {"page": 1, "source": "Nelson Textbook"}},
        {"id": "chunk2", "text": "This is the second placeholder chunk, discussing another topic.", "metadata": {"page": 2, "source": "Nelson Textbook"}},
        {"id": "chunk3", "text": "A third chunk to demonstrate the process.", "metadata": {"page": 3, "source": "Nelson Textbook"}},
    ]

def embed_chunks(chunks: List[Dict]) -> List[Dict]:
    """
    Placeholder function to embed chunks.
    Adds a placeholder 'embedding' key to each chunk dictionary.
    """
    logging.info("Embedding chunks... (placeholder)")
    if not chunks:
        logging.warning("No chunks provided for embedding.")
        return []
    for i, chunk in enumerate(chunks):
        # Placeholder embedding - in reality, this would be a dense vector
        chunk['embedding'] = [0.1 + i*0.01, 0.2 + i*0.01, 0.3 + i*0.01] 
    logging.info(f"Successfully added placeholder embeddings to {len(chunks)} chunks.")
    return chunks

def store_chunks_in_vector_db(chunks: List[Dict]):
    """
    Placeholder function to store chunks in a vector DB.
    Logs the number of chunks it would store.
    """
    logging.info("Storing chunks in vector DB... (placeholder)")
    if not chunks:
        logging.warning("No chunks provided for storage.")
        return
    logging.info(f"Would store {len(chunks)} chunks in the vector database.")
    # Placeholder: print details of the first chunk to simulate storage
    if chunks:
        logging.info(f"Example chunk to be stored: {chunks[0]}")

if __name__ == "__main__":
    logging.info("Starting data preprocessing script...")

    # Define a placeholder filepath
    # In a real scenario, this path would point to the actual textbook data.
    # For this script, we'll simulate it.
    # To make this runnable without an actual file, load_textbook_data will return "" if not found,
    # and chunk_text will handle empty input.
    placeholder_filepath = "data/raw/nelson_textbook.txt" 

    # Create dummy file for load_textbook_data to read for now
    # This is just to make the script runnable as per instructions
    # In a real scenario, the file would exist.
    os.makedirs(os.path.dirname(placeholder_filepath), exist_ok=True)
    with open(placeholder_filepath, 'w') as f:
        f.write("This is a dummy line from the Nelson textbook for testing purposes.\n")
        f.write("Another line to ensure there is some content to chunk.\n")

    textbook_content = load_textbook_data(placeholder_filepath)

    if textbook_content:
        chunked_data = chunk_text(textbook_content)
        embedded_data = embed_chunks(chunked_data)
        store_chunks_in_vector_db(embedded_data)
        logging.info("Data preprocessing script finished successfully (using placeholder functions).")
    else:
        logging.warning("Textbook content was empty. Skipping chunking, embedding, and storing.")
        logging.info("Data preprocessing script finished with warnings (input file might be missing or empty).")

    # Clean up the dummy file
    if os.path.exists(placeholder_filepath):
        os.remove(placeholder_filepath)
        # Try to remove the directory if it's empty
        try:
            os.rmdir(os.path.dirname(placeholder_filepath))
        except OSError:
            pass # Directory not empty, which is fine.
    
    logging.info("Script execution complete.")
