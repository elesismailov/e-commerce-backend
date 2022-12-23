# JSON Formats

- GET `/api/products`
    
    ```json
    [
        {
            "name": "Air Force 1",
            "description": "The legendary Air Force Shoes",
            "slug": "air-force-1",
            "brand": {
                "name": "Nike",
                "description": "The all around the world shoes",
                "slug": "brand-nike-shoes"
            },
            "category": {
                "name": "Running",
                "description": "All men running shoes",
                "slug": "men-running-shoes"
            },
            "in_stock_amount": 12,
            "sold_amount": 1,
            "price": 1234,
            "created_at": "2022-12-05T09:05:27.321045Z",
            "last_modified": "2022-12-05T09:05:27.321055Z"
        }
    ]
    ```
    
- GET `/api/products/product-slug`
    
    ```json
    {
        "name": "Air Force 1",
        "description": "The legendary Air Force Shoes",
        "slug": "nike-air-force-1-shoes-1",
        "brand": {
            "name": "Nike",
            "description": "The all around the world shoes",
            "slug": "brand-nike-shoes"
        },
        "category": {
            "name": "Running",
            "description": "All men running shoes",
            "slug": "men-running-shoes-category"
        },
        "in_stock_amount": 12,
        "sold_amount": 1,
        "price": 1234,
        "created_at": "2022-12-05T09:05:27.321045Z",
        "last_modified": "2022-12-09T05:08:17.777569Z"
    }
    ```
    
- POST `/api/sign-up`
    
    ```json
    {
    	"name": "Be Stoic",
    	"password": "1234",
    	"email": "bestoic@gmail.com",
    	"phone": "+123 456 789"
    }
    ```
    
- POST `/api/log-in`
    
    ```json
    {
    	"email": "bestoic@gmail.com",
    	"password": "1234"
    }
    
    ```
    
    Response
    
    ```json
    {
    	"api_key": "some complicated api_key, still this is not safe, lol",
    	"customer_data": {
    		"name": "Be Stoic",
    		"email": "bestoic@gmail.com",
    		"phone": "+123 456 789",
    		"created_at": "200221-301-241"
    	}
    }
    ```
    
- GET `/api/categories/`
    
    ```json
    {
        "id": 1,
        "name": "Jordan",
        "description": "The legendary basketball shoes.",
        "parent_category_id": null,
        "slug": "jordan"
    }
    ```
    
- GET `/api/categories/<category-slug>/products/`
    
    ```json
    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "name": "Air Force 1",
                "description": "The legendary Air Force Shoes",
                "slug": "nike-air-force-1-shoes-1",
                "brand": {
                    "name": "Nike",
                    "description": "The all around the world shoes",
                    "slug": "brand-nike-shoes"
                },
                "category": {
                    "name": "Running",
                    "description": "All men running shoes",
                    "slug": "men-running-shoes-category"
                },
                "in_stock_amount": 12,
                "sold_amount": 1,
                "price": 1234,
                "created_at": "2022-12-05T09:05:27.321045Z",
                "last_modified": "2022-12-09T05:08:17.777569Z"
            }
        ]
    }
    ```
    
- GET `/api/cart/`
    
    ```json
    {
    	"cart_items": [
    		{
    			"id": 4,
    			"quantity": 1,
    			"created_at": "2022-12-11T09:56:37.672312Z",
    			"product": {
    				"id": 1,
    				"name": "Air Force 1",
    				"description": "The legendary Air Force Shoes",
    				"slug": "nike-air-force-1-1",
    				"in_stock_amount": 12,
    				"sold_amount": 1,
    				"price": 123412,
    				"created_at": "2022-12-05T09:05:27.321045Z",
    				"last_modified": "2022-12-11T09:57:38.098485Z",
    				"brand": {
    					"id": 1,
    					"name": "Nike",
    					"description": "The all around the world shoes",
    					"slug": "brand-nike-shoes"
    				},
    				"category": {
    					"id": 2,
    					"name": "Running",
    					"description": "All men running shoes",
    					"slug": "men-running-shoes-category"
    				}
    			}
    		}
    	]
    }
    ```
    
- POST `/api/cart/`
    
    ```json
    {
    	"product_id": 123,
    	"quantity": 1
    }
    ```
    
- PUT `/api/cart/<cart_item_id>`
    
    ```json
    {
    	"quantity": 5
    }
    ```
    
