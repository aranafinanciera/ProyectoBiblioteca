# conexionredis.py
import redis
from PyQt6.QtWidgets import QMessageBox

def conectar_redis(parent=None):
    try:
        r = redis.Redis(
            host='192.168.52.176',
            port=6379,
            db=1,
            password='changeme',
            decode_responses=True
        )

        r.ping()
        QMessageBox.information(parent, "Conexión Exitosa", "✅ Conexión a Redis exitosa.")
        return r

    except redis.ConnectionError as e:
        QMessageBox.critical(parent, "Error de BD", f"❌ No se pudo conectar a Redis:\n{e}")
        return None
