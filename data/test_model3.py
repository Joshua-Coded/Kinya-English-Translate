from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Define the input and output languages
input_lang = "rw"
output_lang = "en"

# Define the input text
input_text = "ndabona iteka rya nyuma"

# Define the pre-trained models to try
model_names = [
    "Helsinki-NLP/opus-mt-rw-en", 
    "Helsinki-NLP/opus-mt-en-rw",
    "Helsinki-NLP/opus-mt-en-fr",
    "Helsinki-NLP/opus-mt-fr-en"
]

# Load the tokenizer and models and evaluate them on the input text
for model_name in model_names:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output_ids = model.generate(input_ids)
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    print(f"{model_name}:\n{input_lang}: {input_text}\n{output_lang}: {output_text}\n")
