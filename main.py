from website import create_app

# assign instance of Flask application to "app" variable
app = create_app()

# run the Flask application only if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)