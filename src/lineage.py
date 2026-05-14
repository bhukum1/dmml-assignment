import sqlite3

conn = sqlite3.connect(
    "metadata/lineage.db"
)

cursor = conn.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS lineage (
        dataset_version TEXT,
        processed_file TEXT,
        model_name TEXT,
        accuracy REAL
    )
    '''
)

cursor.execute(
    '''
    INSERT INTO lineage VALUES (
        'v1',
        'cleaned.csv',
        'RandomForest',
        0.85
    )
    '''
)

conn.commit()

conn.close()

print("Lineage metadata stored")
