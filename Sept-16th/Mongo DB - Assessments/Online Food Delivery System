use foodDeliveryDB

switched to db foodDeliveryDB


db.customers.insertMany([
{ _id: 1, name: "Rahul Sharma", email: "rahul@example.com", city: "Bangalore" },
{ _id: 2, name: "Priya Singh", email: "priya@example.com", city: "Delhi" },
{ _id: 3, name: "Aman Kumar", email: "aman@example.com", city: "Hyderabad" }
]);
{
  acknowledged: true,
  insertedIds: {
    '0': 1,
    '1': 2,
    '2': 3
  }
}


db.restaurants.insertMany([
{ _id: 101, name: "Spicy Treats", city: "Bangalore", rating: 4.5 },
{ _id: 102, name: "Delhi Biryani House", city: "Delhi", rating: 4.2 },
{ _id: 103, name: "Hyderabad Grill", city: "Hyderabad", rating: 4.7 }
]);
{
  acknowledged: true,
  insertedIds: {
    '0': 101,
    '1': 102,
    '2': 103
  }
}


db.menu.insertMany([
{ _id: 201, restaurant_id: 101, name: "Paneer Tikka", price: 250 },
{ _id: 202, restaurant_id: 101, name: "Veg Biryani", price: 180 },
{ _id: 203, restaurant_id: 102, name: "Chicken Biryani", price: 300 },
{ _id: 204, restaurant_id: 103, name: "Mutton Biryani", price: 400 },
{ _id: 205, restaurant_id: 103, name: "Butter Naan", price: 50 }
]);
{
  acknowledged: true,
  insertedIds: {
    '0': 201,
    '1': 202,
    '2': 203,
    '3': 204,
    '4': 205
  }
}


db.orders.insertMany([
{
_id: 301,
customer_id: 1,
items: [ { menu_id: 201, qty: 2 }, { menu_id: 202, qty: 1 } ],
order_date: ISODate("2025-01-05"),
status: "Delivered"
},
{
_id: 302,
customer_id: 2,
items: [ { menu_id: 203, qty: 1 } ],
order_date: ISODate("2025-01-06"),
status: "Delivered"

},
{
_id: 303,
customer_id: 3,
items: [ { menu_id: 204, qty: 1 }, { menu_id: 205, qty: 3 } ],
order_date: ISODate("2025-01-07"),
status: "Pending"
}
]);
{
  acknowledged: true,
  insertedIds: {
    '0': 301,
    '1': 302,
    '2': 303
  }
}


db.customers.insertOne({
  _id: 4,
  name: "Sneha Iyer",
  email: "sneha@example.com",
  city: "Mumbai"
});
{
  acknowledged: true,
  insertedId: 4
}


db.restaurants.find({ city : "Hyderabad"});
{
  _id: 103,
  name: 'Hyderabad Grill',
  city: 'Hyderabad',
  rating: 4.7
}


db.restaurants.updateOne({name: "Spicy Treats" }, { $set: {rating: 4.8}});
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}


db.menu.deleteOne({name: "Butter Naan"});
{
  acknowledged: true,
  deletedCount: 1
}


db.customers.createIndex({email: 1}, {unique: true});
email_1


db.restaurants.createIndex({city: 1 , rating: -1});
city_1_rating_-1


db.restaurants.getIndexes();
[
  { v: 2, key: { _id: 1 }, name: '_id_' },
  { v: 2, key: { city: 1, rating: -1 }, name: 'city_1_rating_-1' }
]


db.customers.getIndexes();
[
  { v: 2, key: { _id: 1 }, name: '_id_' },
  { v: 2, key: { email: 1 }, name: 'email_1', unique: true }
]


db.restaurants.find({ city: "Bangalore" }).sort({ rating: -1 });
{
  _id: 101,
  name: 'Spicy Treats',
  city: 'Bangalore',
  rating: 4.8
}


db.restaurants.find({ rating: { $gt: 4.5 } });
{
  _id: 101,
  name: 'Spicy Treats',
  city: 'Bangalore',
  rating: 4.8
}
{
  _id: 103,
  name: 'Hyderabad Grill',
  city: 'Hyderabad',
  rating: 4.7
}


db.orders.aggregate([
  {
    $group: {
      _id: "$customer_id",
      totalOrders: { $sum: 1 }
    }
  }
]);
{
  _id: 3,
  totalOrders: 1
}
{
  _id: 1,
  totalOrders: 1
}
{
  _id: 2,
  totalOrders: 1
}


