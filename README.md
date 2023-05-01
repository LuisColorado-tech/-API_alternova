# Clonar el repositorio
git clone <url-del-repositorio>

# Crear un entorno virtual
python -m venv venv

# Activar el entorno virtual
source venv/bin/activate

# Instalar los requisitos
pip install -r requirements.txt

# Crear la base de datos
python manage.py migrate

# Ejecutar el servidor
python manage.py runserver
