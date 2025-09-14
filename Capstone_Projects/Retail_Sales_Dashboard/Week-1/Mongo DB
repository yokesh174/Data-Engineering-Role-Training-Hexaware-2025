use retailDB

switched to db retailDB

// Insert 20+ Campaign Feedback Records
db.campaignFeedback.insertMany([
  { campaign_id: 1, store_id: 1, campaign_name: "Diwali Sale", feedback: "Huge customer turnout, sales boosted", rating: 5 },
  { campaign_id: 2, store_id: 2, campaign_name: "New Year Sale", feedback: "Average participation, need better marketing", rating: 3 },
  { campaign_id: 3, store_id: 3, campaign_name: "Summer Bonanza", feedback: "Loved by young crowd", rating: 4 },
  { campaign_id: 4, store_id: 4, campaign_name: "Christmas Sale", feedback: "Great response, huge crowd", rating: 5 },
  { campaign_id: 5, store_id: 5, campaign_name: "Independence Day Offer", feedback: "Low participation", rating: 2 },
  { campaign_id: 6, store_id: 6, campaign_name: "Republic Day Sale", feedback: "Steady response", rating: 4 },
  { campaign_id: 7, store_id: 7, campaign_name: "Clearance Sale", feedback: "Customers bought bulk items", rating: 5 },
  { campaign_id: 8, store_id: 8, campaign_name: "Festive Sale", feedback: "Good but limited reach", rating: 3 },
  { campaign_id: 9, store_id: 9, campaign_name: "Back to School", feedback: "Parents loved discounts on stationery", rating: 4 },
  { campaign_id: 10, store_id: 10, campaign_name: "Mega Electronics Sale", feedback: "Huge spike in electronics sales", rating: 5 },
  { campaign_id: 11, store_id: 1, campaign_name: "Monsoon Offers", feedback: "Mixed reviews, good raincoats sales", rating: 3 },
  { campaign_id: 12, store_id: 2, campaign_name: "Valentine’s Day Sale", feedback: "Jewelry and perfumes sold well", rating: 4 },
  { campaign_id: 13, store_id: 3, campaign_name: "Flash Friday Sale", feedback: "Customers rushed for offers", rating: 5 },
  { campaign_id: 14, store_id: 4, campaign_name: "Eid Sale", feedback: "Moderate response", rating: 3 },
  { campaign_id: 15, store_id: 5, campaign_name: "Ganesh Chaturthi Sale", feedback: "Festive items sold well", rating: 4 },
  { campaign_id: 16, store_id: 6, campaign_name: "Navratri Sale", feedback: "Great crowd turnout", rating: 5 },
  { campaign_id: 17, store_id: 7, campaign_name: "Black Friday", feedback: "One of the best sales, record revenue", rating: 5 },
  { campaign_id: 18, store_id: 8, campaign_name: "Pongal Sale", feedback: "Good in South India region", rating: 4 },
  { campaign_id: 19, store_id: 9, campaign_name: "Children’s Day Offers", feedback: "Kids’ items sold out quickly", rating: 5 },
  { campaign_id: 20, store_id: 10, campaign_name: "Winter Clearance", feedback: "Discounted jackets were popular", rating: 4 }
]);

{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('68c66fe4b93510fc962d8b2e'),
    '1': ObjectId('68c66fe4b93510fc962d8b2f'),
    '2': ObjectId('68c66fe4b93510fc962d8b30'),
    '3': ObjectId('68c66fe4b93510fc962d8b31'),
    '4': ObjectId('68c66fe4b93510fc962d8b32'),
    '5': ObjectId('68c66fe4b93510fc962d8b33'),
    '6': ObjectId('68c66fe4b93510fc962d8b34'),
    '7': ObjectId('68c66fe4b93510fc962d8b35'),
    '8': ObjectId('68c66fe4b93510fc962d8b36'),
    '9': ObjectId('68c66fe4b93510fc962d8b37'),
    '10': ObjectId('68c66fe4b93510fc962d8b38'),
    '11': ObjectId('68c66fe4b93510fc962d8b39'),
    '12': ObjectId('68c66fe4b93510fc962d8b3a'),
    '13': ObjectId('68c66fe4b93510fc962d8b3b'),
    '14': ObjectId('68c66fe4b93510fc962d8b3c'),
    '15': ObjectId('68c66fe4b93510fc962d8b3d'),
    '16': ObjectId('68c66fe4b93510fc962d8b3e'),
    '17': ObjectId('68c66fe4b93510fc962d8b3f'),
    '18': ObjectId('68c66fe4b93510fc962d8b40'),
    '19': ObjectId('68c66fe4b93510fc962d8b41')
  }
}

// 1. Index on campaign name
db.campaignFeedback.createIndex({ campaign_name: 1 });
campaign_name_1

// 2. Text index on feedback
db.campaignFeedback.createIndex({ feedback: "text" });
feedback_text

// 3. Index by store
db.campaignFeedback.createIndex({ store_id: 1 });
store_id_1

// 4. Index by rating
db.campaignFeedback.createIndex({ rating: 1 });
rating_1

// 5. Compound index store + campaign
db.campaignFeedback.createIndex({ store_id: 1, campaign_name: 1 });
store_id_1_campaign_name_1

