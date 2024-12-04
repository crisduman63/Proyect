import asyncio
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from alembic import context
from alembic import command

# Configuración de logging
config = context.config if hasattr(context, 'config') else None  # Asegurarse de que 'config' está disponible

# Asegurarse de que el archivo de configuración se carga correctamente
if config and config.config_file_name:
    fileConfig(config.config_file_name)

# Configuración de la metadata
target_metadata = None  # Reemplazar con tu metadata si la tienes

def run_migrations_online():
    # Crear motor de conexión asíncrono
    connectable = create_async_engine(
        config.get_main_option("sqlalchemy.url"),
        echo=True,  # Habilitar logging si es necesario
    )

    # Función asíncrona para ejecutar las migraciones
    async def do_run_migrations():
        # Obtener una conexión
        async with connectable.connect() as connection:
            # Ejecutar migraciones de forma síncrona
            await connection.run_sync(run_migrations_sync)

    # Verificar si hay un bucle de eventos en ejecución
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            # Si el bucle ya está en ejecución, crear una tarea
            loop.create_task(do_run_migrations())
        else:
            # Si no hay un bucle de eventos, correr hasta completar la tarea
            loop.run_until_complete(do_run_migrations())
    except RuntimeError:
        # Crear un nuevo bucle si no existe
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(do_run_migrations())

def run_migrations_sync(connection):
    """Ejecutar las migraciones de manera síncrona"""
    # Verificar si el contexto tiene la variable 'script' antes de intentar usarla
    if 'script' not in globals():
        raise KeyError("No se encontró el script de migración en el contexto")

    # Ejecutar las migraciones de Alembic
    command.upgrade(context.config, "head")

# Comprobar si estamos en el modo offline o en línea
if context.is_offline_mode():
    print("Alembic no soporta operaciones offline con asyncpg")
else:
    run_migrations_online()
