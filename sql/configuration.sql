
CREATE TABLE Configuration (
    cid INT,
    client_uid INT NOT NULL,
    content TEXT NOT NULL,
    labels TEXT NOT NULL,
    PRIMARY KEY (cid),
    FOREIGN KEY (client_uid) REFERENCES AgentClient(uid) ON DELETE CASCADE
);
