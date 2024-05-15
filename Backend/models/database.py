from quart_cors import cors
from quart_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CitiesChartData(db.Model):
    __tablename__ = 'cities_chart_data'
    Date = db.Column(db.String(50), primary_key=True)
    Cities = db.Column(db.String(50))
    CityName = db.Column('City name', db.String(50))
    Views = db.Column(db.Integer)

class CitiesTableData(db.Model):
    __tablename__ = 'cities_table_data'
    Cities = db.Column(db.String(50))
    CityName = db.Column('City name', db.String(50))
    Abbreviation = db.Column(db.String(50))
    Geography = db.Column(db.String(50))
    Views = db.Column(db.Integer)
    WatchTime = db.Column('Watch time (hours)', db.Float)
    AverageViewDuration = db.Column('Average view duration', db.String(50))

class TotalViews(db.Model):
    __tablename__ = 'total_views'
    Date = db.Column(db.String(50), primary_key=True)
    Views = db.Column(db.Integer)

class ContentTypeChartData(db.Model):
    __tablename__ = 'content_type_chart_data'
    Date = db.Column(db.String(50), primary_key=True)
    ContentType = db.Column('Content type', db.String(50))
    Views = db.Column(db.Integer)

class ContentTypeTableData(db.Model):
    __tablename__ = 'content_type_table_data'
    ContentType = db.Column('Content type', db.String(50), primary_key=True)
    Views = db.Column(db.Integer)
    WatchTime = db.Column('Watch time (hours)', db.Float)
    AverageViewDuration = db.Column('Average view duration', db.String(50))

class DeviceTypeChartData(db.Model):
    __tablename__ = 'device_type_chart_data'
    Date = db.Column(db.String(50), primary_key=True)
    DeviceType = db.Column('Device type', db.String(50))
    Views = db.Column(db.Integer)

class DeviceTypeTableData(db.Model):
    __tablename__ = 'device_type_table_data'
    DeviceType = db.Column('Device type', db.String(50), primary_key=True)
    Views = db.Column(db.Integer)
    WatchTime = db.Column('Watch time (hours)', db.Float)
    AverageViewDuration = db.Column('Average view duration', db.String(50))

class GeographyChartData(db.Model):
    __tablename__ = 'geography_chart_data'
    Date = db.Column(db.String(50), primary_key=True)
    Geography = db.Column(db.String(50))
    Views = db.Column(db.Integer)

class GeographyTableData(db.Model):
    __tablename__ = 'geography_table_data'
    Geography = db.Column(db.String(50), primary_key=True)
    Views = db.Column(db.Integer)
    WatchTime = db.Column('Watch time (hours)', db.Float)
    AverageViewDuration = db.Column('Average view duration', db.String(50))

class NewReturningViewersChartData(db.Model):
    __tablename__ = 'new_returning_viewers_chart_data'
    Date = db.Column(db.String(50), primary_key=True)
    NewReturningViewers = db.Column('New and returning viewers', db.String(50))
    Views = db.Column(db.Integer)

class NewReturningViewersTableData(db.Model):
    __tablename__ = 'new_returning_viewers_table_data'
    NewReturningViewers = db.Column('New and returning viewers', db.String(50), primary_key=True)
    Views = db.Column(db.Integer)
    WatchTime = db.Column('Watch time (hours)', db.Float)
    AverageViewDuration = db.Column('Average view duration', db.String(50))

class OperatingSystemChartData(db.Model):
    __tablename__ = 'operating_system_chart_data'
    Date = db.Column(db.String(50), primary_key=True)
    OperatingSystem = db.Column('Operating system', db.String(50))
    Views = db.Column(db.Integer)

class OperatingSystemTableData(db.Model):
    __tablename__ = 'operating_system_table_data'
    OperatingSystem = db.Column('Operating system', db.String(50), primary_key=True)
    Views = db.Column(db.Integer)
    WatchTime = db.Column('Watch time (hours)', db.Float)
    AverageViewDuration = db.Column('Average view duration', db.String(50))

class SharingServiceChartData(db.Model):
    __tablename__ = 'sharing_service_chart_data'
    Date = db.Column(db.String(50), primary_key=True)
    SharingService = db.Column('Sharing service', db.String(50))
    Shares = db.Column(db.Integer)

class SharingServiceTableData(db.Model):
    __tablename__ = 'sharing_service_table_data'

    sharing_service = db.Column(db.String(50), nullable=True)
    shares = db.Column(db.Integer, nullable=True)

