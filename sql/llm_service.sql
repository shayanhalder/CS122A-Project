
CREATE TABLE llm_service (
    sid INT,
    domain TEXT,
    PRIMARY KEY (sid),
    FOREIGN KEY (sid) REFERENCES internet_service(sid) ON DELETE CASCADE
);
