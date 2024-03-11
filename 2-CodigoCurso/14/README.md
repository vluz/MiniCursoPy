icomoon.ttf por <a href="https://icomoon.io">IcoMoon</a>      
icomoon.json é o projecto da fonte em icomoon.io

Sound Effects da <a href="https://pixabay.com">Pixabay</a>

---

Para gerar exe em Windows:

```
python -m venv "venv"
venv\Scripts\activate.bat
pip install pygame simpleaudio cx_Freeze
python setup.py build
copy *.wav build\exe.win-amd64-3.10\
copy icomoon.ttf build\exe.win-amd64-3.10\
venv\Scripts\deactivate.bat
```

Executavel `pares.exe` estará na dir `build\exe.win-amd64-3.10\`