class SharingServiceTotals(db.Model):
    __tablename__ = 'sharing_service_totals'

    date = db.Column(db.String(50), nullable=True)
    shares = db.Column(db.Integer, nullable=True)

class SubscriptionSourceChartData(db.Model):
    __tablename__ = 'subscription_source_chart_data'

    date = db.Column(db.String(50), nullable=True)
    subscription_source = db.Column(db.String(50), nullable=True)
    subscribers = db.Column(db.Integer, nullable=True)

class SubscriptionSourceTableData(db.Model):
    __tablename__ = 'subscription_source_table_data'

    subscription_source = db.Column(db.String(50), nullable=True)
    subscribers = db.Column(db.Integer, nullable=True)
    subscribers_gained = db.Column(db.Integer, nullable=True)
    subscribers_lost = db.Column(db.Integer, nullable=True)

class SubscriptionSourceTotals(db.Model):
    __tablename__ = 'subscription_source_totals'

    date = db.Column(db.String(50), nullable=True)
    subscribers = db.Column(db.Integer, nullable=True)


class SubscriptionStatusChartData(db.Model):
    __tablename__ = 'subscription_status_chart_data'

    date = db.Column(db.String(50), nullable=True)
    subscription_status = db.Column(db.String(50), nullable=True)
    views = db.Column(db.Integer, nullable=True)

class SubscriptionStatusTableData(db.Model):
    __tablename__ = 'subscription_status_table_data'

    subscription_status = db.Column(db.String(50), nullable=True)
    views = db.Column(db.Integer, nullable=True)
    watch_time_hours = db.Column(db.Float, nullable=True)
    average_view_duration = db.Column(db.String(50), nullable=True)

class SubtitlesChartData(db.Model):
    __tablename__ = 'subtitles_chart_data'

    date = db.Column(db.String(50), nullable=True)
    subtitles_and_cc = db.Column(db.String(50), nullable=True)
    views = db.Column(db.Integer, nullable=True)

class SubtitlesTableData(db.Model):
    __tablename__ = 'subtitles_table_data'

    subtitles_and_cc = db.Column(db.String(50), nullable=True)
    views = db.Column(db.Integer, nullable=True)
    watch_time_hours = db.Column(db.Float, nullable=True)
    average_view_duration = db.Column(db.String(50), nullable=True)

class TrafficSourceChartData(db.Model):
    __tablename__ = 'traffic_source_chart_data'

    date = db.Column(db.String(50), nullable=True)
    traffic_source = db.Column(db.String(50), nullable=True)
    views = db.Column(db.Integer, nullable=True)

class TrafficSourceTableData(db.Model):
    __tablename__ = 'traffic_source_table_data'

    traffic_source = db.Column(db.String(50), nullable=True)
    views = db.Column(db.Integer, nullable=True)
    watch_time_hours = db.Column(db.Float, nullable=True)
    average_view_duration = db.Column(db.String(50), nullable=True)
    impressions = db.Column(db.Integer, nullable=True)
    impressions_click_through_rate = db.Column(db.Float, nullable=True)

class ViewerAgeTableData(db.Model):
    __tablename__ = 'viewer_age_table_data'

    viewer_age = db.Column(db.String(50), nullable=True)
    views_percentage = db.Column(db.Float, nullable=True)
    average_view_duration = db.Column(db.String(50), nullable=True)
    average_percentage_viewed = db.Column(db.Float, nullable=True)
    watch_time_hours_percentage = db.Column(db.Float, nullable=True)

class ViewerGenderTableData(db.Model):
    __tablename__ = 'viewer_gender_table_data'

    viewer_gender = db.Column(db.String(50), nullable=True)
    views_percentage = db.Column(db.Float, nullable=True)
    average_view_duration = db.Column(db.String(50), nullable=True)
    average_percentage_viewed = db.Column(db.Float, nullable=True)
    watch_time_hours_percentage = db.Column(db.Float, nullable=True)

class ViewershipByDateTableData(db.Model):
    __tablename__ = 'viewership_by_date_table_data'

    date = db.Column(db.String(50), nullable=True)
    views = db.Column(db.Integer, nullable=True)
    watch_time_hours = db.Column(db.Float, nullable=True)
    average_view_duration = db.Column(db.String(50), nullable=True)
