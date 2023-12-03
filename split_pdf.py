from pypdf import PdfReader

path = 'Lectures.pdf'

reader = PdfReader(path)

# page = reader.pages[0]
# text = page.extract_text()
# text = obj.extract_text()

# print(text)

len = len(reader.pages)

full_text = ''

for i in range(len):
    page = reader.pages[i]
    text = page.extract_text()
    full_text += str(i)
    full_text += '\n'
    full_text += text
    full_text += '\n---------------------------------------------------\n'

# Specify the file path
file_path = "psychology_lectures.txt"

# Open the file in write mode
with open(file_path, "w") as file:
    # Write the text content to the file
    file.write(full_text)

# print(full_text)

