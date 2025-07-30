import streamlit as st
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

### Basic AI Agent with WEB UI
llm = OllamaLLM(model="tinyllama") 

#Initialize memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = ChatMessageHistory()

#Define AIT chat prompt
prompt = PromptTemplate(
    input_variables=["chat_history","question"],
    template="Previous conversation: {chat_history}\nUser: {question}\nAI:"
)

#Function to run AI chat with memory
def run_chain(question):
    #Retrieve chat history manually
    chat_history_text= "\n".join([f"{msg.type.capitalize()}: {msg.content}" for msg in st.session_state.chat_history.messages])

    #Run the AI response generation
    response = llm.invoke(prompt.format(chat_history=chat_history_text,question=question))


#Store new user input and AI response in memory
    st.session_state.chat_history.add_user_message(question)
    st.session_state.chat_history.add_ai_message(response)

    return response

#Streamlit UI

st.title("AI CHATBOT WITH MEMORY")
st.write("ASK ME ANYTHING")

user_input = st.text_input("Your Question: ")
if user_input:
    response = run_chain(user_input)
    st.write(f"**You**{user_input}")
    st.write(f"**AI** {response}")

#Show full chat history
st.subheader("Chat history")
for msg in st.session_state.chat_history.messages:
    st.write(f"**{msg.type.capitalize()}**: {msg.content}")
    

        
  











# #Basic AI Agent with memory

# import streamlit as st
# from langchain_community.chat_message_histories import ChatMessageHistory
# from langchain_core.prompts import PromptTemplate
# from langchain_ollama import OllamaLLM

# #Load AI Model
# llm = OllamaLLM(model="tinyllama") 

# #Initialize Memory
# chat_history = ChatMessageHistory() #Stores user-AI conversation history

# #Define AIT chat prompt
# prompt = PromptTemplate(
#     input_variables=["chat_history","question"],
#     template="Previous conversation: {chat_history}\nUser: {question}\nAI:"
# )

# #Function to run AI chat with memory
# def run_chain(question):
#     #Retrieve chat history manually
#     chat_history_text= "\n".join([f"{msg.type.capitalize()}: {msg.content}" for msg in chat_history.messages])

#     #Run the AI response generation
#     response = llm.invoke(prompt.format(chat_history=chat_history_text,question=question))

#     #Store new user input and AI response in memory
#     chat_history.add_user_message(question)
#     chat_history.add_ai_message(response)

# #Interactive CLI Chatbot
# print("\n AI chatbot with memory")
# print("Type 'exit' to stop.")

# while True:
#     user_input = input("\ You:")
#     if user_input.lower() =="exit":
#         print("\n Goodbye!")
#         break
#     ai_response =run_chain(user_input)
#     print(f"\AI: {ai_response}")




#             #Basic AI Agent
# # #Load AI model from Ollama
# # llm= OllamaLLM(model="tinyllama")
# # print("\n Welcome to your AI Agent! Ask me anything.")
# # while True:
# #     question= input("Your Question (or type 'exit' to stop): ")
# #     if question.lower() == 'exit':
# #         print("Goodbye!")
# #         break
# #     response = llm.invoke(question)
# #     print("\n AI Response: ", response)
