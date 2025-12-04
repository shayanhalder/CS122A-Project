
CREATE TABLE base_model (
    bmid INT,
    creator_uid INT NOT NULL,
    description TEXT NOT NULL,
    PRIMARY KEY (bmid),
    FOREIGN KEY (creator_uid) REFERENCES agent_creator(uid) ON DELETE CASCADE
);