- DELETE `/api/cart/<cart_item_id>`
- GET `/api/orders/`
    
    ```json
    {
    	"orders": [
    		{
    			"id": 12,
    			"customer_comment": null,
    			"created_at": "2022-12-13T03:40:08.513028Z",
    			"last_modified": "2022-12-13T03:40:08.513037Z",
    			"status_code": {
    				"id": 1,
    				"code": 0,
    				"name": "Awaiting",
    				"description": "Awaiting orders are the orders to be confirmed by the staff member and moved to 1- Taken"
    			}
    		}
    	]
    }
    ```
    
- POST `/api/orders/`
    
    ```json
    {
    	"cart_items": [
    		{"cart_item_id": 4},
    		{"cart_item_id": 5}	
    	]
    }
    ```
    
- GET `/api/orders/<order_id>/`
    
    ```json
    {
    	"order": {
    		"id": 12,
    		"customer_comment": null,
    		"created_at": "2022-12-13T03:40:08.513028Z",
    		"last_modified": "2022-12-13T03:40:08.513037Z",
    		"status_code": {
    			"id": 1,
    			"code": 0,
    			"name": "Awaiting",
    			"description": "Awaiting orders are the orders to be confirmed by the staff member and moved to 1- Taken"
    		}
    	},
    	"order_items": [
    		{
    			"id": 9,
    			"price": 12344,
    			"quantity": 2,
    			"created_at": "2022-12-13T03:40:08.521986Z",
    			"last_modified": "2022-12-13T03:40:08.521994Z",
    			"product": {
    				"id": 1,
    				"name": "Air Force 1",
    				"description": "The legendary Air Force Shoes.",
    				"slug": "nike-air-force-1-none",
    				"in_stock_amount": 2,
    				"sold_amount": 0,
    				"price": 12344,
    				"created_at": "2022-12-11T13:57:09.842646Z",
    				"last_modified": "2022-12-11T13:57:09.842786Z",
    				"brand": {
    					"id": 1,
    					"name": "Nike",
    					"description": "The 10000 dollar logo.",
    					"slug": "brand-nike"
    				},
    				"category": {
    					"id": 1,
    					"name": "Jordan",
    					"description": "The legendary basketball shoes.",
    					"slug": "jordan"
    				}
    			}
    		},
    		{
    			"id": 10,
    			"price": 12344,
    			"quantity": 2,
    			"created_at": "2022-12-13T03:40:08.526624Z",
    			"last_modified": "2022-12-13T03:40:08.526633Z",
    			"product": {
    				"id": 1,
    				"name": "Air Force 1",
    				"description": "The legendary Air Force Shoes.",
    				"slug": "nike-air-force-1-none",
    				"in_stock_amount": 2,
    				"sold_amount": 0,
    				"price": 12344,
    				"created_at": "2022-12-11T13:57:09.842646Z",
    				"last_modified": "2022-12-11T13:57:09.842786Z",
    				"brand": {
    					"id": 1,
    					"name": "Nike",
    					"description": "The 10000 dollar logo.",
    					"slug": "brand-nike"
    				},
    				"category": {
    					"id": 1,
    					"name": "Jordan",
    					"description": "The legendary basketball shoes.",
    					"slug": "jordan"
    				}
    			}
    		}
    	]
    }
    ```
    
- POST `/api/orders/<order_id>/shipment/`

# Admin

- GET `/admin/products`
    
    ```json
    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "name": "Air Force 1",
                "description": "The legendary Air Force Shoes.",
                "slug": "nike-air-force-1-1",
                "in_stock_amount": 2,
                "sold_amount": 0,
                "price": 12344,
                "created_at": "2022-12-11T13:57:09.842646Z",
                "last_modified": "2022-12-13T10:29:12.304641Z",
                "brand": {
                    "id": 1,
                    "name": "Nike",
                    "description": "The 10000 dollar logo.",
                    "slug": "brand-nike"
                },
                "category": {
                    "id": 1,
                    "name": "Jordan",
                    "description": "The legendary basketball shoes.",
                    "slug": "jordan"
                }
            }
        ]
    }
    ```
    
- POST `/admin/products`
    
    ```json
    ~~{
      "name": "Air Forces 1",
      "description": "This is the legendary Original Air Force.",
      "category_id": 1,
      "brand_id": 1,
      "in_stock_amount": 10,
      "sold_amount": 0,
      "price": 123 
    }~~
    
    {
    	"name": "Air Force 1",
    	"description": "The legenedary shoes",
      "category_id": 1,
    	"price": "1234",
      "brand_id": 1
    	"skus": [
    		{
    			"price": "1234",
    			"is_master": true,
    			"variants": {
    				"color": "white"
    				"size": "43"
    			}
    		},
    		{
    			"price": "1239",
    			"is_master": false,
    
    			"variants": {
    				"color": "white"
    				"black": "41"
    			}
    		}
    	]
    }
    ```
    
