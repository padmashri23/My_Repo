### OOPS CONCEPT:

### ENCAPSULATION
```JavaScript
//procedural implementation:-- variables on one side and functions on the other side 
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

![image](https://github.com/user-attachments/assets/ed3a1b9b-24fc-4bf9-a3a5-2710e1edddfa)

![image](https://github.com/user-attachments/assets/8fdf981d-fcc6-4fdd-b309-d65893ca268d)

![image](https://github.com/user-attachments/assets/5554fcf4-808c-445a-9234-1a5319e73b4c)




