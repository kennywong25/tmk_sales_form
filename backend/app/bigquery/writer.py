from app.config import settings, bq_client

def insert_row(table_name: str, row: dict):
    """
    Helper genérico que inserta una fila en la tabla indicada.
    """
    table_ref = f"{settings.gcp_project}.{settings.bq_dataset}.{table_name}"
    errors = bq_client.insert_rows_json(table_ref, [row])
    if errors:
        # aquí podrías loguear antes de lanzar
        raise RuntimeError(f"Error insertando en BQ ({table_name}): {errors}")

def insert_raw(row: dict):
    insert_row(settings.bq_table_raw, row)

def insert_completed(row: dict):
    insert_row(settings.bq_table_completed, row)

def insert_dev(row: dict):
    insert_row(settings.bq_table_dev, row)