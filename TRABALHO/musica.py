def exibir_frame_musica():
    main_frame.pack_forget()
    frame_musica = tk.Frame(main_frame, bg="white")
    frame_musica.pack(side=tk.TOP, fill=tk.BOTH)

    # criando o widget Canvas
    canvas = tk.Canvas(frame_musica, bg="white")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # criando a barra de rolagem e vinculando-a ao widget Canvas
    scrollbar = tk.Scrollbar(frame_musica, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=scrollbar.set)

    # criando o widget de texto com título e descrição
    texto_musica = tk.Label(canvas, text="Show de Rock", font=("Arial", 16, "bold"), bg="white", fg="white")
    texto_musica_descricao = tk.Label(canvas, text="Venha curtir um show incrível com as melhores bandas de rock do país!", font=("Arial", 14), bg="white", fg="white")
    
    # adicionando o widget de texto ao canvas
    canvas.create_window((0, 0), window=texto_musica, anchor=tk.NW)
    canvas.create_window((0, 40), window=texto_musica_descricao, anchor=tk.NW)
    
    # ajustando o tamanho do canvas para o tamanho do widget de texto
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox(tk.ALL))
