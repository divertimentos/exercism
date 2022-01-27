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
  let wedges = 0;
  let index = 0;
  while (wedges < wedgesNeeded) {
    switch (limes[index]) {
      case "small":
        wedges += 6;
      case "medium":
        wedges += 8;
      case "large":
        wedges += 10;
      default:
        wedges += 0;
    }
    console.log(
      `Volta nº ${index} | limão: ${limes[index]} | wedges: ${wedges}`
    );

    index += 1;
  }
  return index;

  // limes.forEach((lime, index) => {
  //   console.log("INDEX:", index)
  //   switch (lime) {
  //     case "small":
  //       wedges += 6;
  //     case "medium":
  //       wedges +=8;
  //     case "large":
  //       wedges += 10;
  //   }
  //   return index
  // });
}

/**
 * Determines which juices still need to be prepared after the end of the shift.
 *
 * @param {number} timeLeft
 * @param {string[]} orders
 * @returns {string[]} remaining orders after the time is up
 */
export function remainingOrders(timeLeft, orders) {
  throw new Error("Please implement the remainingOrders function");
}
