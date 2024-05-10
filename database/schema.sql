-- public.cities_chart_data definition

CREATE TABLE public.cities_chart_data (
	"Date" varchar(50) NULL,
	cities varchar(50) NULL,
	"City name" varchar(50) NULL,
	"Views" int4 NULL
);


-- public.cities_table_data definition

CREATE TABLE public.cities_table_data (
	cities varchar(255) NULL,
	city_name varchar(255) NULL,
	geography1 varchar(255) NULL,
	geography2 varchar(255) NULL,
	"views" int4 NULL,
	watch_time_hours numeric(10, 4) NULL,
	avg_view_duration interval NULL
);


-- public.cities_totals definition

CREATE TABLE public.cities_totals (
	"date" date NULL,
	"views" int4 NULL
);


-- public.content_type_chart_data definition

CREATE TABLE public.content_type_chart_data (
	"Date" varchar(50) NULL,
	"Content type" varchar(50) NULL,
	"Views" int4 NULL
);


-- public.content_type_table_data definition

CREATE TABLE public.content_type_table_data (
	content_type varchar(255) NULL,
	"views" int4 NULL,
	watch_time_hours numeric(10, 4) NULL,
	avg_view_duration interval NULL
);


-- public.content_type_totals definition

CREATE TABLE public.content_type_totals (
	"date" date NULL,
	"views" int4 NULL
);


-- public.device_type_chart_data definition

CREATE TABLE public.device_type_chart_data (
	"Date" varchar(50) NULL,
	"Device type" varchar(50) NULL,
	"Views" int4 NULL
);


-- public.device_type_table_data definition

CREATE TABLE public.device_type_table_data (
	device_type varchar(255) NULL,
	"views" int4 NULL,
	watch_time_hours numeric(10, 4) NULL,
	avg_view_duration interval NULL
);


-- public.device_type_totals definitions;

CREATE TABLE public.device_type_totals (
	"date" date NULL,
	"views" int4 NULL
);


-- public.geography_chart_data definition

CREATE TABLE public.geography_chart_data (
	"date" date NULL,
	geography varchar(255) NULL,
	"views" int4 NULL
);


-- public.geography_table_data definition

CREATE TABLE public.geography_table_data (
	geography varchar(50) NULL,
	"Views" int4 NULL,
	"Watch time (hours)" float4 NULL,
	"Average view duration" varchar(50) NULL
);


-- public.geography_totals definition

CREATE TABLE public.geography_totals (
	"Date" varchar(50) NULL,
	"Views" int4 NULL
);


-- public.new_returning_viewers_chart_data definition

CREATE TABLE public.new_returning_viewers_chart_data (
	"Date" varchar(50) NULL,
	"New and returning viewers" varchar(50) NULL,
	"Views" int4 NULL
);


-- public.new_returning_viewers_table_data definitiona;

CREATE TABLE public.new_returning_viewers_table_data (
	"New and returning viewers" varchar(50) NULL,
	"Views" int4 NULL,
	"Watch time (hours)" float4 NULL,
	"Average view duration" varchar(50) NULL
);


-- public.new_returning_viewers_totals definition

CREATE TABLE public.new_returning_viewers_totals (
	"Date" varchar(50) NULL,
	"Views" int4 NULL
);


-- public.operating_system_chart_data definition

CREATE TABLE public.operating_system_chart_data (
	"date" date NULL,
	operating_system varchar(255) NULL,
	"views" int4 NULL
);


-- public.operating_system_table_data definition

CREATE TABLE public.operating_system_table_data (
	"Operating system" varchar(50) NULL,
	"Views" int4 NULL,
	"Watch time (hours)" float4 NULL,
	"Average view duration" varchar(50) NULL
);


-- public.operating_system_totals definition

CREATE TABLE public.operating_system_totals (
	"Date" varchar(50) NULL,
	"Views" int4 NULL
);


-- public.sharing_service_chart_data definitionta;

CREATE TABLE public.sharing_service_chart_data (
	"date" date NULL,
	sharing_service varchar(255) NULL,
	shares int4 NULL
);


-- public.sharing_service_table_data definition

CREATE TABLE public.sharing_service_table_data (
	sharing_service varchar(255) NULL,
	shares int4 NULL
);


-- public.sharing_service_totals definition

CREATE TABLE public.sharing_service_totals (
	"Date" varchar(50) NULL,
	shares int4 NULL
);


-- public.subscription_source_chart_data definition

CREATE TABLE public.subscription_source_chart_data (
	"Date" varchar(50) NULL,
	"Subscription source" varchar(50) NULL,
	subscribers int4 NULL
);


-- public.subscription_source_table_data definition

CREATE TABLE public.subscription_source_table_data (
	subscription_source varchar(255) NULL,
	subscribers int4 NULL,
	subscribers_gained int4 NULL,
	subscribers_lost int4 NULL
);


-- public.subscription_status_chart_data definition

CREATE TABLE public.subscription_status_chart_data (
	"Date" varchar(50) NULL,
	"Subscription status" varchar(50) NULL,
	"Views" int4 NULL
);


-- public.subscription_status_table_data definition

CREATE TABLE public.subscription_status_table_data (
	subscription_status varchar(255) NULL,
	"views" int4 NULL,
	watch_time_hours numeric(10, 4) NULL,
	avg_view_duration interval NULL
);


-- public.subscription_status_totals definition

CREATE TABLE public.subscription_status_totals (
	"Date" varchar(50) NULL,
	"Views" int4 NULL
);


-- public.subtitles_chart_data definition

CREATE TABLE public.subtitles_chart_data (
	"Date" varchar(50) NULL,
	"Subtitles and CC" varchar(50) NULL,
	"Views" int4 NULL
);


-- public.subtitles_table_data definition

CREATE TABLE public.subtitles_table_data (
	subtitles_and_cc varchar(255) NULL,
	"views" int4 NULL,
	watch_time_hours numeric(10, 4) NULL,
	avg_view_duration interval NULL
);


-- public.subtitles_totals definition

CREATE TABLE public.subtitles_totals (
	"date" date NULL,
	"views" int4 NULL
);


-- public.traffic_source_chart_data definition

CREATE TABLE public.traffic_source_chart_data (
	"Date" varchar(50) NULL,
	"Traffic source" varchar(50) NULL,
	"Views" int4 NULL
);


-- public.traffic_source_totals definition
s;

CREATE TABLE public.traffic_source_totals (
	"Date" varchar(50) NULL,
	"Views" int4 NULL
);


-- public.viewer_age_table_data definition

CREATE TABLE public.viewer_age_table_data (
	"Viewer age" varchar(50) NULL,
	"Views (%)" float4 NULL,
	"Average view duration" varchar(50) NULL,
	"Average percentage viewed (%)" float4 NULL,
	"Watch time (hours) (%)" float4 NULL
);


-- public.viewer_gender_table_data definition

CREATE TABLE public.viewer_gender_table_data (
	viewer_gender varchar(10) NULL,
	"views" numeric(5, 2) NULL,
	avg_view_duration interval NULL,
	avg_percentage_viewed numeric(5, 2) NULL,
	watch_time_hours_percentage numeric(5, 2) NULL
);


-- public.viewership_by_date_table_data definition

CREATE TABLE public.viewership_by_date_table_data (
	"date" date NULL,
	"views" int4 NULL,
	watch_time_hours numeric(10, 4) NULL,
	avg_view_duration interval NULL
);


-- public.viewership_by_date_totals definition

CREATE TABLE public.viewership_by_date_totals (
	"Date" varchar(50) NULL,
	"Views" int4 NULL
);