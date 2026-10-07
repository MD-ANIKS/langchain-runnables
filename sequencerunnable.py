from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#prompt template 
prompt = ChatPromptTemplate.from_template(
  "Explain {topic} in simple words"
)

#model 
model = ChatMistralAI(model="labs-leanstral-1-5")

# output parser
parser = StrOutputParser()

# ssequence runnable 
chain = prompt | model | parser

result = chain.invoke("Gen AI")

print(result)