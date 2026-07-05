from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():

    result = ""

    if request.method == "POST":

        try:
            first = float(request.form["first"])
            first_rate = float(request.form["first_rate"])

            second = float(request.form["second"])
            second_rate = float(request.form["second_rate"])

            performance = float(request.form["performance"])

            score = (
            first * first_rate / 100 +
            second * second_rate / 100 +
            performance
            )

if score > 100:
    result = "❌ 계산 결과가 100점을 초과했습니다. 입력값을 다시 확인해주세요."

else:
    result = f"{score:.2f}"

        except:
            result = "입력값을 확인하세요."

    # 결과 화면
    if request.method == "POST":
        return f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">

<style>
body {{
    font-family: Arial;
    background:#f4f6f9;
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;
}}

.container {{
    background:white;
    width:90%;
    max-width:400px;
    padding:30px;
    border-radius:15px;
    text-align:center;
    box-shadow:0 0 15px rgba(0,0,0,0.15);
}}

.score {{
    font-size:40px;
    color:#007bff;
    font-weight:bold;
    margin:25px 0;
}}

button {{
    width:100%;
    padding:15px;
    font-size:18px;
    border:none;
    border-radius:10px;
    background:#28a745;
    color:white;
    cursor:pointer;
}}
</style>
</head>

<body>

<div class="container">

<h2>📚 학기말 성적</h2>

<div class="score">
{result}
</div>

<form method="GET">
<button>다시 계산하기</button>
</form>

</div>

</body>
</html>
"""

    # 입력 화면
    return """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">

<style>

body{
font-family:Arial;
background:#f4f6f9;
display:flex;
justify-content:center;
padding:20px;
}

.container{
background:white;
width:100%;
max-width:400px;
padding:20px;
border-radius:15px;
box-shadow:0 0 15px rgba(0,0,0,0.15);
}

input{
width:100%;
padding:12px;
margin-top:8px;
margin-bottom:18px;
font-size:16px;
border-radius:8px;
border:1px solid #ccc;
box-sizing:border-box;
}

button{
width:100%;
padding:15px;
font-size:18px;
background:#007bff;
color:white;
border:none;
border-radius:10px;
cursor:pointer;
}

</style>
</head>

<body>

<div class="container">

<h2 align="center">📚 학기말 성적 계산기</h2>

<form method="POST">

1차 지필 점수
<input type="number" step="0.01" name="first" required>

1차 지필 반영비율(%)
<input type="number" step="0.01" name="first_rate" required>

2차 지필 점수
<input type="number" step="0.01" name="second" required>

2차 지필 반영비율(%)
<input type="number" step="0.01" name="second_rate" required>

수행평가 환산점수
<input type="number" step="0.01" name="performance" required>

<button type="submit">계산하기</button>

</form>

</div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
