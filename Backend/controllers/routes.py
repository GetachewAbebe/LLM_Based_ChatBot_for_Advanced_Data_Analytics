from quart import Blueprint, request, jsonify
from backend.models.database import connect_to_db, store_data

bp = Blueprint('routes', __name__)

@bp.route('/store_data', methods=['POST'])
async def store_data_route():
    data = await request.json()
    conn = await connect_to_db()
    success = await store_data(conn, data)
    await conn.close()
    if success:
        return jsonify({'message': 'Data stored successfully'}), 200
    else:
        return jsonify({'message': 'Failed to store data'}), 500
