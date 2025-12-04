
CREATE TABLE customized_model (
    bmid INT,
    mid INT NOT NULL,
    PRIMARY KEY (bmid, mid),
    FOREIGN KEY (bmid) REFERENCES base_model(bmid) ON DELETE CASCADE
);
