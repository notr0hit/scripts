from pikepdf import Pdf
import os

file_path = './python_async_notes.pdf'
file_name = os.path.splitext(os.path.basename(file_path))[0]

pdf = Pdf(file_path)
start = 3
end = 5

start -= 1 # make 0 based indexing
end -= 1

assert start >= 0 and end < len(pdf.pages)

res = Pdf.new()
for i in range(start, end):
    res.pages.append(pdf.pages[i])

res.save(f'{file_name}_{start+1}_{end+1}.pdf')
