from flask import Flask, render_template, request, jsonify
import mysql.connector
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

app = Flask(__name__)


# MySQL Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydatabase"
)

# Create a cursor object to execute queries
cursor = db.cursor()

# Create a table to store user interactions if not exists
cursor.execute("""CREATE TABLE IF NOT EXISTS interactions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_input TEXT,
                ai_response TEXT
                )""")

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]
    bot_response = get_chat_response(msg)
    save_interaction(msg, bot_response)
    return bot_response


def get_chat_response(text):
    # Let's chat for 5 lines
    for step in range(100):
        # encode the new user input, add the eos_token and return a tensor in Pytorch
        new_user_input_ids = tokenizer.encode(str(text) + tokenizer.eos_token, return_tensors='pt')

        # append the new user input tokens to the chat history
        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

        # generated a response while limiting the total chat history to 3000 tokens, 
        chat_history_ids = model.generate(bot_input_ids, max_length=3000, pad_token_id=tokenizer.eos_token_id)

        # Decode and return the response and pretty print last ouput tokens from bot
        return tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

def save_interaction(user_input, ai_response):
    cursor.execute("INSERT INTO interactions (user_input, ai_response) VALUES (%s, %s)", (user_input, ai_response))
    db.commit()

if __name__ == '__main__':
    app.run(debug=True)
