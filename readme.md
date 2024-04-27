# Pregnancy test using smart phone camera
This project is a pregnancy test with quantitative estimation using a smart phone camera. The project is based on the paper "A smartphone-based rapid quantitative detection platform for lateral flow strip of human chorionic gonadotropin with optimized image algorithm" by Zhang et al. (2020). The paper describes a method to detect the hormone hCG in urine using a smartphone camera. The method is based on the lateral flow immunoassay (LFA) technique, which is commonly used in pregnancy tests. The method uses a smartphone camera to capture an image of the LFA strip and then analyzes the image to estimate the concentration of hCG in the urine sample.

The project is implemented in Flask and python using the OpenCV library for image processing and the NumPy library for numerical calculations. 

## Installation
To run the project, you need to have Python installed on your computer. You can download Python from the official website: https://www.python.org/.
Start by cloning the repository to your computer:
```bash
git clone https://github.com/jitinchekka/sensors-in-healthcare-project.git
```
Then navigate to the project directory:
```bash
cd sensors-in-healthcare-project
```
Install the required Python packages using pip:
```bash
pip install -r requirements.txt
```
Run the Flask application:
```bash
flask run
```
Open a web browser and go to http://127.0.0.1:5000/ to access the application.

## Usage
To use the application, follow these steps:
1. Take a picture of the LFA strip using your smartphone camera.
2. Upload the image to the application.
3. Click the "Analyze" button to process the image and estimate the hCG concentration.
4. View the estimated hCG concentration on the results page.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
This project was inspired by the paper "A smartphone-based rapid quantitative detection platform for lateral flow strip of human chorionic gonadotropin with optimized image algorithm" by Zhang et al. (2020). The authors of the paper developed a method to detect hCG in urine using a smartphone camera and inspired this project.

## Author
- Jitin Chekka
Contact me at [Email](mailto:jitinchekka2@gmail.com?subject=[GitHub]%20Source%20SIH%20Project)
[![Linkedin](https://i.stack.imgur.com/gVE0j.png) LinkedIn](https://www.linkedin.com/in/jitin-krishna-chekka/)
&nbsp;
[![GitHub](https://i.stack.imgur.com/tskMh.png) GitHub](https://github.com/jitinchekka)