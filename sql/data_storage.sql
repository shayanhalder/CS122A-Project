
CREATE TABLE data_storage (
    sid INT,
    type TEXT,
    PRIMARY KEY (sid),
    FOREIGN KEY (sid) REFERENCES internet_service(sid) ON DELETE CASCADE
);
