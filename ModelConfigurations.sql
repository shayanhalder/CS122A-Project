
CREATE TABLE ModelConfigurations (
    bmid INT NOT NULL,
    mid INT NOT NULL,
    cid INT NOT NULL,
    duration INT NOT NULL,
    PRIMARY KEY (bmid, mid, cid),
    FOREIGN KEY (bmid, mid) REFERENCES CustomizedModel(bmid, mid) ON DELETE CASCADE,
    FOREIGN KEY (cid) REFERENCES Configuration(cid) ON DELETE CASCADE
);
