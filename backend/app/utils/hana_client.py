from typing import Optional, Dict, Any
from hdbcli import dbapi
from contextlib import contextmanager
from ..config.hana import HanaSettings

class HanaClient:
    def __init__(self, settings: HanaSettings):
        self.settings = settings
        self._connection_pool = []
        self._max_connections = settings.HANA_POOL_SIZE
        self._max_overflow = settings.HANA_MAX_OVERFLOW

    @contextmanager
    def get_connection(self):
        """Get a connection from the pool or create a new one if needed."""
        connection = None
        try:
            if self._connection_pool:
                connection = self._connection_pool.pop()
            else:
                connection = self._create_connection()
            yield connection
        finally:
            if connection:
                if len(self._connection_pool) < self._max_connections:
                    self._connection_pool.append(connection)
                else:
                    connection.close()

    def _create_connection(self) -> dbapi.Connection:
        """Create a new connection to the HANA database."""
        return dbapi.connect(
            address=self.settings.HANA_HOST,
            port=self.settings.HANA_PORT,
            user=self.settings.HANA_USER,
            password=self.settings.HANA_PASSWORD,
            encrypt=self.settings.HANA_SSL,
            timeout=self.settings.HANA_CONNECTION_TIMEOUT
        )

    def execute_query(self, query: str, params: Optional[Dict[str, Any]] = None) -> list:
        """Execute a query and return the results."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            try:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                return cursor.fetchall()
            finally:
                cursor.close()

    def execute_many(self, query: str, params_list: list) -> None:
        """Execute the same query with different parameters multiple times."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.executemany(query, params_list)
                conn.commit()
            finally:
                cursor.close()

    def execute_ddl(self, ddl: str) -> None:
        """Execute DDL statements (CREATE, ALTER, DROP, etc.)."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(ddl)
                conn.commit()
            finally:
                cursor.close()

    def get_table_schema(self, table_name: str) -> list:
        """Get the schema of a table."""
        query = f"""
        SELECT COLUMN_NAME, DATA_TYPE, LENGTH, SCALE, IS_NULLABLE
        FROM TABLE_COLUMNS
        WHERE SCHEMA_NAME = ? AND TABLE_NAME = ?
        ORDER BY POSITION
        """
        return self.execute_query(query, [self.settings.HANA_SCHEMA, table_name])

    def check_connection(self) -> bool:
        """Check if the connection to HANA is working."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT 1 FROM DUMMY")
                result = cursor.fetchone()
                return result[0] == 1
        except Exception:
            return False

    def close_all_connections(self) -> None:
        """Close all connections in the pool."""
        for conn in self._connection_pool:
            try:
                conn.close()
            except Exception:
                pass
        self._connection_pool.clear() 