- GET `/admin/products/<product-slug>`
    
    ```json
    {
        "product": {
            "id": 11,
            "name": "Air Forces 1",
            "description": "This is the legendary Original Air Force.",
            "slug": "nike-air-forces-1-169500999352",
            "in_stock_amount": 10,
            "sold_amount": 0,
            "price": 123,
            "created_at": "2022-12-14T08:32:54.169516Z",
            "last_modified": "2022-12-14T08:32:54.172709Z",
            "brand": {
                "id": 1,
                "name": "Nike",
                "description": "The 10000 dollar logo.",
                "slug": "brand-nike"
            },
            "category": {
                "id": 1,
                "name": "Jordan",
                "description": "The legendary basketball shoes.",
                "slug": "jordan"
            }
        }
    }
    ```
    
- DELETE `/admin/products/<product-slug>`
    
    ```json
    {
        "product": {
            "id": 11,
            "name": "Air Forces 1",
            "description": "This is the legendary Original Air Force.",
            "slug": "nike-air-forces-1-169500999352",
            "in_stock_amount": 10,
            "sold_amount": 0,
            "price": 123,
            "created_at": "2022-12-14T08:32:54.169516Z",
            "last_modified": "2022-12-14T08:32:54.172709Z",
            "brand": {
                "id": 1,
                "name": "Nike",
                "description": "The 10000 dollar logo.",
                "slug": "brand-nike"
            },
            "category": {
                "id": 1,
                "name": "Jordan",
                "description": "The legendary basketball shoes.",
                "slug": "jordan"
            }
        }
    }
    ```
    
- PUT `/admin/products/<product-slug>/`
    
    ```json
    {
      "name": "Air Forces 1",
      "description": "This is the legendary Original Air Force.",
      "category_id": 1,
      "brand_id": 1,
      "in_stock_amount": 10,
      "sold_amount": 0,
      "price": 123,
    
    	"is_active": true,
    
    	"slug": "new-product-slug"
    }
    ```
    

- GET `/admin/categories/`
    
    ```json
    {
        "categories": [
            {
                "id": 1,
                "name": "Jordan",
                "description": "The legendary basketball shoes.",
                "parent_category_id": null,
                "slug": "jordan",
                "created_at": "2022-12-11T13:55:41.455288Z",
                "last_modified": "2022-12-11T13:55:41.455368Z"
            },
            {
                "id": 2,
                "name": "Jordan Signed",
                "description": "The legendary basketball shoes.",
                "parent_category_id": 1,
                "slug": "jordan-jordan-signed",
                "created_at": "2022-12-16T03:51:47.119059Z",
                "last_modified": "2022-12-16T03:51:47.119215Z"
            }
        ]
    }
    ```
    
- POST `/admin/categories/`
    
    ```json
    {
          "name": "Jordan Signed",
          "description": "The legendary basketball shoes.",
          "parent_category_id": 1
    }
    ```
    
- GET, DELETE `/admin/categories/<category-slug>`
    
    GET category
    
    ```json
    {
        "count": 6,
        "next": null,
        "previous": null,
        "results": {
            "category": {
                "id": 1,
                "name": "Jordan",
                "description": "The legendary basketball shoes.",
                "is_active": true,
                "parent_category_id": null,
                "slug": "jordan",
                "created_at": "2022-12-11T13:55:41.455288Z",
                "last_modified": "2022-12-11T13:55:41.455368Z"
            },
            "products": [
                {
                    "id": 1,
                    "name": "Air Force 1",
                    "description": "The legendary Air Force Shoes.",
                    "slug": "nike-air-force-1-1",
                    "in_stock_amount": 2,
                    "sold_amount": 0,
                    "is_active": false,
                    "price": 12344,
                    "created_at": "2022-12-11T13:57:09.842646Z",
                    "last_modified": "2022-12-14T18:00:01.522689Z",
                    "brand": {
                        "id": 1,
                        "name": "Nike",
                        "description": "The 10000 dollar logo.",
                        "slug": "brand-nike"
                    },
                    "category": {
                        "id": 1,
                        "name": "Jordan",
                        "description": "The legendary basketball shoes.",
                        "is_active": true,
                        "parent_category_id": null,
                        "slug": "jordan"
                    }
                }
            ]
        }
    }
    ```
    
