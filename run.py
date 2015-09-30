from app import app
import os

port = int(os.getenv('VCAP_APP_PORT', 5000))

app.run(host='localhost', port=port, debug = True)
