from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pymysql
import pymongo

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MYSQL_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'meesho',
}

MONGO_URI = "mongodb://localhost:27017"
MONGO_DB_NAME = "migration"

mongo_client = pymongo.MongoClient(MONGO_URI)
mongo_db = mongo_client[MONGO_DB_NAME]

@app.post("/CountryMigrate")
async def country_migrate():
    try:
        mysql_conn = pymysql.connect(**MYSQL_CONFIG)
        cursor = mysql_conn.cursor(pymysql.cursors.DictCursor)
        query="""
                SELECT 
                    s.state_id, 
                    s.state_name, 
                    c.country_id, 
                    c.country_name,
                    d.district_id,
                    d.district_name
                FROM 
                    country c
                LEFT JOIN 
                    state s ON s.country_id = c.country_id
                LEFT JOIN 
                    district d ON s.state_id = d.state_id"""
        cursor.execute(query)
        result = cursor.fetchall()
      
        country_collection = mongo_db['country']
        
        for row in result:
            country_document = {
                "country_id": row['country_id'],
                "country_name": row['country_name'],
                "state": [{
                    "state_id": row['state_id'],
                    "state_name": row['state_name'],
                    "district":[{
                        "district_id": row['district_id'],
                        "district_name": row['district_name']
                        }]
                    }
                    ]
            }
            country_collection.insert_one(country_document)

        cursor.close()
        mysql_conn.close()

        return {"message": "Data migration completed successfully!"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/stop_migrate")
async def stop_migrate():
    return {"message": "Data migration stopped successfully!"}


@app.post("/ProductMigrate")
async def product_migrate():
    try:
        mysql_conn = pymysql.connect(**MYSQL_CONFIG)
        cursor = mysql_conn.cursor(pymysql.cursors.DictCursor)
        query="""
                SELECT 
                    p.product_id, 
                    p.product_name, 
                    p.product_image, 
                    p.product_price,
                    p.description,
                    c.category_id,
                    c.category_name
                FROM 
                    products p
                LEFT JOIN 
                    category c ON p.category_id = c.category_id
                """
        cursor.execute(query)
        result = cursor.fetchall()
      
        product_collection = mongo_db['product']
        
        for row in result:
            product_document = {
                "product_id": row['product_id'],
                "product_name": row['product_name'],
                "product_image": row['product_image'],
                "product_price": row['product_price'],
                "description": row['description'],
                "category":[{
                    "category_id": row['category_id'],
                    "category_name": row['category_name']
                }]
            }
            product_collection.insert_one(product_document)

        cursor.close()
        mysql_conn.close()

        return {"message": "Data migration completed successfully!"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
