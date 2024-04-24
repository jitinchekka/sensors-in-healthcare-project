import base64
import io
import numpy as np
import cv2
from flask import Flask, render_template, request
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend for non-GUI environments


app = Flask(__name__)

# Define the standard hCG concentrations and their corresponding blue intensities
standards = {
    0: 255,  # Negative control
    25: 200,  # 25 mIU/mL
    100: 150  # 100 mIU/mL
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    # Get the uploaded image
    file = request.files['image']
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

    # Define the points to sample for the test line
    points = [(100, 200), (120, 200), (140, 200), (160, 200), (180, 200)]

    # Get the blue pixel intensities for the test line
    blue_intensities = [img[y, x, 0] for x, y in points]
    avg_blue_intensity = sum(blue_intensities) / len(blue_intensities)

    # Calculate the absorbance for the known standards
    std_absorbances = {conc: -np.log10(intensity / 255)
                       for conc, intensity in standards.items()}

    # Calculate the absorbance for the unknown sample
    unknown_absorbance = -np.log10(avg_blue_intensity / 255)

    # Plot the absorbance vs concentration
    plt.figure(figsize=(6, 4))
    plt.scatter([0] + list(standards.keys()), [std_absorbances[0]] +
                list(std_absorbances.values()), label='Standards')
    plt.scatter([unknown_absorbance], [0], color='r', label='Unknown')
    plt.xlabel('hCG Concentration (mIU/mL)')
    plt.ylabel('Absorbance')
    plt.legend()

    # Save the plot to a buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plot_url = base64.b64encode(buf.getvalue()).decode('utf8')

    # Determine the approximate hCG concentration
    concs = sorted(standards.keys())
    abs_values = [std_absorbances[c] for c in concs]
    unknown_conc = np.interp(unknown_absorbance, abs_values, concs)

    return render_template('result.html', plot_url=plot_url, unknown_conc=unknown_conc)


if __name__ == '__main__':
    app.run(debug=True)
