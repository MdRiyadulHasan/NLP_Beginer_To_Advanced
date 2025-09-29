from transformers import AutoTokenizer

# Load a pretrained BERT tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = "Tokenization is essential for NLP."

# Tokenize into subwords
tokens = tokenizer.tokenize(text)
token_ids = tokenizer.convert_tokens_to_ids(tokens)

print("Subword Tokens:", tokens)
print("Token IDs:", token_ids)
