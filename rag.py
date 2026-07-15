
from langchain_community.document_loaders import PyPDFLoader 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_chroma import Chroma
from langchain_classic.chains import create_retrieval_chain 
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains.combine_documents import create_stuff_documents_chain


# loading the PDF document
file_path = "C:\\Users\\RAHUL\\Desktop\\PYTHON PROGRAMMING NOTES (1).pdf"  # Replace with your PDF file path 
loader = PyPDFLoader(file_path) 
document = loader.load() 
print("Document loaded successfully!")   

# splitting the document into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=30)
texts = text_splitter.split_documents(document) 
print(len(texts))
print("Document split into chunks successfully!") 

# embedding  
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2") 
print("Embeddings model loaded successfully!") 

# creating a vector store 
vector_store = Chroma.from_documents(documents=texts, embedding=embeddings)
print("Vector store created successfully!") 

# retrival 
retriever = vector_store.as_retriever(search_kwargs={"k": 3})
print("Retriever created successfully!") 

#llm 
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.3-70B-Instruct",
    task="conversational",
    provider="groq",
    huggingfacehub_api_token= "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",
    max_new_tokens=512)
chat_model = ChatHuggingFace(llm=llm) 
print("chat model create") 

#create a prompt  
prompt = ChatPromptTemplate.from_template(""" 
                you are a helpful assistant.
                use only the provided context to answer the question.
                context : 
                {context}
                                          
                 question:
                {input} """) 

#create document chain 
document_chain = create_stuff_documents_chain(chat_model , prompt)
retrieval_chain = create_retrieval_chain(retriever , document_chain)
print("create chain successful") 

# user ask question 
def ask_question(question):
     responce = retrieval_chain.invoke({"input" : question})
     return responce['answer']