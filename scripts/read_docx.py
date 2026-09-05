import os
import zipfile
import xml.etree.ElementTree as ET

def extract_text_from_docx(docx_path):
    try:
        with zipfile.ZipFile(docx_path) as docx:
            xml_content = docx.read('word/document.xml')
            tree = ET.XML(xml_content)
            
            # The XML namespace for Word
            WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
            PARA = WORD_NAMESPACE + 'p'
            TEXT = WORD_NAMESPACE + 't'
            
            paragraphs = []
            for paragraph in tree.iter(PARA):
                texts = [node.text for node in paragraph.iter(TEXT) if node.text]
                if texts:
                    paragraphs.append(''.join(texts))
            
            return '\n'.join(paragraphs)
    except Exception as e:
        return f"Error reading {docx_path}: {e}"

folder = 'EVENTS'
with open('events_info.md', 'w', encoding='utf-8') as out:
    for filename in os.listdir(folder):
        if filename.endswith('.docx'):
            path = os.path.join(folder, filename)
            out.write(f"# {filename}\n")
            out.write(extract_text_from_docx(path))
            out.write("\n\n")
print("Extraction complete.")
