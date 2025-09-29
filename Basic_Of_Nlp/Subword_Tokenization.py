from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
text = "Hello, NLP with Hugging Face!"
tokens = tokenizer.tokenize(text)
print(tokens)
