# Criando ambiente virtual
python -m venv venv

# Conectando no ambiente virtual
.\venv\Scripts\activate

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
