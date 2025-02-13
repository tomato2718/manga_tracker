__all__ = ["INIT_TABLE", "DROP_TABLE", "INSERT"]

INIT_TABLE = """\
CREATE TABLE IF NOT EXISTS manga (
    id BLOB PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    source VARCHAR(255) NOT NULL,
    link VARCHAR(255) NOT NULL,
    latest_chapter INT NOT NULL,
    updated FLOAT NOT NULL
);
"""

DROP_TABLE = """\
DROP TABLE IF EXISTS manga;
"""

INSERT = """\
INSERT INTO manga 
VALUES (?, ?, ?, ?, ?, ?, ?)
"""
