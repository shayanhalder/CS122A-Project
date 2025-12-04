
CREATE TABLE CustomizedModel (
    bmid INT,
    mid INT NOT NULL,
    PRIMARY KEY (bmid, mid),
    FOREIGN KEY (bmid) REFERENCES BaseModel(bmid) ON DELETE CASCADE
);
