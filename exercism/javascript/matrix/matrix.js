 
class Matrix {
  constructor(string) {
    this.string = string
  }

  rows() {
    let number = parseInt(this.string)
    
    return [number]
  }

  // columns() {
  //   throw new Error("Remove this statement and implement this function");
  // }
}

// m = new Matrix('1')

// console.log(m.rows())