db.orders.aggregate([
  { $unwind: "$items" },
  {
    $lookup: {
      from: "menu",
      localField: "items.menu_id",
      foreignField: "_id",
      as: "menuDetails"
    }
  },
  { $unwind: "$menuDetails" },
  {
    $group: {
      _id: "$menuDetails.restaurant_id",
      totalRevenue: {
        $sum: { $multiply: ["$items.qty", "$menuDetails.price"] }
      }
    }
  }
]);
{
  _id: 102,
  totalRevenue: 300
}
{
  _id: 103,
  totalRevenue: 400
}
{
  _id: 101,
  totalRevenue: 680
}


db.menu.aggregate([
  { $sort: { price: -1 } },
  { $limit: 2 }
]);
{
  _id: 204,
  restaurant_id: 103,
  name: 'Mutton Biryani',
  price: 400
}
{
  _id: 203,
  restaurant_id: 102,
  name: 'Chicken Biryani',
  price: 300
}


db.menu.aggregate([
  {
    $group: {
      _id: "$restaurant_id",
      avgPrice: { $avg: "$price" }
    }
  }
]);
{
  _id: 102,
  avgPrice: 300
}
{
  _id: 101,
  avgPrice: 215
}
{
  _id: 103,
  avgPrice: 400
}


db.orders.aggregate([
  { $match: { status: "Pending" } },
  {
    $lookup: {
      from: "customers",
      localField: "customer_id",
      foreignField: "_id",
      as: "cust"
    }
  },
  { $unwind: "$cust" },
  {
    $group: {
      _id: "$cust.city",
      pendingOrders: { $sum: 1 }
    }
  }
]);
{
  _id: 'Hyderabad',
  pendingOrders: 1
}


db.restaurants.aggregate([
  {
    $sort: { city: 1, rating: -1 }
  },
  {
    $group: {
      _id: "$city",
      topRestaurant: { $first: "$name" },
      topRating: { $first: "$rating" }
    }
  }
]);
{
  _id: 'Bangalore',
  topRestaurant: 'Spicy Treats',
  topRating: 4.8
}
{
  _id: 'Delhi',
  topRestaurant: 'Delhi Biryani House',
  topRating: 4.2
}
{
  _id: 'Hyderabad',
  topRestaurant: 'Hyderabad Grill',
  topRating: 4.7
}


db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customer_id",
      foreignField: "_id",
      as: "cust"
    }
  },
  { $unwind: "$cust" },
  {
    $project: {
      _id: 1,
      order_date: 1,
      status: 1,
      "cust.name": 1,
      "cust.city": 1,
      items: 1
    }
  }
]);
{
  _id: 301,
  items: [
    {
      menu_id: 201,
      qty: 2
    },
    {
      menu_id: 202,
      qty: 1
    }
  ],
  order_date: 2025-01-05T00:00:00.000Z,
  status: 'Delivered',
  cust: {
    name: 'Rahul Sharma',
    city: 'Bangalore'
  }
}
{
  _id: 302,
  items: [
    {
      menu_id: 203,
      qty: 1
    }
  ],
  order_date: 2025-01-06T00:00:00.000Z,
  status: 'Delivered',
  cust: {
    name: 'Priya Singh',
    city: 'Delhi'
  }
}
{
  _id: 303,
  items: [
    {
      menu_id: 204,
      qty: 1
    },
    {
      menu_id: 205,
      qty: 3
    }
  ],
  order_date: 2025-01-07T00:00:00.000Z,
  status: 'Pending',
  cust: {
    name: 'Aman Kumar',
    city: 'Hyderabad'
  }
}


