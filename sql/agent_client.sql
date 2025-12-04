
CREATE TABLE agent_client (
    uid INT,
    interests TEXT NOT NULL,
    cardholder TEXT NOT NULL,
    expire DATE NOT NULL,
    cardno INT NOT NULL,
    cvv INT NOT NULL,
    zip INT NOT NULL,
    PRIMARY KEY (uid),
    FOREIGN KEY (uid) REFERENCES user(uid) ON DELETE CASCADE
);
