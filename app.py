import matplotlib

matplotlib.use("Agg")
from matplotlib import pyplot as plt

from flask import Flask, render_template, request
import cv2
import numpy as np
import io
import base64
import json

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # Set maximum file size to 16MB

standards = {0: 255, 25: 200, 100: 150}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files["image"]
    if file:
        img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

        points_str = request.form["points"]
        points = json.loads(points_str)
        points = [(int(x), int(y)) for x, y in points]
        print(points)
        
        blue_intensities = [img[y, x, 0] for x, y in points]
        print(blue_intensities)
        avg_blue_intensity = sum(blue_intensities) / len(blue_intensities)

        std_absorbances = {
            conc: -np.log10(intensity / 255) for conc, intensity in standards.items()
        }

        unknown_absorbance = -np.log10(avg_blue_intensity / 255)

        plt.figure(figsize=(6, 4))
        plt.scatter(
            [0] + list(standards.keys()),
            [std_absorbances[0]] + list(std_absorbances.values()),
            label="Standards",
        )
        plt.scatter([unknown_absorbance], [0], color="r", label="Unknown")
        plt.xlabel("hCG Concentration (mIU/mL)")
        plt.ylabel("Absorbance")
        plt.legend()

        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        plot_url = base64.b64encode(buf.getvalue()).decode("utf8")

        concs = sorted(standards.keys())
        abs_values = [std_absorbances[c] for c in concs]
        unknown_conc = np.interp(unknown_absorbance, abs_values, concs)

        return render_template(
            "result.html", plot_url=plot_url, unknown_conc=unknown_conc
        )
    else:
        return "No image uploaded", 400


if __name__ == "__main__":
    app.run(debug=True)
