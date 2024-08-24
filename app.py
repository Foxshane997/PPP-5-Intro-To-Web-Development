from petfax import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

# Use python app.py in the terminal with the app.run(debug=True)