from website import create_app

app = create_app()

if __name__ == '__main__': 
#only if we run this file we will excute app.run(debug=True). 
#Only run web server if we run this file. 
#Turn off when running in production
    app.run(debug=True)
