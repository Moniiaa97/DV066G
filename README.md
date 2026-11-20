# Ollama LLM Comparison #
### DV066G AI - Assignment 1 group 5 ###

## Description ##
In this project, we use Ollama to run and compare two different language models locally. The objective is to examine how
the models respond to the same question and to compare their speed. The results are saved to a CSV file.
## Models used ##
ollama gemma3:1b
ollama  llama3.2:1b
## How to run the code ##
1. Install Ollama from https://ollama.com. 
2. Download the models by running the following commands in the terminal:
* ollama pull gemma3:1b
* ollama pull llama3.2:1b
3. Install the Python library:
* pip install ollama
4. Run the Python program:
* Python main.py
5. Open results.csv in the project folder to read the saved output. It contains one row per model with the model name 
and its response. The file is overwritten each time the program runs.

## Observations ##
* The two models may provide different answers, even when presented with the same question.
* Speed: Smaller models generally require fewer resources and can therefore respond more quickly.
To measure the speed, 6_elapsedtime.py from the provided tutoriaLLM repository (not included in this repo) was run 
several times with the prompt “Hello!”. Both models averaged roughly 1.5 to 2 seconds per response with no timeouts. 
The differences between them were smaller than the variation between runs, so it is not possible to conclude that one 
was faster than the other.
* Comparison: Larger commercial language models, such as ChatGPT, can often provide more detailed and accurate answers, 
especially to more complex questions.
* The two models were presented with the same prompt, “What is the capital of Sweden?”, and both answered correctly, 
though there were some noticeable differences in their style of answers. Each model was run several times, but no exact 
count was recorded. gemma3:1b always included an emoji and markdown formatting, but the content after the answer differed 
between runs: it ended with either follow-up questions or an added descriptive sentence. Whereas gemma3:1b’s answers 
were more engagement-oriented and in an informal register, llama3.2:1b’s were minimal and plain-text, with no emojis and
no markdown formatting. llama3.2:1b consistently returned the correct answer as a single plain sentence.

A practical consequence of the formatting difference is that when saving the models’ outputs to the CSV file, it at first
broke because of the use of emojis by gemma3:1b. This was fixed by setting the file encoding to UTF-8.




