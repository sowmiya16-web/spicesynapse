import uuid
from datetime import datetime
from firebase_setup import db, bucket

def upload_image(file_path, file_name=None):
    if not file_name:
        file_name = str(uuid.uuid4())
    blob = bucket.blob(f"products/{file_name}")
    blob.upload_from_filename(file_path)
    blob.make_public()
    return blob.public_url

def create_product(vendor_id, name, description, image_path, ai_data):
    image_url = upload_image(image_path)
    product_id = str(uuid.uuid4())
    product_data = {
        "vendorId": vendor_id,
        "name": name,
        "description": description,
        "imageUrl": image_url,
        "tags": ai_data.get("tags", []),
        "trustScore": ai_data.get("trust_score", 50),
        "sentiment": ai_data.get("sentiment", "neutral"),
        "createdAt": datetime.now()
    }
    db.collection("products").document(product_id).set(product_data)
    return product_id
