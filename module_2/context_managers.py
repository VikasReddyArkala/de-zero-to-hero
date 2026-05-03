import sqlite3

class PipelineDB:
    """
    A context manager that wraps a SQLite connection.
    On entry: opens the connection and returns a cursor.
    On exit: commits if everything went fine, rolls back if an exception occurred.
    This pattern — commit on success, rollback on failure — is called a transaction,
    and it's one of the most important data integrity patterns you'll use.
    """

    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        cursor = self.conn.cursor()
        return cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        self.conn.close()
        return False
    
# Test it — this should work cleanly
with PipelineDB("orders.db") as cursor:
    cursor.execute("SELECT COUNT(*) FROM orders")
    print(f"Orders in DB: {cursor.fetchone()[0]}")

# Test the rollback — this should NOT corrupt the database
try:
    with PipelineDB("orders.db") as cursor:
        cursor.execute("DELETE FROM orders")  # deletes everything
        raise Exception("something went wrong mid-transaction!")
        # the DELETE should be rolled back because of the exception
except Exception as e:
    print(f"Caught: {e}")

# Verify the data is still there after the failed transaction
with PipelineDB("orders.db") as cursor:
    cursor.execute("SELECT COUNT(*) FROM orders")
    print(f"Orders still in DB after rollback: {cursor.fetchone()[0]}")
    