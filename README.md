## FlipKart Product Recommendation Bot Using GEN AI

### Project Description
The FlipKart Product Recommendation Bot is an AI-driven chatbot designed to assist users in finding the best products based on their preferences and queries. Utilizing Retrieval-Augmented Generation (RAG) and the advanced LLM model "llama-3.1-70b-versatile," the bot analyzes user input to provide personalized product suggestions. With a user-friendly interface built on Flask, this chatbot enhances the online shopping experience by delivering relevant recommendations in real time.

### Features
* Interactive Chatbot: Engages users in natural language for product recommendations.
* Personalized Suggestions: Analyzes user preferences to provide tailored product options.
* Easy Deployment: Built using Flask, allowing for straightforward setup and usage.
* Responsive Design: User-friendly interface that adapts to various screen sizes.

### Screenshots
<img width="800" height="400" align="center" src="/screenshots/sample_image1.png">
<img width="800" height="400" align="center" src="/screenshots/sample_image2.png">
<img width="800" height="400" align="center" src="/screenshots/sample_image3.png">

### Technologies used in this project
* Python: Core programming language for development.
* Langchain: Framework for building AI applications.
* Astra DB: NoSQL database for storing product data.
* Jupyter Notebook: For data exploration and visualization.
* Flask: Web framework for building the web application.
* HTML/CSS: For frontend design.
* Git/GitHub: Version control and collaboration.
* Docker: Containerization for easy deployment.
* GitHub Actions: CI/CD for automated testing and deployment.
* AWS: Cloud services for hosting and scalability. 


### Installation and Setup
1. **Clone the Repository**:
    ```bash
    git clone FlipKart_Product_Recommendation_Bot_Using_GEN_AI.git
    cd FlipKart_Product_Recommendation_Bot_Using_GEN_AI
    ```

2. **Create a Virtual Environment**:
    ```bash
    conda create --name <env name> python=3.10 -y
    ```
3. **Activate the Virtual Enviroment**
    ```bash
    conda activate <env name>
    ```
4. **Install the Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Flask Application**:
    ```bash
    python app.py
    ```
    The application will be available at `http://127.0.0.1:8080/`.

### Usage
* To use the chatbot, navigate to the application URL and enter your product-related queries in the chat interface. The bot will respond with appropriate recommendations based on the provided input.

### Dataset
* The dataset consists of product names, reviews, and related information sourced from various online platforms. This data is used to train the recommendation model and improve the accuracy of suggestions.

### LLM Model
* The chatbot utilizes the "llama-3.1-70b-versatile" model for understanding and generating human-like responses based on user input.

### Future Work
* Enhance the recommendation algorithm to include user feedback.
* Expand the dataset to cover more product categories and details.
* Implement advanced analytics to track user interactions and improve recommendations over time.
### Contributing
* Contributions are welcome! If you have any suggestions or improvements, please raise an issue or submit a pull request.

### License
* This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

### Acknowledgments
* Special thanks to the open-source community for the libraries used in this project.