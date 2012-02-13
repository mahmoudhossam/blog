from webapp import app
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # Disable this when deploying
    app.debug = True
    app.run(host='0.0.0.0', port=port)
