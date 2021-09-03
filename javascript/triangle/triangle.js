export class Triangle {
  constructor(...sides) {
    this.sides = sides;
    this.a = sides[0];
    this.b = sides[1];
    this.c = sides[2];
  }

  get isTriangle() {
    return (
      this.a + this.b > this.c &&
      this.a + this.c > this.b &&
      this.b + this.c > this.a
    );
  }

  get matchingSides() {
    let isEquilateral = false;

    if (this.a === this.b && this.b === this.c) {
      isEquilateral = true;
    }

    return isEquilateral;
  }

  get sumSides() {
    return this.sides.reduce((sum, curr) => sum + curr);
  }

  get isEquilateral() {
    return this.isTriangle && this.matchingSides;
  }

  get isIsosceles() {
    return this.isTriangle && (this.a === this.b || this.b === this.c || this.a === this.c);
  }

  get isScalene() {
    if (this.isTriangle) {
      return !this.isEquilateral && !this.isIsosceles;
    }

    return false;
  }
}
