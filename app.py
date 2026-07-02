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

            total_rate = first_rate + second_rate

            all=first*first_rate/100 + second*second_rate/100 + performance

            if first < 0 or first > 100:
                result = "1차 지필 점수는 0~100 사이여야 합니다."

            elif second < 0 or second > 100:
                result = "2차 지필 점수는 0~100 사이여야 합니다."

            elif first_rate < 0 or second_rate < 0:
                result = "반영비율은 0 이상이어야 합니다."

            elif total_rate > 100:
                result = "반영비율의 합이 100%를 초과했습니다."
            elif all > 100:
                result = "총합 성적이 100을 초과했습니다"
            else:
                score = (
                        first * first_rate / 100 +
                        second * second_rate / 100 +
                        performance
                )

                result = f"학기말 성적은 {score:.2f}점 입니다."

        except:
            result = "입력값을 확인하세요."

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
    body {{
        font-family: Arial, sans-serif;
        background: #f4f6f9;
        display: flex;
        justify-content: center;
        padding: 20px;
    }}

    .container {{
        background: white;
        width: 100%;
        max-width: 400px;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 0 15px rgba(0,0,0,0.15);
    }}

    h1 {{
        text-align: center;
        color: #2c3e50;
    }}

    label {{
        font-weight: bold;
    }}

    input[type=number] {{
        width: 100%;
        padding: 12px;
        margin: 8px 0 18px 0;
        border-radius: 8px;
        border: 1px solid #ccc;
        box-sizing: border-box;
        font-size: 16px;
    }}

    button {{
        width: 100%;
        padding: 15px;
        background: #007bff;
        color: white;
        border: none;
        border-radius: 8px;
        font-size: 18px;
        cursor: pointer;
    }}

    button:hover {{
        background: #0056b3;
    }}

    .result {{
        margin-top:20px;
        padding:15px;
        background:#e8f5e9;
        border-radius:10px;
        text-align:center;
        font-size:20px;
        font-weight:bold;
    }}
    </style>
    </head>

    <body>

    <div class="container">

    <h1>📚 학기말 성적 계산기</h1>

    <form method="post">

    <label>1차 지필 점수</label>
    <input type="number" name="first">

    <label>1차 지필 반영비율(%)</label>
    <input type="number" name="first_rate">

    <label>2차 지필 점수</label>
    <input type="number" name="second">

    <label>2차 지필 반영비율(%)</label>
    <input type="number" name="second_rate">

    <label>수행평가 환산점수</label>
    <input type="number" name="performance" placeholder="예: 40">

    <button type="submit">계산하기</button>

    </form>

    <div class="result">
    {result}
    </div>

    </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
