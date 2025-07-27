from firebase_setup import db

def seed_users():
    db.collection("vendors").document("vendor123").set({
        "name": "Test Vendor",
        "email": "vendor@demo.com",
        "role": "vendor"
    })

    db.collection("suppliers").document("supplier456").set({
        "name": "Test Supplier",
        "email": "supplier@demo.com",
        "role": "supplier"
    })
