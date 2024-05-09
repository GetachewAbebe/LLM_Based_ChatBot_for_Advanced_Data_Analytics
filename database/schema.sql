-- Cities
CREATE TABLE cities_chart_data (
    date DATE,
    cities VARCHAR(255),
    city_name VARCHAR(255),
    views INT
);

CREATE TABLE cities_table_data (
    cities VARCHAR(255),
    city_name VARCHAR(255),
    geography1 VARCHAR(255),
    geography2 VARCHAR(255),
    views INT,
    watch_time_hours NUMERIC(10, 4),
    avg_view_duration INTERVAL
);

CREATE TABLE cities_totals (
    date DATE,
    views INT
);

-- Content Type
CREATE TABLE content_type_chart_data (
    date DATE,
    content_type VARCHAR(255),
    views INT
);

CREATE TABLE content_type_table_data (
    content_type VARCHAR(255),
    views INT,
    watch_time_hours NUMERIC(10, 4),
    avg_view_duration INTERVAL
);

CREATE TABLE content_type_totals (
    date DATE,
    views INT
);

-- Device Type
CREATE TABLE device_type_chart_data (
    date DATE,
    device_type VARCHAR(255),
    views INT
);

CREATE TABLE device_type_table_data (
    device_type VARCHAR(255),
    views INT,
    watch_time_hours NUMERIC(10, 4),
    avg_view_duration INTERVAL
);

CREATE TABLE device_type_totals (
    date DATE,
    views INT
);

-- Geography
CREATE TABLE geography_chart_data (
    date DATE,
    geography VARCHAR(255),
    views INT
);

CREATE TABLE geography_table_data (
    geography VARCHAR(255),
    views INT,
    watch_time_hours NUMERIC(10, 4),
    avg_view_duration INTERVAL
);

CREATE TABLE geography_totals (
    date DATE,
    views INT
);

-- New and Returning Viewers
CREATE TABLE new_returning_viewers_chart_data (
    date DATE,
    new_and_returning_viewers VARCHAR(255),
    views INT
);

CREATE TABLE new_returning_viewers_table_data (
    new_and_returning_viewers VARCHAR(255),
    views INT,
    watch_time_hours NUMERIC(10, 4),
    avg_view_duration INTERVAL
);

CREATE TABLE new_returning_viewers_totals (
    date DATE,
    views INT
);

-- Operating System
CREATE TABLE operating_system_chart_data (
    date DATE,
    operating_system VARCHAR(255),
    views INT
);

CREATE TABLE operating_system_table_data (
    operating_system VARCHAR(255),
    views INT,
    watch_time_hours NUMERIC(10, 4),
    avg_view_duration INTERVAL
);

CREATE TABLE operating_system_totals (
    date DATE,
    views INT
);

-- Sharing Service
CREATE TABLE sharing_service_chart_data (
    date DATE,
    sharing_service VARCHAR(255),
    shares INT
);

CREATE TABLE sharing_service_table_data (
    sharing_service VARCHAR(255),
    shares INT
);

CREATE TABLE sharing_service_totals (
    date DATE,
    shares INT
);

-- Subscription Source
CREATE TABLE subscription_source_chart_data (
    date DATE,
    subscription_source VARCHAR(255),
    subscribers INT
);

CREATE TABLE subscription_source_table_data (
    subscription_source VARCHAR(255),
    subscribers INT,
    subscribers_gained INT,
    subscribers_lost INT
);

CREATE TABLE subscription_source_totals (
    date DATE,
    subscribers INT
);

-- Subscription Status
CREATE TABLE subscription_status_chart_data (
    date DATE,
    subscription_status VARCHAR(255),
    views INT
);

CREATE TABLE subscription_status_table_data (
    subscription_status VARCHAR(255),
    views INT,
    watch_time_hours NUMERIC(10, 4),
    avg_view_duration INTERVAL
);

CREATE TABLE subscription_status_totals (
    date DATE,
    views INT
);

-- Subtitles
CREATE TABLE subtitles_chart_data (
    date DATE,
    subtitles_and_cc VARCHAR(255),
    views INT
);

CREATE TABLE subtitles_table_data (
    subtitles_and_cc VARCHAR(255),
    views INT,
    watch_time_hours NUMERIC(10, 4),
    avg_view_duration INTERVAL
);

CREATE TABLE subtitles_totals (
    date DATE,
    views INT
);

-- Traffic Source 
CREATE TABLE traffic_source_chart_data (
    date DATE,
    traffic_source VARCHAR(255),
    views INT
);

CREATE TABLE traffic_source_table_data (
    traffic_source VARCHAR(255),
    views INT
);

CREATE TABLE traffic_source_totals (
    date DATE,
    views INT
);

-- Viewer Age

CREATE TABLE viewer_age_table_data (
    viewer_age VARCHAR(50),
    views NUMERIC(5,2),
    avg_view_duration INTERVAL,
    avg_percentage_viewed NUMERIC(5,2),
    watch_time_hours_percentage NUMERIC(5,2)
);

-- Viewer Gender

CREATE TABLE viewer_gender_table_data (
    viewer_gender VARCHAR(10),
    views NUMERIC(5,2),
    avg_view_duration INTERVAL,
    avg_percentage_viewed NUMERIC(5,2),
    watch_time_hours_percentage NUMERIC(5,2)
);

-- Viewership by Date

CREATE TABLE viewership_by_date_table_data (
    date DATE PRIMARY KEY,
    views INT NOT NULL,
    watch_time_hours NUMERIC(10, 4),
    avg_view_duration INTERVAL
);

CREATE TABLE viewership_by_date_totals (
    date DATE PRIMARY KEY,
    views INT NOT NULL
);
