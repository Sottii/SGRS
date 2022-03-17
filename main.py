from website import criar_app


app = criar_app()

if __name__ == '__main__':  #3 só se rodar o app isso funciona
    app.run(debug=True)  #4 sempre que fizermos uma mudança, automaticamente, rerun o servidor
