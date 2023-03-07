// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

/**
 * Determines how long it takes to prepare a certain juice.
 *
 * @param {string} name
 * @returns {number} time in minutes
 */
export function timeToMixJuice(name) {
  switch (name) {
    case "Energizer":
      return 1.5;

    case "Pure Strawberry Joy":
      return 0.5;

    case "Green Garden":
      return 1.5;

    case "Tropical Island":
      return 3;

    case "All or Nothing":
      return 5;

    default:
      return 2.5;
  }
}

/**
 * Calculates the number of limes that need to be cut
 * to reach a certain supply.
 *
 * @param {number} wedgesNeeded
 * @param {string[]} limes
 * @returns {number} number of limes cut
 */

export function limesToCut(wedgesNeeded, limes) {
  // if (wedgesNeeded === 0 || limes.length === 0) return 0;
  if (!wedgesNeeded) return 0;

  const limeSizes = {
    small: 6,
    medium: 8,
    large: 10,
  };

  let remain = wedgesNeeded;

  for (let i = 0; i < limes.length; i++) {
    remain -= limeSizes[limes[i]];

    if (remain <= 0) return i + 1;
  }

  return limes.length;
}

/**
 * Determines which juices still need to be prepared after the end of the shift.
 *
 * @param {number} timeLeft
 * @param {string[]} orders
 * @returns {string[]} remaining orders after the time is up
 */
export function remainingOrders(timeLeft, orders) {
  let juicesForDmitry = [...new Set(orders)];
  let remainingTime = orders.reduce((accOrders, currOrder) => accOrders + timeToMixJuice(currOrder), 0);

  if (timeLeft > remainingTime) return []

  juicesForDmitry.map((order) => {
    if (remainingTime <= 0) juicesForDmitry;

    remainingTime -= timeToMixJuice(order);
    juicesForDmitry.shift();

    return juicesForDmitry

  })

  return juicesForDmitry

}
