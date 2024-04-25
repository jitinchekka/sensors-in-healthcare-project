import json
import base64
import io
import numpy as np
import cv2
from flask import Flask, render_template, request
from matplotlib import pyplot as plt
import matplotlib

matplotlib.use("Agg")


app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * \
    1024  # Set maximum file size to 16MB

# Standard red, green, blue intensities for hCG standards are 183.4, 186.7, 181.3
standards = {0: [181.3, 186.7, 183.4], 500: [  # conc: [blue, green, red]
    175.6, 174.1, 181.5], 1000: [163.4, 154.5, 172.9]}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files["image"]
    if file:
        img = cv2.imdecode(np.frombuffer(
            file.read(), np.uint8), cv2.IMREAD_COLOR)

        points_str = request.form["points"]
        points = json.loads(points_str)
        points = [(int(x), int(y)) for x, y in points]
        print(points)

        avg_intentisies = []  # Average intensities of the points for each color
        for i in range(3):  # 3 colors: blue, green, red
            avg_intentisies.append(np.mean([img[y, x, i] for x, y in points]))
        print("Average intensities: ", avg_intentisies)
        std_absorbances = {}
        # std_absorbances of a colour of a concentration is the -log10 of the intensity divided by intensity of 0 concentration
        for conc, intensities in standards.items():
            std_absorbances[conc] = []
            for i in range(3):
                std_absorbances[conc].append(
                    -np.log10(standards[conc][i]/standards[0][i]))

        print("Std absorbances: ", std_absorbances)

        unknown_absorbance = []
        for i in range(3):
            unknown_absorbance.append(
                -np.log10(avg_intentisies[i]/standards[0][i]))

        # Plot the B, G, R intensities of the standards and unknown
        # Separate plots for each color
        # Make three lists of concentrations and absorbances for each color
        b_concs = list(standards.keys())
        b_absorbances = [std_absorbances[c][0] for c in b_concs]
        r_concs = list(standards.keys())
        r_absorbances = [std_absorbances[c][2] for c in r_concs]
        g_concs = list(standards.keys())
        g_absorbances = [std_absorbances[c][1] for c in g_concs]

        print("Blue concs: ", b_concs)
        print("Blue absorbances: ", b_absorbances)

        plt.figure(figsize=(6, 4))
        plt.scatter(
            b_concs,
            b_absorbances,
            label="Blue",
            color="blue",
        )
        plt.scatter(
            r_concs,
            r_absorbances,
            label="Red",
            c="red",
        )
        plt.scatter(
            g_concs,
            g_absorbances,
            label="Green",
            c="green",
        )
        plt.scatter([unknown_absorbance[0]], [0],
                    color="black", label="Unknown")

        # Plot and join the points with lines
        plt.plot(b_concs, b_absorbances, color="blue")
        plt.plot(r_concs, r_absorbances, color="red")
        plt.plot(g_concs, g_absorbances, color="green")

        print("Unknown absorbance: ", unknown_absorbance)
        plt.xlabel("hCG Concentration (mIU/mL)")
        plt.ylabel("Absorbance")
        plt.legend()

        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        plot_url = base64.b64encode(buf.getvalue()).decode("utf8")

        concs = sorted(standards.keys())
        # interpolate the unknown concentration separately for each color and take the average
        unknown_conc = np.mean([np.interp(unknown_absorbance[i], [
                               std_absorbances[c][i] for c in concs], concs) for i in range(3)])
        print(unknown_conc)
        return render_template(
            "result.html", plot_url=plot_url, unknown_conc=unknown_conc, intensities=avg_intentisies, absorbances=unknown_absorbance
        )
    else:
        return "No image uploaded", 400


if __name__ == "__main__":
    app.run(debug=True)
