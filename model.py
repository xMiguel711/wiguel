from transformers import pipeline

# Usamos un modelo de texto open-source (puedes cambiar a Mistral, GPT-J, etc.)
generator = pipeline("text-generation", model="gpt2")

def generate_response(prompt):
    try:
        result = generator(prompt, max_length=150, do_sample=True, temperature=0.7)
        return result[0]["generated_text"]
    except Exception as e:
        return "Lo siento, no pude generar respuesta."