- PUT `/admin/categories/<category-slug>`
    
    ```json
    {
    	"slug": "new-url-slug-of-a-category"
    }
    ```
    

- GET `/admin/orders/by-status-code/<status-code-slug>/`
    
    ```json
    {
        "count": 2,
        "next": null,
        "previous": null,
        "results": {
            "count": {
                "0": 2
            },
            "orders": [
                {
                    "id": 12,
                    "customer_comment": null,
                    "created_at": "2022-12-13T03:40:08.513028Z",
                    "last_modified": "2022-12-13T03:40:08.513037Z",
                    "status_code": {
                        "id": 1,
                        "code": 0,
                        "name": "Awaiting",
                        "description": "Awaiting orders are the orders to be confirmed by the staff member and moved to 1- Taken"
                    }
                },
                {
                    "id": 13,
                    "customer_comment": null,
                    "created_at": "2022-12-13T15:19:47.196595Z",
                    "last_modified": "2022-12-13T15:19:47.196604Z",
                    "status_code": {
                        "id": 1,
                        "code": 0,
                        "name": "Awaiting",
                        "description": "Awaiting orders are the orders to be confirmed by the staff member and moved to 1- Taken"
                    }
                }
            ]
        }
    }
    ```
    
- GET `/admin/orders/<order-id>/`
    
    ```json
    {
        "order": {
            "id": 12,
            "customer": {
                "id": 1,
                "name": "Be Stoic",
                "email": "bestoic@gmail.com",
                "phone": "+123 456 789",
                "created_at": "2022-12-11T13:54:12.008163Z"
            },
            "customer_comment": null,
            "created_at": "2022-12-13T03:40:08.513028Z",
            "last_modified": "2022-12-13T03:40:08.513037Z",
            "status_code": {
                "id": 1,
                "code": 0,
                "name": "Awaiting",
                "description": "Awaiting orders are the orders to be confirmed by the staff member and moved to 1- Taken"
            }
        },
        "order_items": [
            {
                "id": 9,
                "price": 12344,
                "quantity": 2,
                "created_at": "2022-12-13T03:40:08.521986Z",
                "last_modified": "2022-12-13T03:40:08.521994Z",
                "product": {
                    "id": 1,
                    "name": "Air Force 1",
                    "description": "The legendary Air Force Shoes.",
                    "slug": "nike-air-force-1-1",
                    "in_stock_amount": 2,
                    "sold_amount": 0,
                    "is_active": false,
                    "price": 12344,
                    "created_at": "2022-12-11T13:57:09.842646Z",
                    "last_modified": "2022-12-14T18:00:01.522689Z",
                    "brand": {
                        "id": 1,
                        "name": "Nike",
                        "description": "The 10000 dollar logo.",
                        "slug": "brand-nike"
                    },
                    "category": {
                        "id": 1,
                        "name": "Jordan",
                        "description": "The legendary basketball shoes.",
                        "is_active": true,
                        "parent_category_id": null,
                        "slug": "jordan"
                    }
                }
            }        
        ]
    }
    ```
    
- PUT `/admin/orders/<order-id>/`
    
    ```json
    { "status_code_id": 12 }
    ```
    

- GET `/admin/status-codes/`
    
    ```json
    {
        "status_codes": [
            {
                "id": 1,
                "code": 0,
                "name": "Awaiting",
                "description": "Awaiting orders are the orders to be confirmed by the staff member and moved to 1- Taken"
            },
            {
                "id": 7,
                "code": 1,
                "name": "Taken",
                "description": "Awaiting orders are the orders to be confirmed by the staff member and moved to 1- Taken"
            }
        ]
    }
    ```
    
- POST `/admin/status-codes/`
    
    ```json
    {
    	"code": 4,
    	"name": "In Delivery",
    	"description": "This status means that your order is in your city and currently being on the way" 
    }
    ```
    
- GET `/admin/status-codes/<ID>/`
    
    ```json
    {
        "status_code": {
            "id": 7,
            "code": 1,
            "name": "Taken",
            "description": "Awaiting orders are the orders to be confirmed by the staff member and moved to 1- Taken"
        }
    }
    ```
    
- PUT `/admin/status-codes/<ID>/`
    
    ```json
    { "code": 3 }
    ```
    
    Provide some field.