db.orders.aggregate([
  {
    $unwind: "$items"
  },
  {
    $lookup: {
      from: "menu",
      localField: "items.menu_id",
      foreignField: "_id",
      as: "menuDetails"
    }
  },
  { $unwind: "$menuDetails" },
  {
    $lookup: {
      from: "restaurants",
      localField: "menuDetails.restaurant_id",
      foreignField: "_id",
      as: "restDetails"
    }
  },
  { $unwind: "$restDetails" },
  {
    $project: {
      _id: 1,
      order_date: 1,
      status: 1,
      "items.qty": 1,
      "menuDetails.name": 1,
      "menuDetails.price": 1,
      "restDetails.name": 1,
      "restDetails.city": 1
    }
  }
]);
{
  _id: 301,
  items: {
    qty: 2
  },
  order_date: 2025-01-05T00:00:00.000Z,
  status: 'Delivered',
  menuDetails: {
    name: 'Paneer Tikka',
    price: 250
  },
  restDetails: {
    name: 'Spicy Treats',
    city: 'Bangalore'
  }
}
{
  _id: 301,
  items: {
    qty: 1
  },
  order_date: 2025-01-05T00:00:00.000Z,
  status: 'Delivered',
  menuDetails: {
    name: 'Veg Biryani',
    price: 180
  },
  restDetails: {
    name: 'Spicy Treats',
    city: 'Bangalore'
  }
}
{
  _id: 302,
  items: {
    qty: 1
  },
  order_date: 2025-01-06T00:00:00.000Z,
  status: 'Delivered',
  menuDetails: {
    name: 'Chicken Biryani',
    price: 300
  },
  restDetails: {
    name: 'Delhi Biryani House',
    city: 'Delhi'
  }
}
{
  _id: 303,
  items: {
    qty: 1
  },
  order_date: 2025-01-07T00:00:00.000Z,
  status: 'Pending',
  menuDetails: {
    name: 'Mutton Biryani',
    price: 400
  },
  restDetails: {
    name: 'Hyderabad Grill',
    city: 'Hyderabad'
  }
}


db.orders.aggregate([
  { $unwind: "$items" },
  {
    $lookup: {
      from: "menu",
      localField: "items.menu_id",
      foreignField: "_id",
      as: "menuDetails"
    }
  },
  { $unwind: "$menuDetails" },
  {
    $lookup: {
      from: "customers",
      localField: "customer_id",
      foreignField: "_id",
      as: "cust"
    }
  },
  { $unwind: "$cust" },
  {
    $group: {
      _id: "$cust.name",
      dishes: {
        $push: {
          dish: "$menuDetails.name",
          qty: "$items.qty"
        }
      }
    }
  }
]);
{
  _id: 'Aman Kumar',
  dishes: [
    {
      dish: 'Mutton Biryani',
      qty: 1
    }
  ]
}
{
  _id: 'Priya Singh',
  dishes: [
    {
      dish: 'Chicken Biryani',
      qty: 1
    }
  ]
}
{
  _id: 'Rahul Sharma',
  dishes: [
    {
      dish: 'Paneer Tikka',
      qty: 2
    },
    {
      dish: 'Veg Biryani',
      qty: 1
    }
  ]
}


db.orders.aggregate([
  { $unwind: "$items" },
  {
    $lookup: {
      from: "menu",
      localField: "items.menu_id",
      foreignField: "_id",
      as: "menuDetails"
    }
  },
  { $unwind: "$menuDetails" },
  {
    $lookup: {
      from: "restaurants",
      localField: "menuDetails.restaurant_id",
      foreignField: "_id",
      as: "restDetails"
    }
  },
  { $unwind: "$restDetails" },
  { $match: { "restDetails.name": "Hyderabad Grill" } },
  {
    $lookup: {
      from: "customers",
      localField: "customer_id",
      foreignField: "_id",
      as: "cust"
    }
  },
  { $unwind: "$cust" },
  {
    $project: {
      _id: 0,
      customerName: "$cust.name",
      city: "$cust.city"
    }
  }
]);
{
  customerName: 'Aman Kumar',
  city: 'Hyderabad'
}


db.orders.aggregate([
  { $match: { _id: 301 } },
  { $unwind: "$items" },
  {
    $lookup: {
      from: "menu",
      localField: "items.menu_id",
      foreignField: "_id",
      as: "menuDetails"
    }
  },
  { $unwind: "$menuDetails" },
  {
    $project: {
      _id: 0,
      dish: "$menuDetails.name",
      qty: "$items.qty",
      price: "$menuDetails.price",
      total: { $multiply: ["$items.qty", "$menuDetails.price"] }
    }
  }
]);
{
  dish: 'Paneer Tikka',
  qty: 2,
  price: 250,
  total: 500
}
{
  dish: 'Veg Biryani',
  qty: 1,
  price: 180,
  total: 180
}


