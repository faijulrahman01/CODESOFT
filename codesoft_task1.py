#CHATBOT WITH RULE-BASED RESPONSES
import tkinter as tk
from tkinter import scrolledtext
import re
from datetime import datetime

def get_response(user_input):
    user_input = user_input.lower()

    if re.search(r'\b(hi|hello|hey|hola)\b', user_input):
        return "Hello! How can I help you today?"

    elif re.search(r'\b(who are you|what are you|your name)\b', user_input):
        return "I'm a simple rule-based chatbot created to assist you."

    elif re.search(r'\b(time|date|day)\b', user_input):
        now = datetime.now()
        return f"The current date and time is: {now.strftime('%Y-%m-%d %H:%M:%S')}"

    elif re.search(r'\b(bye|exit|quit)\b', user_input):
        return "Goodbye! Have a great day!"

    elif re.search(r'\bhow are you\b', user_input):
        return "I'm just a program, but I'm functioning as expected. 😊"

    elif re.search(r'\b(help|what can you do)\b', user_input):
        return ("I can respond to greetings, tell you the BHtime, introduce myself, "
                "and answer simple questions. Try saying 'hello' or 'what's the time?'")

    else:
        return "I'm sorry, I don't understand that. Can you rephrase it?"

def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    chat_area.config(state='normal')
    chat_area.insert(tk.END, "You: " + user_input + "\n")
    entry.delete(0, tk.END)

    response = get_response(user_input)
    chat_area.insert(tk.END, "Bot: " + response + "\n\n")
    chat_area.config(state='disabled')
    chat_area.yview(tk.END)

    if "goodbye" in response.lower():
        window.after(2000, window.destroy)

window = tk.Tk()
window.title("Rule-Based Chatbot")

chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=20, font=("Arial", 12))
chat_area.pack(padx=10, pady=10)
chat_area.config(state='disabled')

entry = tk.Entry(window, width=50, font=("Arial", 12))
entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10), expand=True, fill=tk.BOTH)

send_button = tk.Button(window, text="Send", command=send_message, font=("Arial", 12))
send_button.pack(side=tk.RIGHT, padx=(0, 10), pady=(0, 10))
window.mainloop()