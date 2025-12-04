
CREATE TABLE DataStorage (
    sid INT,
    type TEXT,
    PRIMARY KEY (sid),
    FOREIGN KEY (sid) REFERENCES InternetService(sid) ON DELETE CASCADE
);
