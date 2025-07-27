from firebase_setup import db

def search_products_by_name(name_query):
    results = db.collection("products")\
        .where("name", ">=", name_query)\
        .where("name", "<=", name_query + "\uf8ff").stream()
    return [doc.to_dict() for doc in results]

def filter_by_tag(tag):
    results = db.collection("products")\
        .where("tags", "array_contains", tag).stream()
    return [doc.to_dict() for doc in results]

def get_reviews_by_vendor(vendor_id):
    products = db.collection("products").where("vendorId", "==", vendor_id).stream()
    product_ids = [p.id for p in products]
    all_reviews = []
    for pid in product_ids:
        reviews = db.collection("reviews").where("productId", "==", pid).stream()
        all_reviews.extend([r.to_dict() for r in reviews])
    return all_reviews

def get_reviews_by_supplier(supplier_id):
    reviews = db.collection("reviews").where("supplierId", "==", supplier_id).stream()
    return [doc.to_dict() for doc in reviews]
