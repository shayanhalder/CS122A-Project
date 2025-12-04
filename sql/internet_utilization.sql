    
CREATE TABLE internet_utilization (
    bmid INT NOT NULL,
    sid INT NOT NULL,
    version INT NOT NULL,
    PRIMARY KEY (bmid, sid),
    FOREIGN KEY (bmid) REFERENCES base_model(bmid) ON DELETE CASCADE,
    FOREIGN KEY (sid) REFERENCES internet_service(sid) ON DELETE CASCADE
);
