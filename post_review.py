import uuid
from datetime import datetime
from firebase_setup import db

def post_review(product_id, supplier_id, emoji, text, ai_result):
    review_id = str(uuid.uuid4())
    review_data = {
        "productId": product_id,
        "supplierId": supplier_id,
        "emoji": emoji,
        "text": text,
        "sentiment": ai_result["sentiment"],
        "tags": ai_result["tags"],
        "createdAt": datetime.now()
    }
    db.collection("reviews").document(review_id).set(review_data)
    return review_id
