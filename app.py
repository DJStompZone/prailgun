import os

from flask import Flask, render_template, request, jsonify
import dotenv
from openai import OpenAI

dotenv.load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)


@app.route("/")
def index():
    """
    Route for the index page.

    This function handles the root URL ('/') of the application and renders the 'index.html' template.

    Returns:
        Response: The rendered 'index.html' template.
    """
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    """
    Generates a professional media inquiry email based on client-provided details.
    This function retrieves client details from an HTTP request, constructs prompts for an AI model,
    and generates a media inquiry email. The generated email is then returned as a JSON response.
    Returns:
        JSON: A JSON object containing the generated email or an error message.
    Raises:
        Exception: If there is an error during the email generation process, an error message is returned
                   with a 500 status code.
    """
    client_name = request.form.get('client_name')
    dba = request.form.get('dba')
    industry = request.form.get('industry')
    custom_instructions = request.form.get('custom_instructions')

    system_prompt = {
        "role": "system",
        "content": "You are an expert public relations specialist. Your task is to craft a professional media inquiry email based on the details provided by the client below. Include a clear introduction, a concise request or purpose, and a polite closing."
    }

    user_prompt = {
        "role": "user",
        "content": f"""
        Client Details:
        Name: {client_name}
        DBA: {dba}
        Industry: {industry}
        
        Custom Instructions:
        {custom_instructions}
        """
    }

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[system_prompt, user_prompt],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        generated_email = response.choices[0].message.content.strip()

        return jsonify({"email": generated_email})
     # pylint: disable=broad-exception-caught
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
