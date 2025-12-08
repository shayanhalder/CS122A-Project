
CREATE TABLE BaseModel (
    bmid INT,
    creator_uid INT NOT NULL,
    description TEXT NOT NULL,
    PRIMARY KEY (bmid),
    FOREIGN KEY (creator_uid) REFERENCES AgentCreator(uid) ON DELETE CASCADE
);
