from haystack.nodes import EmbeddingRetriever, MarkdownConverter, PreProcessor, AnswerParser, PromptModel, PromptNode, PromptTemplate, TextConverter
from haystack.document_stores import WeaviateDocumentStore
# from haystack.preview.components.file_converters.pypdf import PyPDFToDocument
from haystack import Pipeline

print("Import Successfully")


path_doc = ['combined.txt']

# for dirpath, dirnames, filenames in os.walk("data"):
#     for filename in filenames:
#         if filename.endswith(".txt"):
#             path_doc.append(dirpath + '/' + filename)


document_store = WeaviateDocumentStore(host='http://localhost',
                                       port=8080,
                                       embedding_dim=384)

print("Document Store: ", document_store)
print("#####################")

converter = TextConverter()
print("Converter: ", converter)
print("#####################")

output = converter.convert(file_path=path_doc[0])
docs = []
docs.append(output[0])

# print(docs)
# print("Output: ", output)
# docs = output["documents"]
# print("Docs: ", docs)
# print("#####################")

final_doc = []
for doc in docs:
    # print(doc)
    new_doc = {
        'content': doc.content,
        'meta': doc.meta
    }
    final_doc.append(new_doc)
    print("#####################")

preprocessor = PreProcessor(
    clean_empty_lines=True,
    clean_whitespace=True,
    clean_header_footer=True,
    split_by="word",
    split_length=100,
    split_respect_sentence_boundary=True,
)
print("Preprocessor: ", preprocessor)
print("#####################")

preprocessed_docs = preprocessor.process(final_doc)
print("Preprocessed Docs: ", preprocessed_docs)
print("#####################")

document_store.write_documents(preprocessed_docs)


retriever = EmbeddingRetriever(
    document_store=document_store,
    embedding_model="sentence-transformers/all-MiniLM-L6-v2",
)

print("Retriever: ", retriever)

document_store.update_embeddings(retriever)

print("Embeddings Done.")
