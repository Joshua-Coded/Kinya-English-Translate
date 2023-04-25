from google.cloud import translate_v2 as translate

def translate_text(text, target_language):
    """Translates a text string to the specified target language."""
    # Set up the Translation API client
    translate_client = translate.Client()

    # Translate the text
    result = translate_client.translate(text, target_language=target_language)

    # Return the translated text
    return result['translatedText']

if __name__ == '__main__':
    # Example usage
    text = 'Hello, world!'
    target_language = 'es'
    translated_text = translate_text(text, target_language)
    print(f'Translated text: {translated_text}')
