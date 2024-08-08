from quart import Blueprint, jsonify
from models.database import *

data_blueprint = Blueprint('data', __name__)

@data_blueprint.route('/cities_chart_data')
async def get_cities_chart_data():
    data = await CitiesChartData.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/cities_chart_data')
async def get_cities_chart_data():
    data = await CitiesChartData.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/cities_table_data')
async def get_cities_table_data():
    data = await CitiesTableData.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/total_views')
async def get_total_views():
    data = await TotalViews.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/content_type_chart_data')
async def get_content_type_chart_data():
    data = await ContentTypeChartData.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/content_type_table_data')
async def get_content_type_table_data():
    data = await ContentTypeTableData.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/device_type_chart_data')
async def get_device_type_chart_data():
    data = await DeviceTypeChartData.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/device_type_table_data')
async def get_device_type_table_data():
    data = await DeviceTypeTableData.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/geography_chart_data')
async def get_geography_chart_data():
    data = await GeographyChartData.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/geography_table_data')
async def get_geography_table_data():
    data = await GeographyTableData.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/new_returning_viewers_chart_data')
async def get_new_returning_viewers_chart_data():
    data = await NewReturningViewersChartData.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/new_returning_viewers_table_data')
async def get_new_returning_viewers_table_data():
    data = await NewReturningViewersTableData.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/operating_system_chart_data')
async def get_operating_system_chart_data():
    data = await OperatingSystemChartData.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/operating_system_table_data')
async def get_operating_system_table_data():
    data = await OperatingSystemTableData.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/sharing_service_chart_data')
async def get_sharing_service_chart_data():
    data = await SharingServiceChartData.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/sharing_service_table_data')
async def get_sharing_service_table_data():
    data = await SharingServiceTableData.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/sharing_service_totals')
async def get_sharing_service_totals():
    data = await SharingServiceTotals.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/subscription_source_chart_data')
async def get_subscription_source_chart_data():
    data = await SubscriptionSourceChartData.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/subscription_source_table_data')
async def get_subscription_source_table_data():
    data = await SubscriptionSourceTableData.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/subscription_source_totals')
async def get_subscription_source_totals():
    data = await SubscriptionSourceTotals.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/subscription_status_chart_data')
async def get_subscription_status_chart_data():
    data = await SubscriptionStatusChartData.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/subscription_status_table_data')
async def get_subscription_status_table_data():
    data = await SubscriptionStatusTableData.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/subtitles_chart_data')
async def get_subtitles_chart_data():
    data = await SubtitlesChartData.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/subtitles_table_data')
async def get_subtitles_table_data():
    data = await SubtitlesTableData.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/traffic_source_chart_data')
async def get_traffic_source_chart_data():
    data = await TrafficSourceChartData.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/traffic_source_table_data')
async def get_traffic_source_table_data():
    data = await TrafficSourceTableData.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/viewer_age_table_data')
async def get_viewer_age_table_data():
    data = await ViewerAgeTableData.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/viewer_gender_table_data')
async def get_viewer_gender_table_data():
    data = await ViewerGenderTableData.query.all()
    return jsonify([item.serialize() for item in data])

@data_blueprint.route('/viewership_by_date_table_data')
async def get_viewership_by_date_table_data():
    data = await ViewershipByDateTableData.query.all()
    return jsonify([item.serialize() for item in data])