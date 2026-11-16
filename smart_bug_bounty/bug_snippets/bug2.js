async function calculateCartTotal(cartItems, fetchDiscountRate) {
  let subtotal = 0;

  // Bug 1: Array.prototype.forEach does not await async callbacks
  cartItems.forEach(async (item) => {
    const discount = await fetchDiscountRate(item.category);
    const discountedPrice = item.price * (1 - discount);
    subtotal += discountedPrice * item.quantity;
  });

  // Bug 2: Runs before async callbacks complete and lacks rounding for currency
  return subtotal;
}

module.exports = { calculateCartTotal };
