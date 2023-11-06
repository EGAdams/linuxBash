from flask import Flask, request, render_template_string
import datetime

app = Flask(__name__)

HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">

    <title>Comment Logger</title>
  </head>
  <body>
    <div class="container">
      <h1 class="mt-5">Enter your comment</h1>
      <form method="post">
        <div class="mb-3">
          <textarea class="form-control" name="comment" rows="4" required></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </div>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        comment = request.form['comment']
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('log.txt', 'a') as f:
            f.write(f'{timestamp}: {comment}\n')
        return 'Comment logged successfully'
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run()
