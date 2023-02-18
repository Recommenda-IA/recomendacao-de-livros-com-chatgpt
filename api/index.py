import os
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        book = request.form["book"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(book),
            temperature=0.5,
            max_tokens=600,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")

    return render_template("index.html", result=result)


def generate_prompt(book):
    return """10 livros recomendados para quem leu {} e lojas para comprar:""".format(book.capitalize()
                                                                                      )


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050, debug=True)
