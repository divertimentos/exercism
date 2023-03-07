/// <reference path="./global.d.ts" />

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */

export function cookingStatus(timeLeft) {
  if (timeLeft > 0) return "Not done, please wait.";
  if (timeLeft === 0) return "Lasagna is done.";
  return "You forgot to set the timer.";
}

export function preparationTime(layers, time) {
  if (time) return layers.length * time;

  return layers.length * 2;
}

export function quantities(layers) {
  let lasagnas = {
    noodles: 0,
    sauce: 0,
  };

  let des = [0, 0];

  layers
    .filter((layer) => layer === "noodles" || layer === "sauce")
    .map((layer) => (layer === "noodles" ? (des[0] += 1) : (des[1] += 1)));

  const [noodles, sauce] = des;

  return { ...lasagnas, noodles: noodles * 50, sauce: sauce * 0.2 };
}

export function addSecretIngredient(friendsList, myList) {
  myList.push(friendsList[friendsList.length - 1]);
}
