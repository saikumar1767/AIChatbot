# AI-Powered Web Application Documentation

## Objective:

This project aims to develop a simple AI-powered web application using Python, Flask, and MySQL, enabling users to interact with a basic AI model. The Application features a user-friendly interface where users can input data and view responses generated by the AI model. Users can view their chat history. The code is well-structured, commented, and available in a GitHub repository.

## Implementation:

1. **Application Setup:**

   - Initialized a Flask web application.
   - I have set up a MySQL database to store user queries and AI responses.

2. **AI Integration:**

   - Integrated the Microsoft's DialoGPT-medium AI model into the Application.
   - Utilize pre-trained models from Hugging Face's AutoModelForCausalLM and AutoTokenizer classes(transformers) into the applicaiton.

3. **User Interface:**

   - Developed a simple and intuitive web interface allowing users to:
     - Input data to interact with the AI model.
     - View the AI model's responses.
     - Added Chat history section of the User.
   - Basic navigation and user feedback mechanisms were included.

4. **Database Interaction:**

   - Stored user inputs and AI responses in the MySQL database.
   - Implement functionality to retrieve past interactions from the database and display them on the website.

5. **Error Handling and Validation:**

   - Implemented error handling to manage and respond to potential failures or invalid inputs.
   - Validated user inputs to ensure they meet expected formats or criteria before processing.

6. **Documentation and Code Quality:**

   - Commented code adequately to explain critical sections and logic.
   - Included a README file in the GitHub repository with:
     - Instructions on how to set up and run the Application.
     - A brief description of the Application's functionality.

7. **GitHub Repository:**
   - Pushed code to a GitHub repository.
   - Ensured the repository is public and contains all necessary files to run the Application, excluding sensitive information like database credentials.

## Usage:

1. **Setup:**

   - Clone the repository to your local machine.

2. **Installation:**

   - Install Python and required dependencies using `pip install -r requirements.txt.`

3. **Database Setup:**

   - Set up a MySQL database and configure database credentials in the Flask application.
   - Create a database (for example: "mydatabase") using MySQL Command Line Client.

4. **Running the Application:**

   - Execute `python app.py` to start the Flask server.
   - Access the Application via the provided URL in your web browser.
   - The Application creates a table if it doesn't exist and inserts chats into it as the user interacts with the AI ChatBot.
   - On application render, the side-view bar has a chat history section feature that displays previous chat messages with ChatBot.

5. **Interacting wApplicatApplication:**
   - Input data in the provided interface to interact with the AI model.
   - View responses generated by the AI model and past interactions in the chat history section.
