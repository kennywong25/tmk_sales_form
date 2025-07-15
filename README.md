# Proyecto Full Stack - Sistema de Ventas

Este proyecto consiste en una aplicación web completa para el manejo de ventas, con un backend en FastAPI y un frontend en React, diseñada para almacenar datos en BigQuery.

## 🏗️ Arquitectura General

La aplicación sigue una arquitectura de microservicios con separación clara entre frontend y backend, facilitando el despliegue independiente y la escalabilidad.

## 🔧 Backend

### Estructura del Proyecto

```
backend/
├── app/
│   ├── main.py                  # Entry point (FastAPI app)
│   ├── config.py                # Configuración de entorno (dotenv, secrets)
│   ├── logger.py                # Logger personalizado
│   ├── routes/                  # Endpoints agrupados
│   │   ├── ventas.py
│   │   └── tokens.py
│   ├── services/                # Lógica de negocio
│   │   ├── ventas_service.py
│   │   └── token_service.py
│   ├── schemas/                 # Pydantic models (request, response)
│   │   └── venta.py
│   ├── utils/                   # Helpers utilitarios
│   │   └── token_generator.py
│   └── bigquery/                # Módulo de escritura en BigQuery
│       └── writer.py
├── tests/                       # Unit tests
├── requirements.txt
├── Dockerfile
└── .env                         # Variables locales (no subir al repo)
```

### Tecnologías Backend

- **FastAPI**: Framework web moderno y rápido para APIs
- **Uvicorn**: Servidor ASGI de alto rendimiento
- **Pydantic**: Validación de datos y serialización
- **Google Cloud BigQuery**: Almacenamiento y análisis de datos
- **Python-dotenv**: Manejo de variables de entorno
- **Loguru/Structlog**: Sistema de logging avanzado
- **Pytest**: Framework de testing

### Características del Backend

- **API RESTful**: Endpoints bien estructurados siguiendo convenciones REST
- **Validación de datos**: Usando Pydantic para validación automática
- **Logging estructurado**: Para mejor debugging y monitoreo
- **Integración BigQuery**: Escritura directa a Google Cloud BigQuery
- **Gestión de tokens**: Sistema de autenticación y autorización
- **Testing**: Suite de pruebas unitarias con pytest

## 🎨 Frontend

### Estructura del Proyecto

```
frontend/
├── public/                     # Archivos públicos (favicon, etc)
├── src/
│   ├── components/             # Componentes reutilizables
│   ├── pages/                  # Página principal del formulario
│   ├── services/               # Conexión a API del backend
│   ├── utils/                  # Helpers (validación, formato)
│   └── App.jsx
├── Dockerfile
├── vite.config.js
├── package.json
├── .env
└── nginx.conf                  # Configuración del servidor
```

### Tecnologías Frontend

- **React**: Biblioteca para interfaces de usuario
- **Vite**: Build tool moderno y rápido
- **Axios/Fetch**: Cliente HTTP para consumir APIs
- **TailwindCSS**: Framework CSS utilitario (opcional)
- **React Router**: Enrutamiento del lado del cliente
- **Nginx**: Servidor web para producción

### Características del Frontend

- **Componentes reutilizables**: Arquitectura modular y mantenible
- **Estado reactivo**: Manejo eficiente del estado de la aplicación
- **Validación del lado del cliente**: Mejor experiencia de usuario
- **Responsive design**: Adaptable a diferentes dispositivos
- **Build optimizado**: Usando Vite para builds rápidos

## 🚀 Despliegue

Ambos servicios incluyen Dockerfile para facilitar el despliegue en contenedores:

- **Backend**: Ejecuta con Uvicorn en un contenedor Python
- **Frontend**: Build estático servido por Nginx

## 🔒 Configuración

### Variables de Entorno

**Backend (.env)**:
- Configuración de BigQuery
- Secrets y tokens
- Configuración de base de datos

**Frontend (.env)**:
- URL del API backend
- Configuraciones del cliente

## 🧪 Testing

El proyecto incluye:
- Tests unitarios para el backend con pytest
- Estructura preparada para tests de integración
- Validación de endpoints y servicios

## 📋 Requisitos

- Python 3.8+
- Node.js 16+
- Cuenta de Google Cloud (para BigQuery)
- Docker (opcional, para despliegue)

## 🏃‍♂️ Inicio Rápido

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

---

## Repositorios en Artifact Registry

### Repositorios creados 

Repositorios creados para alojar el ambiente dev y prod del backend que orquesta la recepción y flujo de datos.

#### Backend

```bash
# Repo para desarrollo (backend del formulario Wolkvox)
gcloud artifacts repositories create connectdatasilver-wolkvox-salesform-backend-dev \
  --repository-format=docker \
  --location=us-central1 \
  --description="Backend de Wolkvox SalesForm (dev)"

# Repo para producción
gcloud artifacts repositories create connectdatasilver-wolkvox-salesform-backend-prod \
  --repository-format=docker \
  --location=us-central1 \
  --description="Backend de Wolkvox SalesForm (prod)"
```

#### Fronend

Es importante está en el proyecto correcto para realizar el despliegue, ejecutar el siguiente comando.

### Carga de Imagen

Ambiente Dev
```bash
gcloud builds submit backend \
  --config=backend/cloudbuild-dev.yaml \
  --project=connectdatasilver
```

Ambiente Prod
```bash
gcloud builds submit backend \
  --config=backend/cloudbuild-prod.yaml \
  --project=connectdatasilver
```

### Despliegue de función

Una vez ya la imagene sté actualizada podemos desplegar nuestras funciones en Cloud Run.

#### Backend

## Despliegue en Cloud Run

### Dev

```bash

```