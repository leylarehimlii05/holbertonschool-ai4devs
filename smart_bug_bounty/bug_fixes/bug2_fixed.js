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

module.exports = { calculateCartTotal };
