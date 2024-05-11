CREATE TABLE public.cities_chart_data (
	"Date" varchar(50) NULL,
	cities varchar(50) NULL,
	"City name" varchar(50) NULL,
	"Views" int4 NULL
);

CREATE TABLE public.cities_table_data (
	cities varchar(255) NULL,
	city_name varchar(255) NULL,
	geography1 varchar(255) NULL,
	geography2 varchar(255) NULL,
	"views" int4 NULL,
	watch_time_hours numeric(10, 4) NULL,
	avg_view_duration interval NULL
);

CREATE TABLE public.total_views (
	"date" date NULL,
	"views" int4 NULL
);

CREATE TABLE public.content_type_chart_data (
	"Date" varchar(50) NULL,
	"Content type" varchar(50) NULL,
	"Views" int4 NULL
);

CREATE TABLE public.content_type_table_data (
	content_type varchar(255) NULL,
	"views" int4 NULL,
	watch_time_hours numeric(10, 4) NULL,
	avg_view_duration interval NULL
);

CREATE TABLE public.device_type_chart_data (
	"Date" varchar(50) NULL,
	"Device type" varchar(50) NULL,
	"Views" int4 NULL
);

CREATE TABLE public.device_type_table_data (
	device_type varchar(255) NULL,
	"views" int4 NULL,
	watch_time_hours numeric(10, 4) NULL,
	avg_view_duration interval NULL
);

CREATE TABLE public.geography_chart_data (
	"date" date NULL,
	geography varchar(255) NULL,
	"views" int4 NULL
);

CREATE TABLE public.geography_table_data (
	geography varchar(50) NULL,
	"Views" int4 NULL,
	"Watch time (hours)" float4 NULL,
	"Average view duration" varchar(50) NULL
);

CREATE TABLE public.new_returning_viewers_chart_data (
	"Date" varchar(50) NULL,
	"New and returning viewers" varchar(50) NULL,
	"Views" int4 NULL
);

CREATE TABLE public.new_returning_viewers_table_data (
	"New and returning viewers" varchar(50) NULL,
	"Views" int4 NULL,
	"Watch time (hours)" float4 NULL,
	"Average view duration" varchar(50) NULL
);

CREATE TABLE public.operating_system_chart_data (
	"date" date NULL,
	operating_system varchar(255) NULL,
	"views" int4 NULL
);

CREATE TABLE public.operating_system_table_data (
	"Operating system" varchar(50) NULL,
	"Views" int4 NULL,
	"Watch time (hours)" float4 NULL,
	"Average view duration" varchar(50) NULL
);

CREATE TABLE public.sharing_service_chart_data (
	"date" date NULL,
	sharing_service varchar(255) NULL,
	shares int4 NULL
);

CREATE TABLE public.sharing_service_table_data (
	sharing_service varchar(255) NULL,
	shares int4 NULL
);

CREATE TABLE public.sharing_service_totals (
	"Date" varchar(50) NULL,
	shares int4 NULL
);

CREATE TABLE public.subscription_source_chart_data (
	"Date" varchar(50) NULL,
	"Subscription source" varchar(50) NULL,
	subscribers int4 NULL
);

CREATE TABLE public.subscription_source_table_data (
	subscription_source varchar(255) NULL,
	subscribers int4 NULL,
	subscribers_gained int4 NULL,
	subscribers_lost int4 NULL
);

CREATE TABLE public.subscription_source_totals (
	"Date" varchar(50) NULL,
	subscribers int4 NULL
);

CREATE TABLE public.subscription_status_chart_data (
	"Date" varchar(50) NULL,
	"Subscription status" varchar(50) NULL,
	"Views" int4 NULL
);

CREATE TABLE public.subscription_status_table_data (
	subscription_status varchar(255) NULL,
	"views" int4 NULL,
	watch_time_hours numeric(10, 4) NULL,
	avg_view_duration interval NULL
);

CREATE TABLE public.subtitles_chart_data (
	"Date" varchar(50) NULL,
	"Subtitles and CC" varchar(50) NULL,
	"Views" int4 NULL
);

CREATE TABLE public.subtitles_table_data (
	subtitles_and_cc varchar(255) NULL,
	"views" int4 NULL,
	watch_time_hours numeric(10, 4) NULL,
	avg_view_duration interval NULL
);

CREATE TABLE public.traffic_source_chart_data (
	"Date" varchar(50) NULL,
	"Traffic source" varchar(50) NULL,
	"Views" int4 NULL
);

CREATE TABLE public.traffic_source_table_data (
	"Traffic source" varchar(50) NULL,
	"Views" int4 NULL,
	"Watch time (hours)" float4 NULL,
	"Average view duration" varchar(50) NULL,
	impressions int4 NULL,
	"Impressions click-through rate (%)" float4 NULL
);

CREATE TABLE public.viewer_age_table_data (
	"Viewer age" varchar(50) NULL,
	"Views (%)" float4 NULL,
	"Average view duration" varchar(50) NULL,
	"Average percentage viewed (%)" float4 NULL,
	"Watch time (hours) (%)" float4 NULL
);

CREATE TABLE public.viewer_gender_table_data (
	viewer_gender varchar(10) NULL,
	"views" numeric(5, 2) NULL,
	avg_view_duration interval NULL,
	avg_percentage_viewed numeric(5, 2) NULL,
	watch_time_hours_percentage numeric(5, 2) NULL
);

CREATE TABLE public.viewership_by_date_table_data (
	"date" date NULL,
	"views" int4 NULL,
	watch_time_hours numeric(10, 4) NULL,
	avg_view_duration interval NULL
);