    
CREATE TABLE ModelServices (
    bmid INT NOT NULL,
    sid INT NOT NULL,
    version INT NOT NULL,
    PRIMARY KEY (bmid, sid),
    FOREIGN KEY (bmid) REFERENCES BaseModel(bmid) ON DELETE CASCADE,
    FOREIGN KEY (sid) REFERENCES InternetService(sid) ON DELETE CASCADE
);
