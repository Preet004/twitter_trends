from database.mongo import get_db

def store_trends(trend_data):
    db = get_db()
    trends_collection = db.trends
    trends_collection.insert_one(trend_data)

def get_latest_trends():
    db = get_db()
    trends_collection = db.trends
    return trends_collection.find_one(sort=[("timestamp", -1)])
