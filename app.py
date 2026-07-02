from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""

    if request.method == "POST":
        try:
            mid = float(request.form["mid"])
            final = float(request.form["final"])
            assignment = float(request.form["assignment"])

            score = mid * 0.4 + final * 0.4 + assignment * 0.2
            result = f"최종 성적: {score:.2f}점"

        except:
            result = "입력값을 확인하세요."

    return f"""
<h2>학기말 성적 계산기</h2>
<form method="post">
    중간고사(40%): <input type="number" name="mid"><br><br>
    기말고사(40%): <input type="number" name="final"><br><br>
    과제(20%): <input type="number" name="assignment"><br><br>

    <input type="submit" value="계산하기">
</form>

<h3>{result}</h3>
"""

if __name__ == "__main__":
    app.run(debug=True)
