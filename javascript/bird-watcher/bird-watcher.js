// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

/**
 * Calculates the total bird count.
 *
 * @param {number[]} birdsPerDay
 * @returns {number} total bird count
 */
export function totalBirdCount(birdsPerDay) {
  let birdSum = 0;
  birdsPerDay.map((bird) => (birdSum += bird));
  return birdSum;
}

/**
 * Calculates the total number of birds seen in a specific week.
 *
 * @param {number[]} birdsPerDay
 * @param {number} week
 * @returns {number} birds counted in the given week
 */
export function birdsInWeek(birdsPerDay, week) {
  // const dynamicWeek = week <= 1 ? 1 : week;
  // const dynamicBeginning = week <= 1 ? 0 : (week * 7) / 2;
  // console.dir("ARRAY:", birdsPerDay);
  // console.log(
  //   "SLICE ITSELF:",
  //   birdsPerDay.slice(
  //     dynamicWeek,
  //   )
  // );
  // console.log("LENGTH:", birdsPerDay.length);
  // console.log("SLICE:", birdsPerDay.length - week * 7);
  // console.log("SLICE END:", birdsPerDay.length - week * 7 + 7);
  if (birdsPerDay.length <= 7) {
    return totalBirdCount(birdsPerDay);
  } else {
    return totalBirdCount(
      birdsPerDay.slice(
        7 * week - 7 - birdsPerDay.length,
        7 * week - 7 - birdsPerDay.length + 7
      )
    );
  }
}

/**
 * Fixes the counting mistake by increasing the bird count
 * by one for every second day.
 *
 * @param {number[]} birdsPerDay
 * @returns {number[]} corrected bird count data
 */
export function fixBirdCountLog(birdsPerDay) {
  birdsPerDay.forEach((_, index) => {
    if (index % 2 === 0) {
      birdsPerDay[index]++;
    }
  });
  return birdsPerDay;
}
