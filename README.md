# Project Feeder()

## Description
Project Feeder() is a machine learning application built using Keras and Flask, that detects diseases in fruits and vegetables. It is capable of classifying 38 different types of diseases across 14 different crops. 

## Project Structure
```bash
├── static
│   ├── css
│   └── js
├── templates
│   ├── base.html
│   └── index.html
├── app.py
├── best_model.h5
└── README.md
```

## Installation
To use this application, please follow the steps below:

1. Clone the repository: `git clone https://github.com/username/project-feeder.git`
2. Install the required dependencies using `pip install -r requirements.txt`
3. Run the app: `python app.py`

## Usage
After following the installation steps, open the browser and go to http://127.0.0.1:5000/ to access the application's homepage. 

1. Click on the "Choose File" button to upload an image of a fruit or vegetable
2. Click on the "Submit" button to submit the form
3. Wait for a few seconds until the application processes the image and predicts the disease
4. The predicted disease along with a brief description of the disease will be displayed on the screen

## Dependencies
* numpy
* keras
* tensorflow
* flask

## Model
The application uses a pre-trained VGG19 model for image classification, which was trained on the PlantVillage dataset. The model was saved with Keras model.save() and can be found in the file `best_model.h5`.

## Credits
This application was built by [your name], inspired by the work of [Prakhar Mishra](https://github.com/prakhar21) and the PlantVillage research group.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
