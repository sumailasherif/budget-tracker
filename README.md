# **Budget Tracker**

## **Project Overview**
This Budget Tracker application was developed as part of the **Week 7 Formative Assessment for Programming 1**.  
The task involved building a **menu-driven Python program** that allows users to:

- Record income and expenses  
- View all transactions  
- Filter transaction data  
- Generate a financial summary  

The project demonstrates key programming concepts taught in class, including:

- Functions  
- Loops and conditionals  
- Input validation  
- Collections  
- Object-Oriented Programming (OOP) with inheritance  

The program runs entirely in the terminal, storing data in memory during runtime. Its structured interface helps users track financial activity within a single session.

---

## **Key Features**
- **Add Transactions** (Income or Expense)  
- **List All Transactions** in a clean formatted view  
- **Filter Transactions** by:
  - Type  
  - Category  
  - Month (YYYY-MM)  
- **View Summary** including:
  - Total income  
  - Total expenses  
  - Balance  
  - Category totals  
- **Input Validation** for dates, amounts, and menu selections  
- **OOP Design** using:
  - `Transaction`  
  - `Income`  
  - `Expense` classes  

---

## **How to Run the Program**

### **1. Ensure Python 3 is installed**
Check using:
```
python --version
````

### **2. Clone the project repository**

```
git clone https://github.com/sumailasherif/budget-tracker
```

### **3. Navigate into the project directory**

```
cd budget-tracker
```

### **4. Run the program**

```
python main.py
```

### **5. Follow the on-screen menu instructions**

---

## **Menu Structure**

The main program menu provides the following options:

```
1) Add Income
2) Add Expense
3) List Transactions
4) Filter Transactions
5) Show Summary
6) Exit
```

---

## **Additional Notes**

### **Key Learnings**

* Applying OOP principles in Python
* Designing a user-friendly CLI interface
* Implementing strong input validation
* Managing data using custom classes and lists

### **Challenges Encountered**

* Ensuring correct date/amount validation
* Maintaining clean, readable CLI formatting
* Handling edge cases in filtering and summaries

### **Future Enhancements**

* Save and load data using CSV or JSON
* Improve the formatting of tables in the terminal
* Add automated tests
* Implement an undo feature
* Introduce color-coded CLI output

---

## **Author**

[**Sherif Sumaila**](https://github.com/sumailasherif)