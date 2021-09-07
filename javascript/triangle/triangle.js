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
    if (
      this.sides.sort()[0] === this.sides.sort()[1] &&
      this.sides.sort()[1] === this.sides.sort()[2]
    ) {
      return 3;
    }

    if (
      this.sides.sort()[0] === this.sides.sort()[1] ||
      this.sides.sort()[1] === this.sides.sort()[2]
    ) {
      return 2;
    }

    return 0;
  }

  get isEquilateral() {
    if (this.isTriangle && this.matchingSides === 3) {
      return true;
    }

    return false;
  }

  get isIsosceles() {
    if ((this.isTriangle && this.matchingSides === 2) || this.isEquilateral) {
      return true;
    }

    return false;
  }

  get isScalene() {
    if (this.isTriangle && this.matchingSides === 0) {
      return true;
    }

    return false;
  }
}
