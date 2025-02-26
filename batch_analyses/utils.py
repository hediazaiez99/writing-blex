from difflib import HtmlDiff

def merge_documents(doc1_path, doc2_path):
    with open(doc1_path, 'r') as file1, open(doc2_path, 'r') as file2:
        doc1_lines = file1.readlines()
        doc2_lines = file2.readlines()

    differ = HtmlDiff()
    merged_doc = differ.make_table(doc1_lines, doc2_lines, fromdesc='Document 1', todesc='Document 2')

    return merged_doc