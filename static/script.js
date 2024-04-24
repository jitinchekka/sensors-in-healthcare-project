const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
let img;
let points = [];

const drawPoints = () => {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
  points.forEach((point) => {
    ctx.beginPath();
    ctx.arc(point.x, point.y, 3, 0, 2 * Math.PI);
    ctx.fillStyle = "red";
    ctx.fill();
  });
};

const imageInput = document.getElementById("image");
imageInput.addEventListener("change", (e) => {
  const file = e.target.files[0];
  const reader = new FileReader();
  reader.onload = () => {
    img = new Image();
    img.onload = () => {
      canvas.width = img.width;
      canvas.height = img.height;
      drawPoints();
    };
    img.src = reader.result;
  };
  reader.readAsDataURL(file);
});

canvas.addEventListener("click", (e) => {
  const rect = canvas.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;
  points.push({ x, y });
  drawPoints();
});

const analyzeBtn = document.getElementById("analyze-btn");
analyzeBtn.addEventListener("click", () => {
  const formData = new FormData();
  formData.append("image", imageInput.files[0]);
  formData.append(
    "points",
    JSON.stringify(points.map((point) => [point.x, point.y]))
  );

  fetch("/analyze", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.text())
    .then((html) => {
      const parser = new DOMParser();
      const doc = parser.parseFromString(html, "text/html");
      document.body.innerHTML = doc.body.innerHTML;
    })
    .catch((error) => console.error("Error:", error));
});
