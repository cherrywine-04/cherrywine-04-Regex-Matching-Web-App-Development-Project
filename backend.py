from flask import Flask, render_template, request
import re

backend = Flask(__name__)

@backend.route('/', methods=['POST', 'GET'])
def match():
    if request.method == 'POST':
        regex = request.form['regex']
        string = request.form['string']
        count = 0
        spans = []
        for match in re.finditer(r"{}".format(regex), string):
            count += 1
            span_info = "Match {}: \"{}\" at start index: {} and end index: {}".format(
                count, match.group(), match.start(), match.end())
            spans.append(span_info)
        return render_template("frontend.html", ans="Match Found!", regex=regex, string=string, count=count, spans=spans)
    return render_template("frontend.html", count=-1)

if __name__ == '__main__':
    backend.run(debug=True)
