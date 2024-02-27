<img src="MiniCursoPython.jpg" width=33% height=33%>

# Mini Curso Python

Repositório de apresentação e pequenos programas 
destinados a um curso livre de Python 3

Para poder correr o código:

```
git clone https://github.com/vluz/MiniCursoPy.git
pip install -r requirements.txt
```

Para criar a imagem:

`cd podman_compose`

`podman build -t mini-curso-py .`
ou
`podman-compose build`

Correr com `podman run -it -p 8888:8888 -p 8501:8501 -p 5000:5000 mini-curso-py`


Para jupyter correr o comando dentro do contentor:     
`jupyter notebook --ip=0.0.0.0 --allow-root`    
A URL será `http://localhost:8888/tree?token=<token>`     
O token pode ser encontrado na consola.


Para Streamlit correr `streamlit run <programa.py>`     
em que `<programa.py>` é o programa a correr.     
A URL será `http://localhost:8501`


Os programas com tkinter só correm localmente, a imagem não tem GUI.     
O exemplo 14 não pode correr na imagem pela mesma razão.


`ultimate_qr.py` requer uma chave de API     
Mais informação em https://developers.giphy.com/docs/api#quick-start-guide     


Para correr o exemplo de Flask use `flask run --host=0.0.0.0`

     
