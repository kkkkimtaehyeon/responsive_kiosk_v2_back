DUMMY_ANSWER_CART_DATA = {
    "isMenu": True,
    "isOrder": False,
    "isAnswer": True,
    "content": {
        "answer": "아메리카노를 추가하셨습니다.",
        "menus": {
                "id": "667cf9d8bf0cbc39cdf4ced1",
                "name": "아메리카노",
                "price": 3000,
                "amount": 1,
            }
    }
}
# 카트에 있는 메뉴로 주문 접수
DUMMY_ANSWER_ORDER_DATA = {
    "isMenu": False,
    "isOrder": True,
    "isAnswer": True,
    "content": {
        "answer": "주문이 완료되었습니다.",
        "menus": {}
    }
}

DUMMY_ORDER_REQUEST = {
    "order_takeout": True,
    "order_details": [
        {
            "order_menu_id": "1",
            "order_menu_name": "name",
            "order_menu_amount": 1,
            "order_menu_price": 3000
        },
        {
            "order_menu_id": "2",
            "order_menu_name": "name",
            "order_menu_amount": 1,
            "order_menu_price": 3000
        }
    ]
}
