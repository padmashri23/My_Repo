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

```java
import java.util.*;
public class Main{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the Array:");
        int size = scanner.nextInt();
        List<Integer> numbers = new ArrayList<>();
        System.out.print("Enter the elements:");
        for(int i=0;i<size;i++)
        {
            numbers.add(scanner.nextInt());
        }
        boolean found = false;
        for(int i = 0;i<size;i++)
        {
            if(numbers.get(i)==2)
            {
                found = true;
                break;
            }
        }
        if(found)
        {
            System.out.println("True");
        }
        else
        {
            System.out.println("False");
        }
        scanner.close();
    }
}
```
![image](https://github.com/user-attachments/assets/5bf8e8b2-eb8e-43df-a9c0-b4922b435641)

The time complexity of this program can be analyzed as follows:

Reading Input (O(n)):

The for loop:
```java
for (int i = 0; i < size; i++) {
    numbers.add(scanner.nextInt());
}
```
Runs size times (i.e., n times).
Each iteration takes constant time O(1), so the total complexity is O(n).

Searching for 2 (O(n)):
The second for loop:
```java
for (int i = 0; i < size; i++) {
    if (numbers.get(i) == 2) {
        found = true;
        break;
    }
}
```
In the worst case (if 2 is not in the list or is at the end), the loop runs n times.
Best case: If 2 is found early, the loop breaks early (O(1) in best case).
Worst case: O(n).

Printing the Result (O(1)):
The final if condition and System.out.println(...) take constant time O(1).
Overall Time Complexity:
O(n) + O(n) + O(1) = O(n)
Since O(n) dominates, the overall time complexity of the program is O(n).
Best & Worst Case Analysis:
Best Case (O(1)): If 2 is found at the very beginning.

Worst Case (O(n)): If 2 is not found or appears at the end.






