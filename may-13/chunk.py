def chunk_text(text, max_words=100):
    """
    Splits the input text into chunks, each containing up to `max_words` words.
    
    Parameters:
        text (str): The input text to be chunked.
        max_words (int): Maximum number of words per chunk.
        
    Returns:
        List[str]: A list of text chunks.
    """
    words = text.split()
    chunks = []
    
    for i in range(0, len(words), max_words):
        chunk = ' '.join(words[i:i + max_words])
        chunks.append(chunk)
    
    return chunks
