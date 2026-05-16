from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('DocumentLoaders/AI_Overview_25_Pages.pdf')
docs = loader.load()

print('Type==', type(docs))
print('Length==', len(docs))
print('Content==', docs[0].page_content)
print('Metadata==', docs[0].metadata)