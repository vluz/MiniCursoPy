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

Correr com `podman run -it -p 8888:8888 -p 8501:8501 mini-curso-py`

Para jupyter correr o comando dentro do contentor:     
`jupyter notebook --ip=0.0.0.0 --allow-root`    
A URL será  http://localhost:8888/tree?token=<token>     
O token pode ser encontrado na consola.

