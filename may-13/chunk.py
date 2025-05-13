import pdfplumber

def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def chunk_text(text, chunk_size=1000):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

def main():
    file_path = input("Enter the path to the PDF file: ")
    chunk_size = int(input("Enter the chunk size (default=1000): ") or 1000)

    try:
        text = extract_text_from_pdf(file_path)
        chunks = chunk_text(text, chunk_size)
        for i, chunk in enumerate(chunks):
            print(f"Chunk {i+1}: {chunk}")
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