db.orders.aggregate([
  { $unwind: "$items" },
  {
    $lookup: {
      from: "menu",
      localField: "items.menu_id",
      foreignField: "_id",
      as: "menuDetails"
    }
  },
  { $unwind: "$menuDetails" },
  {
    $group: {
      _id: "$customer_id",
      totalSpent: { $sum: { $multiply: ["$items.qty", "$menuDetails.price"] } }
    }
  },
  { $match: { totalSpent: { $gt: 500 } } },
  {
    $lookup: {
      from: "customers",
      localField: "_id",
      foreignField: "_id",
      as: "cust"
    }
  },
  { $unwind: "$cust" },
  {
    $project: {
      _id: 0,
      customerName: "$cust.name",
      city: "$cust.city",
      totalSpent: 1
    }
  }
]);
{
  totalSpent: 680,
  customerName: 'Rahul Sharma',
  city: 'Bangalore'
}


db.orders.aggregate([
  { $unwind: "$items" },
  {
    $lookup: {
      from: "menu",
      localField: "items.menu_id",
      foreignField: "_id",
      as: "menuDetails"
    }
  },
  { $unwind: "$menuDetails" },
  {
    $group: {
      _id: "$customer_id",
      totalSpent: { $sum: { $multiply: ["$items.qty", "$menuDetails.price"] } }
    }
  },
  {
    $lookup: {
      from: "customers",
      localField: "_id",
      foreignField: "_id",
      as: "cust"
    }
  },
  { $unwind: "$cust" },
  { $match: { "cust.city": "Bangalore" } },
  { $sort: { totalSpent: -1 } },
  { $limit: 1 },
  {
    $project: {
      _id: 0,
      customerName: "$cust.name",
      totalSpent: 1
    }
  }
]);
{
  totalSpent: 680,
  customerName: 'Rahul Sharma'
}


db.orders.aggregate([
  { $unwind: "$items" },
  {
    $lookup: {
      from: "menu",
      localField: "items.menu_id",
      foreignField: "_id",
      as: "menuDetails"
    }
  },
  { $unwind: "$menuDetails" },
  {
    $group: {
      _id: "$menuDetails.restaurant_id",
      totalRevenue: { $sum: { $multiply: ["$items.qty", "$menuDetails.price"] } }
    }
  },
  { $match: { totalRevenue: { $gt: 500 } } },
  {
    $lookup: {
      from: "restaurants",
      localField: "_id",
      foreignField: "_id",
      as: "rest"
    }
  },
  { $unwind: "$rest" },
  {
    $project: {
      _id: 0,
      restaurantName: "$rest.name",
      totalRevenue: 1
    }
  }
]);
{
  totalRevenue: 680,
  restaurantName: 'Spicy Treats'
}


db.orders.aggregate([
  { $unwind: "$items" },
  {
    $lookup: {
      from: "menu",
      localField: "items.menu_id",
      foreignField: "_id",
      as: "menuDetails"
    }
  },
  { $unwind: "$menuDetails" },
  {
    $group: {
      _id: "$order_date",
      dailyRevenue: { $sum: { $multiply: ["$items.qty", "$menuDetails.price"] } }
    }
  },
  { $sort: { _id: 1 } }
]);
{
  _id: 2025-01-05T00:00:00.000Z,
  dailyRevenue: 680
}
{
  _id: 2025-01-06T00:00:00.000Z,
  dailyRevenue: 300
}
{
  _id: 2025-01-07T00:00:00.000Z,
  dailyRevenue: 400
}


db.orders.aggregate([
  { $unwind: "$items" },
  {
    $lookup: {
      from: "menu",
      localField: "items.menu_id",
      foreignField: "_id",
      as: "menuDetails"
    }
  },
  { $unwind: "$menuDetails" },
  {
    $group: {
      _id: "$order_date",
      dailyRevenue: { $sum: { $multiply: ["$items.qty", "$menuDetails.price"] } }
    }
  },
  { $sort: { _id: 1 } }
]);
{
  _id: 2025-01-05T00:00:00.000Z,
  dailyRevenue: 680
}
{
  _id: 2025-01-06T00:00:00.000Z,
  dailyRevenue: 300
}
{
  _id: 2025-01-07T00:00:00.000Z,
  dailyRevenue: 400
}


db.orders.aggregate([
  { $unwind: "$items" },
  {
    $lookup: {
      from: "menu",
      localField: "items.menu_id",
      foreignField: "_id",
      as: "menuDetails"
    }
  },
  { $unwind: "$menuDetails" },
  {
    $group: {
      _id: "$menuDetails.name",
      totalQty: { $sum: "$items.qty" }
    }
  },
  { $sort: { totalQty: -1 } },
  { $limit: 1 }
]);
{
  _id: 'Paneer Tikka',
  totalQty: 2
}
