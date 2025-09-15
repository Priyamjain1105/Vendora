from app import db
class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20))
    address = db.Column(db.String(255))
    email = db.Column(db.String(100), unique=True, nullable=False)
    pin_code = db.Column(db.String(10))
    vendor_type = db.Column(db.String(50))
    registration_date = db.Column(db.Date)
    total_booking = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone_number": self.phone_number,
            "address": self.address,
            "email": self.email,
            "pin_code": self.pin_code,
            "vendor_type": self.vendor_type,
            "registration_date": self.registration_date.isoformat() if self.registration_date else None,
            "total_booking": self.total_booking
        }
        
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True, nullable=False)
    address = db.Column(db.String(255))
    current_location = db.Column(db.String(255))
    registration_date = db.Column(db.Date)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone_number": self.phone_number,
            "email": self.email,
            "address": self.address,
            "current_location": self.current_location,
            "registration_date": self.registration_date.isoformat() if self.registration_date else None
        }        