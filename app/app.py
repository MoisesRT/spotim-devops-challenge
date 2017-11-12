from flask import Flask

import router

app = Flask(__name__)
app.add_url_rule('/secret', view_func=router.secret)
app.add_url_rule('/health', view_func=router.health)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
