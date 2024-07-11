from api import app, routes
import os

if __name__ == 'main':
    port = int(os.getenv('PORT'), '5000')
    app.run(host='0.0.0.0', port = port)

# if __name__ == 'main':
#     app.run(debug=True)
