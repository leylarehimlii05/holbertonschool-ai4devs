async function calculateCartTotal(cartItems, fetchDiscountRate) {
  const lineTotals = await Promise.all(
    cartItems.map(async (item) => {
      const discount = await fetchDiscountRate(item.category);
      const discountedPrice = item.price * (1 - discount);
      return discountedPrice * item.quantity;
    })
  );

  const subtotal = lineTotals.reduce((sum, value) => sum + value, 0);
  return Math.round(subtotal * 100) / 100;
}

// Validation tests
(async () => {
  const mockRates = { books: 0.1, electronics: 0.2 };
  const mockFetch = async (cat) => mockRates[cat] || 0;

  const items = [
    { category: "books", price: 19.99, quantity: 1 },
    { category: "electronics", price: 5.5, quantity: 1 },
  ];

  const total = await calculateCartTotal(items, mockFetch);
  console.assert(total === 22.39, `Expected 22.39, got ${total}`);

  const emptyTotal = await calculateCartTotal([], mockFetch);
  console.assert(emptyTotal === 0, `Expected 0, got ${emptyTotal}`);
  console.log("bug2_fixed.js: All test cases passed!");
})();

module.exports = { calculateCartTotal };
