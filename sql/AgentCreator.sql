
CREATE TABLE AgentCreator (
    uid INT,
    bio TEXT,
    payout TEXT,
    PRIMARY KEY (uid),
    FOREIGN KEY (uid) REFERENCES User(uid) ON DELETE CASCADE
);
