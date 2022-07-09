import paypayopa
from dotenv import load_dotenv

load_dotenv()

client = paypayopa.Client(auth=("API_KEY", "API_SECRET"), production_mode=False)

client.set_assume_merchant("MERCHANT_ID")

request = {
    "merchantPaymentId": "cb31bcc0-3b6c-46e0-9002-e5c4bb1e3d5f",
    "codeType": "ORDER_QR",
    "redirectUrl": "http://foobar.com",
    "redirectType": "WEB_LINK",
    "orderDescription": "Example - Mune Cake shop",
    "orderItems": [
        {
            "name": "Moon cake",
            "category": "pasteries",
            "quantity": 1,
            "productId": "67678",
            "unitPrice": {
                "amount": 1,
                "currency": "JPY",
            },
        }
    ],
    "amount": {
        "amount": 1,
        "currency": "JPY",
    },
}

client.Code.create_qr_code(request)
