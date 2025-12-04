
CREATE TABLE configuration_utilization (
    bmid INT NOT NULL,
    mid INT NOT NULL,
    cid INT NOT NULL,
    duration INT NOT NULL,
    PRIMARY KEY (bmid, mid, cid),
    FOREIGN KEY (bmid, mid) REFERENCES customized_model(bmid, mid) ON DELETE CASCADE,
    FOREIGN KEY (cid) REFERENCES configuration(cid) ON DELETE CASCADE
);
