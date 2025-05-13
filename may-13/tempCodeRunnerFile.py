api_key = 'AIzaSyCp3OhyjXeoHg644fm6_O0ZZ2uf_RtGT1E'
import google.generativeai as genai

# Correct configuration
genai.configure(api_key=api_key)

# Load the model
model = genai.GenerativeModel("gemini-1.5-flash")

# 1. Text generation
def generate_text(prompt):
    response = model.generate_content(prompt)
    return response.text

# 2. Text summarization
def text_summarization(text):
    response = model.generate_content(f'Summarize this: {text}')
    return response.text

# 3. Question answering
def question_answering(context, question):
    response = model.generate_content(f'Question: {question}\nContext: {context}')
    return response.text

# 4. Sentiment analysis
def sentiment_analysis(text):
    response = model.generate_content(f'Analyze the sentiment of this text: {text}')
    return response.text

# 5. Text translation
def text_translation(text, target_language):
    response = model.generate_content(f'Translate this text to {target_language}: {text}')
    return response.text

# Example calls
prompt = "The quick brown fox"
print("Generated Text:", generate_text(prompt))

text = "The quick brown fox jumps over the lazy dog"
print("Summary:", text_summarization(text))

context = "The quick brown fox jumps over the lazy dog"
question = "What does the fox jump over?"
print("Answer:", question_answering(context, question))

print("Sentiment:", sentiment_analysis(text))

target_language = "es"
print("Translation:", text_translation(text, target_language))
