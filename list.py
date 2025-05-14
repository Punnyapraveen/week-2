import google.generativeai as genai

genai.configure(api_key="AIzaSyCp3OhyjXeoHg644fm6_O0ZZ2uf_RtGT1E")  # Replace with your actual key

models = genai.list_models()
for m in models:
    print(m.name, "supports generation:" if "generateContent" in m.supported_generation_methods else "")
