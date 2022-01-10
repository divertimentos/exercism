function funWithArgs(arg1, arg2, arg3) {
  return Object.values(arguments).sort()[0]  
}

// console.log(funWithArgs("UM", "DOIS", "TRES"));
console.log(funWithArgs("Golf", "Agile")); //

// function funcWithParameters(par1, par2, par3) {
//   return arguments; // [Arguments] { '0': 'one', '1': 'two', '2': 'three' }
// }

// console.log(funcWithParameters("one", "two", "three"));
