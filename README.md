# Interactive Smart E-Commerce System

## 📌 Project Overview
This is a professional Python Terminal (CLI) application developed as part of the Practical Task Assignment. The system simulates a real-world e-commerce experience where users can browse products, manage a shopping cart, and perform a secure checkout with automated discount logic.

## ⚙️ Core Features
- **Dynamic Product Catalog:** Supports both Physical and Digital products.
- **Interactive Shopping Cart:** Users can add items by ID and view their cart neatly.
- **Smart Checkout:** Automatically applies different business rules for discounts and shipping fees based on product type.
- **Robust Error Handling:** Prevents crashes from invalid user inputs using try-except blocks.

## 🛠️ OOP Principles Applied (The Pillars)
To meet the academic requirements, the project strictly follows these four structural conditions:

1. **Abstraction (The Blueprint):** - Utilized the `abc` module to create an abstract base class `Product`. 
   - Forces subclasses to implement `apply_discount()` and `display_info()`.

2. **Inheritance (Specialization):**
   - Created `PhysicalProduct` (adds shipping weight) and `DigitalProduct` (adds download links).

3. **Encapsulation (Data Protection):**
   - Implemented private attributes (e.g., `__price`) to protect sensitive data.
   - Used `@property` decorators and setters for controlled data access and validation.

4. **Polymorphism (Smart Behavior):**
   - The system calls the same `apply_discount()` method for all items in the cart, but each product reacts uniquely (e.g., Digital = 20% off, Physical = 10% off + shipping).
