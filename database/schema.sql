CREATE TABLE SubscriptionTable (
    subscription_status VARCHAR(50),
    views INT,
    watch_time_hours NUMERIC,
    average_view_duration INTERVAL
);

CREATE TABLE SubscriptionChart (
    date DATE,
    subscription_status VARCHAR(50),
    views INT
);

CREATE TABLE SubscriptionTotals (
    date DATE,
    views INT
);
 -- create tables for the other data categories using the same naming approach
 -- add primary and foreign keys where necessary