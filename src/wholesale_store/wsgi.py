from waitress import serve

from wholesale_store import create_app

app = create_app()
if __name__=='__main__':
    serve(app, port=8000)
