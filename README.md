# Padmavathy-Python-Training

## **Day 1:**
**Activity**
1. Write a python program to find maximum of three numbers
2. Write a python program for the following problem statements
 
- **Problem 1:** Calculate the final bill for a food order based on:
   - Order amount
   - Customer type
   - Delivery distance
   - Payment method
  
  **Simplified Rules**
  1. Discount
     - Order ≥ 1000 → 10%
     - Order ≥ 500 → 5%
  2. Prime customer
     - If prime and order ≥ 500 → extra 5%
  3. Delivery charge
     - Distance ≤ 5 km → ₹40
     - Distance > 5 km → ₹70
  4. COD charge
     - If payment is COD and bill < ₹500 → ₹25 extra

- **Probelm 2**

##### Scenario: Smart Electricity Billing System (Advanced)

A power company calculates the **monthly electricity bill** based on the following rules:

#### Inputs

* `units_consumed` (int)
* `is_senior_citizen` (bool)
* `has_solar_panel` (bool)
* `payment_mode` (str → `"online"` or `"offline"`)


#### Billing Rules

1. **Base charge per unit**

   * First **100 units** → ₹3 per unit
   * Next **200 units (101–300)** → ₹5 per unit
   * Above **300 units** → ₹8 per unit

2. **Senior citizen discount**

   * If `is_senior_citizen == True` → **10% discount** on total bill

3. **Solar panel benefit**

   * If `has_solar_panel == True` **AND** units ≤ 250 → **₹500 flat discount**
   * If `has_solar_panel == True` **AND** units > 250 → **₹300 flat discount**

4. **Payment mode surcharge**

   * If `payment_mode == "offline"` **AND** total bill < ₹1000 → **₹50 surcharge**
   * If `payment_mode == "offline"` **AND** total bill ≥ ₹1000 → **₹100 surcharge**
   * No surcharge for `"online"`

5. **Minimum payable amount**

   * Final bill **cannot be less than ₹200**

#### Task

Write a Python program to:

1. Calculate the electricity bill based on the above conditions
2. Apply all discounts and surcharges correctly
3. Ensure minimum payable amount rule is enforced
4. Print the **final bill amount**

#### Use Cases (Test Scenarios)

##### Use Case 1

```python
units_consumed = 180
is_senior_citizen = True
has_solar_panel = True
payment_mode = "online"
```

**Expected Logic**

* Tiered billing (100 + 80 units)
* Senior citizen discount
* Solar discount (≤250 units)
* No surcharge
* Final bill ≥ ₹200

##### Use Case 2

```python
units_consumed = 350
is_senior_citizen = False
has_solar_panel = True
payment_mode = "offline"
```

**Expected Logic**

* Highest slab applied
* Solar discount (>250 units)
* Offline payment surcharge (bill ≥ ₹1000)
* No senior discount


##### Use Case 3

```python
units_consumed = 90
is_senior_citizen = True
has_solar_panel = False
payment_mode = "offline"
```

**Expected Logic**

* Low consumption
* Senior discount
* Offline surcharge (bill < ₹1000)
* Enforce minimum bill ₹200

---

## **Day 2:**
1. Write a python program using class and __init__ for discount problem (alike day 1 problem)
2. Write a python program using class and __init__ for placement eligibility criteria check upon cgpa or %

---

## **Day 3:** 

- Mock Test - [Take Test](https://forms.gle/hDpbYo4rTqwFR6w89)

---

## **Day 4:**

# **Problem Statements – Python OOP (Abstraction, Inheritance, Polymorphism)**

---

## **1. Bank Management System**

### *Objective*
Design a Python program for a **Bank Management System** that demonstrates:

- **Abstraction** using an abstract class *BankAccount*
- **Inheritance** using *SavingsAccount*
- **Encapsulation** by protecting account balance
- **Polymorphism** by overriding the *calculate_interest()* method
- Use of **class** and **constructor**

### *Sample Input*
- **Name:** Ravi  
- **Balance:** 10000  

### *Sample Output*
- **Balance:** 10000  
- **Interest:** 400.0  

---

## **2. Library Management System**

### *Objective*
Create an abstract class **LibraryItem**.  
Derive **Book** and override the issue logic.

### *Input*
- **Book Name:** Python Basics  

### *Output*
- **Book 'Python Basics' issued for 14 days**

---

## **3. Employee Payroll System**

### *Objective*
Create an abstract class **Employee**.  
Derived classes **PermanentEmployee** and **ContractEmployee** override salary calculation.

### *Input*
- **Employee Type:** Permanent  

### *Output*
- **Salary:** 50000  

---

## **4. Vehicle Rental System**

### *Objective*
Create an abstract class **Vehicle**.  
Derived classes **Car** and **Bike** override rent calculation.

### *Input*
- **Vehicle:** Car  
- **Days:** 3  

### *Output*
- **Total Rent:** 3000  

---

## **5. Online Payment System**

### *Objective*
Create an abstract class **Payment**.  
Derived classes **UPI**, **Card**, and **Cash** override the *pay()* method.

### *Input*
- **Payment Mode:** UPI  
- **Amount:** 1500  

### *Output*
- **Paid ₹1500 using UPI**

---

## **6. Hospital Management System**

### *Objective*
Create an abstract class **Patient**.  
Derived class **InPatient** overrides bill calculation.

### *Input*
- **Patient Type:** InPatient  

### *Output*
- **Total Bill:** 20000  

---

## **7. Shape Calculator**

### *Objective*
Create an abstract class **Shape**.  
Derived classes **Rectangle** and **Circle** override the *area()* method.

### *Input*
- **Rectangle:** length = 10, breadth = 5  

### *Output*
- **Area of Rectangle:** 50
