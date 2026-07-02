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
            performance_rate = float(request.form["performance_rate"])

            total_rate = first_rate + second_rate + performance_rate

            if total_rate != 100:
                result = f"반영비율의 합이 {total_rate}%입니다. 100%가 되어야 합니다."
            else:
                score = (
                    first * first_rate / 100 +
                    second * second_rate / 100 +
                    performance * performance_rate / 100
                )

                result = f"학기말 성적은 {score:.2f}점 입니다."

        except:
            result = "입력값을 확인하세요."

    return f"""
    <h1>📚 학기말 성적 계산기</h1>

    <form method="post">

        <h3>1차 지필</h3>
        점수 : <input type="number" name="first"><br><br>
        반영비율(%) : <input type="number" name="first_rate"><br><br>

        <h3>2차 지필</h3>
        점수 : <input type="number" name="second"><br><br>
        반영비율(%) : <input type="number" name="second_rate"><br><br>

        <h3>수행평가</h3>
        점수 : <input type="number" name="performance"><br><br>
        반영비율(%) : <input type="number" name="performance_rate"><br><br>

        <input type="submit" value="계산하기">

    </form>

    <h2>{result}</h2>
    """

if __name__ == "__main__":
    app.run(debug=True)
