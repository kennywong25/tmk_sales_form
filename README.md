Arquitectura del Backend

´´´
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
´´´

Tecnologías / Librerías
fastapi
uvicorn[standard]
pydantic
google-cloud-bigquery
python-dotenv
loguru o structlog para logging
pytest (tests)


Arquitectura del Frontend
´´´
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

Tecnologías / Librerías
React
Vite
Axios o fetch
TailwindCSS (opcional, para UI limpia)
React Router (si decides tener más de una ruta)
´´´