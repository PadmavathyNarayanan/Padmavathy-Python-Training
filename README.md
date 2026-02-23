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
