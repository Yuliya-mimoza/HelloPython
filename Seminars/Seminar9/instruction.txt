# python -m venv venv
# python3 -m venv venv
# source venv/bin/activate
# venv\Scripts\activate

# pip freeze
# pip freeze > requirements.txt

# pip install -r requirements.txt


# РЕШЕНИЕ ДЛЯ МАК -в системном терминале вот такую команду запустили: python3 -m pip install --upgrade pip


# РЕШЕНИЕ ДЛЯ WINDOWS - В Windows при установке Python необходимо было установить галочку для установки pip, установить путь Python в папку с:\Program Files, а не в User, и обязательно поставить галочку add PATH

# иногнда в винде в командной строке - Set-ExecutionPolicy -ExecutionPolicy AllSigned , если не активируется

# Set-ExecutionPolicy Unrestricted - эту коммаду в повер шел ввведите
#==========================================================================
# При установке среды прописать:
# "py -m venv venv"
# в VSCode у меня шла блокировка и выходило сообщение:
# "...так как выполнение сценариев отключено в этой системе..."
# надо запустить от имени админа Windows PowerShell и прописать:
# "Set-ExecutionPolicy RemoteSigned"
# и поставить: "A"
# вернуться в терминал VSCode и активировать venv:
# "venv\Scripts\activate.bat"

# ссылка на видео
# https://yandex.ru/video/preview/13770932925170864700