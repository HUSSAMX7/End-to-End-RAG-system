from langchain.embeddings import OpenAIEmbeddings
from sentence_transformers import SentenceTransformer
import re
from langchain_community.vectorstores import Chroma


from utils import call_llm


from langchain_core.messages import HumanMessage, AIMessage

from langchain_core.prompts import ChatMessagePromptTemplate, MessagesPlaceholder
from langchain.embeddings import HuggingFaceEmbeddings
from docx import Document

__import__('pysqlite3')

import sys

sys.modules['sqlite3'] = sys.modules['pysqlite3']


class LLamaModel:

    def __init__(self):
        self.vectorstore_ar = self.get_ar_vectorstore()
        self.vectorstore_en = self.get_en_vectorstore()
        self.conversation_history = []



def custom_arabic_text_spliter_by_heading1(self, docx_path: str):
    doc = Document(docx_path)
    sections = []
    current_section = ""

    for para in doc.paragraphs:
        if para.style.name == 'Heading 1':
            if current_section:
                sections.append(current_section)
                current_section = ""
            current_section += para.text + "\n"
        else:
            current_section += para.text + "\n"

    if current_section:
        sections.append(current_section)
        
    return sections


def get_arabic_vector_store(self):

    embeddings = OllamaEmbeddings(model="UBC-NLP/ARBERT")
    vectorstore_ar = Chroma(parsist_direction="ar", embedding_function = embeddings)
        
    return vectorstore_ar
   
def get_english_vector_store(self):

    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore_en = Chroma(parsist_direction="en", embedding_function = embeddings)
        
    return vectorstore_en



def ollama_llm(self, question, context, language):
    if language == "ar":
        system_message = (
        "تصرف كخبير مختص في الموضوع، أجب عن السؤال المطروح باللغة العربية الفصحى فقط. "
        "إذا لم تجد إجابة ضمن المعلومات المقدمة، أخبر المستخدم بوضوح أنه لا تتوفر معلومات كافية. "
        "استخدم لغة واضحة وبسيطة دون إدخال أي كلمات أجنبية. "
        "التزم بالرد بناءً على المعلومات المقدمة فقط دون إضافة معلومات من خارج السياق. "
        "حافظ على نبرة رسمية مهذبة ومباشرة."
        )

        prompt = f"""
        السؤال: {question}

        {f"السياق:\n{context}" if context else ""}
        """
    else:
        system_message = (
        "Act as an expert in the subject. Answer the user's question strictly in English only. "
        "If no answer is found within the provided context, clearly inform the user that there is insufficient information. "
        "Use clear and simple English language without inserting any foreign words. "
        "Respond only based on the provided context without adding any external information. "
        "Maintain a formal, polite, and direct tone in all responses."
        )

        prompt = f"""Question: {question}

        {f"Context:\n{context}" if context else ""}
        """

    prompt_template = ChatMessagePromptTemplate.format_messages(
        [
            ("system", system_message),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human","{input}")
        ]
    )

    final_prompt = prompt_template.format(input=prompt, chat_history= self.conversation_history)

    response = call_llm(final_prompt)

    self.conversation_history.append(HumanMessage(content=question))
    self.conversation_history.append(AIMessage(content=response))

    return response


def determine_language(self,text):
    
    if re.search(r'[\u0600-\u06FF]' , text):
        return "ar"
    elif re.search(r'a-zA-Z', text):
        return "en"
    else:
        return None
    
def get_retriever(self, question):
    
    language = self.determine_language(question)
    if language == "ar":
        return self.vectorstore_ar.as_retriver(search_kwargs={"k":3})
    else:
        return self.vectorstore_en.as_retriver(search_kwargs={"k":3})
    

def rag_chain(self, question):
    
    language = self.determine_language(question)
    retrived_docs = self.get_retriever(question).invoke(question)
    formatted_context = "".join(doc.page_content.replace("\n", " ") for doc in retrived_docs)

    return self.ollama_llma(question, formatted_context, language)

def get_important_facts(self, qestion):
    response = self.rag_chain(qestion)

    if not response.strip() or response == "":

        return ""
    return response 

