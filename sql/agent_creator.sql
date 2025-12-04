
CREATE TABLE agent_creator (
    uid INT,
    bio TEXT,
    payout TEXT,
    PRIMARY KEY (uid),
    FOREIGN KEY (uid) REFERENCES user(uid) ON DELETE CASCADE
);
