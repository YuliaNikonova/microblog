from app import app
import os



# On Bluemix, get the port number from the environment variable VCAP_APP_PORT
# When running this app on the local machine, default the port to 8080
port = int(os.getenv('VCAP_APP_PORT', 5000))

app.run(host='0.0.0.0', port=port)
