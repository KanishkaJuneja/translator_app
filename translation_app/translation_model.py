from transformers import MarianMTModel, MarianTokenizer

class TranslationApp:
    def __init__(self):
        self.tokenizer = MarianTokenizer.from_pretrained('Helsinki-NLP/opus-mt-en-es')
        self.model = MarianMTModel.from_pretrained('Helsinki-NLP/opus-mt-en-es')
    
    def translate_text(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        translated_tokens = self.model.generate(**inputs)
        translated_text = self.tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
        return translated_text

app = TranslationApp()

