# Import Dependencies
from flask import Flask, render_template, request
from flipkart_ecom.retrieval_generation import generation
from flipkart_ecom.data_ingestion import data_ingestion

# Initialize Data Ingestion and Retrieval Generation
vstore = data_ingestion("done")
chain = generation(vstore)

# Initialize Flask Application
app = Flask(__name__)


# Home Page
@app.route("/")
def index():
    return render_template("index.html")

# Chat Route
@app.route("/get", methods = ["POST", "GET"])
def chat():
   if request.method == "POST":
      msg = request.form["msg"]
      input = msg

      result = chain.invoke(
         {"input": input},
    config={
        "configurable": {"session_id": "dhruv"}
    },
)["answer"]

      return str(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=False)