# backend/Dockerfile

# 1. Base: Python 3.11 slim
FROM python:3.11-slim

# 2. Variables de entorno para un comportamiento consistente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# 3. Directorio de trabajo
WORKDIR /app

# 4. Instala dependencias del sistema necesarias (opcional según tu caso)
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

# 5. Copia y instala dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copia todo el código de la app
COPY . .

# 7. Exponer el puerto que usará Uvicorn
EXPOSE 8080

# 8. Comando de arranque
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
