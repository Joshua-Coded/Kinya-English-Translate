from transformers import TFMarianMTModel, MarianTokenizer

# Load the model
model_name = "Helsinki-NLP/opus-mt-rw-en"
model = TFMarianMTModel.from_pretrained(model_name)

# Load the tokenizer
tokenizer = MarianTokenizer.from_pretrained(model_name)

# Tokenize the input text
input_text = "Ndabona iteka rya nyuma"
input_ids = tokenizer.encode(input_text, return_tensors="tf")

# Generate the output text
output_ids = model.generate(input_ids)
output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

# Print the generated output text
print("Input text:", input_text)
print("Generated output text:", output_text)