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

## Assignment 2: Testing ask_capital ##

### Description ###
In this project, Ollama is used to run `ask_capital` and test it with five tests with assertions, including tests that 
use an LLM-as-a-judge. A sixth test has no assertion and only prints the judge's verdict for this README.  

### Purpose ###
The purpose of this assignment is to test how reliable and consistent an AI model is. `gemma3:1b` was tested with Python 
unittest and an LLM-as-a-judge. The minimum threshold is 2 out of 3 correct answers per consistency test, and the 
expected pass rate is 3 out of 3, since the question is simple. Two countries were chosen: Sweden and Kazakhstan. An 
answer is counted correct if it contains the name of the capital.

### How to run the code ###
1. Install Ollama from https://ollama.com
2. Download the model:
* ollama pull gemma3:1b
3. Install the python libraries:
* pip install ollama pillow
4. Run the tests, either from the terminal:
* python -m unittest llm_as_judge -v  
* or in PyCharm by pressing the green play button next to `class TestApp` in  `llm_as_judge.py` (runs all tests) or next 
to a single test (runs only that test).
5. Analyze the results

### Observations ###
All five tests with assertions passed (a 100% pass rate). However, the model gave contradictory answers about Kazakhstan, 
and the consistency test still passed (a false positive). This shows that checking only whether the capital name is 
included is not enough, since the rest of the answer can be wrong.  

To answer whether the mistake came from the model or the judge, an extra test was added. It gives the judge a shortened 
and slightly reworded version of the model's own contradictory answer, and the judge answered NO in all 3 runs, so it 
spotted the error. The fault was therefore not in the judge: the model hallucinated, and the keyword check in the test 
was too lenient. Still, an LLM-as-a-judge can also make mistakes and incorrectly accept or reject answers, so it should 
not be the only method used to evaluate AI systems. Stricter tests are needed to check that the whole answer is correct. 

Consistency test for Kazakhstan: 

```python
def test_knows_capital_of_kazakhstan(self):
    correct = 0
    for i in range(3):
        answer = ask_capital("Kazakhstan")
        print(f"Kazakhstan run {i+1}: {answer}")
        if "Astana" in answer:
            correct += 1
    self.assertGreaterEqual(correct, 2)
```

Model output (run 1 contradicts itself, run 2 invents the name "Nur-Suu", run 3 uses the outdated name "Nur-Sultan"): 

```
Kazakhstan run 1: The capital of Kazakhstan is ** Astana**.
It's a planned city located in the north of the country.
While it's a significant urban center, it's important to note that Astana is a planned city, and it's not the capital city itself. The official capital remains Almaty.

Kazakhstan run 2: The capital of Kazakhstan is **Astana**, also known as Nur-Suu.
It's a modern, planned city.

Kazakhstan run 3: The capital of Kazakhstan is **Astana**, also known as Nur-Sultan. 😊
```

Judge test with a shortened and slightly reworded version of the model's answer:

```python
def test_judge_on_self_contradicting_answer(self):
    answer = ("The capital of Kazakhstan is Astana. However, Astana is not the "
              "capital city itself. The official capital remains Almaty.")
    verdict = llm_as_a_judge_agrees("Kazakhstan", answer, "Astana")
    print(f"Judge on contradicting answer: {verdict}")
```

```
Judge (Kazakhstan, expected Astana): NO
Judge on contradicting answer: False
```