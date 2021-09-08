export class Triangle {
  constructor(...sides) {
    this.sides = sides;

    [this.a, this.b, this.c] = this.sides.sort();
  }

  get validTriangle() {
    return (
      this.a + this.b > this.c &&
      this.a + this.c > this.b &&
      this.b + this.c > this.a
    );
  }

  get matchingSides() {
    if (this.a === this.b && this.b === this.c) {
      return 3;
    }

    if (this.a === this.b || this.b === this.c) {
      return 2;
    }

    return 0;
  }

  get isEquilateral() {
    return this.validTriangle && this.matchingSides === 3;
  }

  get isIsosceles() {
    return (
      (this.validTriangle && this.matchingSides === 2) || this.isEquilateral
    );
  }

  get isScalene() {
    return this.validTriangle && this.matchingSides === 0;
  }
}
