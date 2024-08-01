# Criando ambiente virtual
python -m venv venv

# Conectando no ambiente virtual
.\venv\Scripts\activate

# Bibliotecas 
pip install pyqt6
pip install pyside6
pip install pillow
pip install pyinstaller
pip install PyMuPDF

# Iniciando meu git
git init
git add .
git commit -m "Initial"
git remote add origin https://github.com/danieltorreess/ProjetoItau.git
git push -u origin main
git status
git log
git log --onefile

# Chave ssh
ssh-keygen -f C:/Users/Cicero/.ssh/projetoitau_rsa -t rsa -b 4096
cat C:/Users/Cicero/.ssh/projetoitau_rsa.pub
git remote rm origin
git remote add origin git@github.com:danieltorreess/ProjetoItau.git
git push origin main

# Transformando meu arquivo .ui em .py
pyside6-uic "J:\Meu Drive\ProjetoItau\ui\window.ui" -o "J:\Meu Drive\ProjetoItau\src\window.py"

