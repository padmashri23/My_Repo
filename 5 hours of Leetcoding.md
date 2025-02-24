### OOPS CONCEPT:
```JavaScript
//procedural implementation:
let baseSalary = 30_000;  
let overtime = 10;
let rate = 20;
function getWage(baseSalary, overtime, rate) { //three parameters
    return baseSalary + (overtime * rate);
}
console.log(getWage(baseSalary, overtime, rate));
```
```javascript
//part of one unit
let employee = {
  baseSalary: 30000,  
  overtime: 10,
  rate: 20,
  getWage: function() { //has no parameters
    return this.baseSalary + (this.overtime * this.rate);
  }
};
//part of one unit
console.log(employee.getWage()); 
```
![image](https://github.com/user-attachments/assets/d55f31b1-b8af-4a59-aa27-f2ee9e65737b)
