
CREATE TABLE LLMService (
    sid INT,
    domain TEXT,
    PRIMARY KEY (sid),
    FOREIGN KEY (sid) REFERENCES InternetService(sid) ON DELETE CASCADE
);
