# project.Feeder
This repository contains a Flask web application that predicts the plant disease using a pre-trained Convolutional Neural Network (CNN) model. The trained model is integrated with the Flask web application to build an interactive user interface.

Project Structure
.
├── static
│   ├── css
│   └── js
├── templates
│   ├── base.html
│   └── index.html
├── app.py
├── best_model.h5
└── README.md

static: This directory contains the static assets of the Flask app (JavaScript and CSS).
templates: This directory contains the HTML files that define the structure of the web pages.
app.py: This file is the Flask app's main entry point that sets up the web server and implements the backend functionality for the app.
best_model.h5: This is the pre-trained Convolutional Neural Network (CNN) model that is used for the plant disease classification.
README.md: A Markdown file that provides useful information about the project.

Requirements
To run this project you need to have the following installed:
- Flask
- Keras
- TensorFlow
- Numpy

Usage
To run the Flask app, follow these steps:
1. Clone the repository: git clone https://github.com/your_username/machine-learning-plant-disease-detector
2. Navigate to the project directory: cd machine-learning-plant-disease-detector
3. Install the required packages: pip install -r requirements.txt
4. Run the Flask app: python app.py
5. Open your web browser and navigate to http://127.0.0.1:5000/.

Model Training
The Convolutional Neural Network (CNN) model used in this project was trained on the Plant Village dataset using the VGG19 architecture. The model achieved an accuracy of 95% on the validation set. The training process is not included in this repository.

Flask App Workflow
1. User uploads an image of the plant with a suspected disease
2. The image is sent to the Flask app using a POST request
3. The app processes the image using the pre-trained CNN model
4. The app returns the predicted disease with a brief description to the user.

License
This project is licensed under the MIT License - see the LICENSE file for details.
