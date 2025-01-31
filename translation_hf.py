from transformers import MarianMTModel, MarianTokenizer

def translate_text(text, source_lang="en", target_lang="fr"):
    """
    Translates text from source language to target language using Hugging Face MarianMT.
    """
    # Load pre-trained model and tokenizer
    model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # Tokenize input text
    tokenized_text = tokenizer.prepare_seq2seq_batch([text], return_tensors="pt")

    # Perform translation
    translated_tokens = model.generate(**tokenized_text)
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

    return translated_text

def main():
    print("Welcome to the Language Translation System!")
    text = input("Enter the text to translate: ")
    source_lang = input("Enter the source language code (e.g., 'en' for English): ")
    target_lang = input("Enter the target language code (e.g., 'fr' for French): ")

    translated_text = translate_text(text, source_lang, target_lang)
    print(f"\nTranslated Text: {translated_text}")

if __name__ == "__main__":
    main()