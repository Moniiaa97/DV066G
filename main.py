import ollama
import LLMcalls

models = ["gemma3:1b", "llama3.2:1b"]
LLMcalls.add_to_csv("results.csv", ["Model", "Response"], new=True)
prompt = "What is the capital of Sweden?"

for model in models:
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    print(response['message']['content'])

    LLMcalls.add_to_csv("results.csv", [model, response['message']['content']])


