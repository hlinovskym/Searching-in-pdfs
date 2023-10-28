from PyPDF2 import PdfReader
import os
import pandas

PATH = "pdfs/"
texts = ["Words", "to", "find"]

files = os.listdir(PATH)
files_json = []
for file in files:
    files_json.append({"file": file})
files_df = pandas.DataFrame(files_json)
# print(files_json)
# print(files_df)

for text_to_find in texts:
    file_no = 0
    results = []

    for file in files:
        file_no += 1
        print(f"slovo: {text_to_find} - file {file_no}/{len(files)}: {file}")
        print("------------------------------------------------------------")
        result = {}
        stranky = []
        reader = PdfReader(f"{PATH}{file}")
        number_of_pages = len(reader.pages)

        for page_no in range(0, number_of_pages):
            page = reader.pages[page_no]
            text = page.extract_text()
            if text_to_find in text:
                stranky.append(page_no + 1)
        if len(stranky) > 0:
            result["file"] = file
            result[text_to_find] = stranky
        results.append(result)
        print(len(result))

    results_df = pandas.DataFrame(results)
    files_df = pandas.merge(files_df, results_df,  on=["file"],  how="left")
    # print(results_df)
    # print(files_df)

print(files_df.iloc[0:6, 0:4])
files_df.to_csv("results/results.csv")
# files_df.to_csv("results/results_utf-8.csv", encoding="utf-8")
