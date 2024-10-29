from langchain_community.llms import ollama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from server.models.recipe import Recipe

model = ollama.Ollama(
    model='mistral',
    base_url='http://192.168.1.144:11434'
)

parser = JsonOutputParser(pydantic_object=Recipe)

# Set up the prompt template
prompt = PromptTemplate(
    template="You are a master chef. Create a detailed recipe using the following ingredients and give the answers and follow the instructions no extras\n{format_instructions}\n ingredients: {ingredients}\n cuisine_type: {cuisine_type}\n",    
    input_variables=["ingredients", "cuisine_type"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)