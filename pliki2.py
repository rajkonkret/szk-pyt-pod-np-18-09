import chardet  # mozna z ajej pomoca wykryc typ kodowania znaków w pliku

# pip install chardet

file_path = 'test.log'

with open(file_path, 'rb') as file:
    raw_data = file.read()

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'Windows-1254', 'confidence': 0.6843959022560266, 'language': 'Turkish'}
kodowanie = result['encoding']
# dla większej próbki:
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
confidence = result['confidence']
print(kodowanie, confidence)  # utf-8 0.99

print(raw_data.decode(encoding=kodowanie))
