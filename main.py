from website import create_app


app = create_app()

if __name__ == '__main__':  #3 só se rodar o app isso funciona
    app.run(debug=True)  #4 sempre que fizermos uma mudança, automaticamente, rerun o servidor