from flask import Flask, render_template, request, jsonify
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
openai.api_key = "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"


@app.route("/get-recipe", methods=["POST"])
def get_recipe():
    try:
        # Get user input from the request
        user_input = request.json.get("user_input")
        if not user_input:
            return jsonify({"error": "No input provided"}), 400

        # Call the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that provides recipes."},
                {"role": "user", "content": user_input}
            ]
        )

        # Extract the response text
        recipe = response.choices[0].message["content"]

        # Return the recipe as a JSON response
        return jsonify({"recipe": recipe})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
