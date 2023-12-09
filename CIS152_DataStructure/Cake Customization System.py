import tkinter as tk
from tkinter import messagebox
import heapq

# Bakery Item Class
class BakeryItem:
    def __init__(self, item_id, customer_name, item_type):
        self.item_id = item_id
        self.customer_name = customer_name
        self.item_type = item_type

    def prepare(self):
        raise NotImplementedError("Prepare method should be implemented by subclasses.")

    def __str__(self):
        return f"Item ID: {self.item_id}, Customer: {self.customer_name}, Item Type: {self.item_type}"

# Cake Order Class
class CakeOrder(BakeryItem):
    def __init__(self, item_id, customer_name, cake_type, design_preferences, size, special_instructions, urgency=0):
        super().__init__(item_id, customer_name, cake_type)
        self.design_preferences = design_preferences
        self.size = size
        self.special_instructions = special_instructions
        self.urgency = urgency

    def __lt__(self, other):
        # For priority comparison in the priority queue
        return self.urgency < other.urgency

    def prepare(self):
        return f"Preparing {self.item_type}: {self.size}, Design: {self.design_preferences}, Instructions: {self.special_instructions}"

    def __str__(self):
        return super().__str__() + f", Size: {self.size}, Design: {self.design_preferences}, Special Instructions: {self.special_instructions}"

# Customer Class
class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def __str__(self):
        return f"Customer Name: {self.name}, Contact: {self.contact}"

# Customer Manager Class
class CustomerManager:
    def __init__(self):
        self.customers = {}  # Dictionary to store customer information

    def add_customer(self, name, contact):
        if name not in self.customers:
            self.customers[name] = Customer(name, contact)
        else:
            print("Customer already exists.")

    def get_customer_info(self, name):
        return self.customers.get(name, None)

    def display_customers(self):
        for name, customer in self.customers.items():
            print(customer)

# Order Node Class for Linked List
class OrderNode:
    def __init__(self, order):
        self.order = order
        self.next = None

# Order Queue Class
class OrderQueue:
    def __init__(self):
        self.priority_queue = []

    def enqueue(self, order):
        heapq.heappush(self.priority_queue, order)

    def dequeue(self):
        if not self.priority_queue:
            return None
        return heapq.heappop(self.priority_queue)

    def display(self):
        for order in sorted(self.priority_queue):
            print(order)

# Cake Customization System Class
class CakeCustomizationSystem:
    def __init__(self):
        self.orders = []
        self.recipes = {}
        self.customer_manager = CustomerManager()

    def quick_sort_orders(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort_orders(low, pi - 1)
            self.quick_sort_orders(pi + 1, high)

    def partition(self, low, high):
        i = (low - 1)
        pivot = self.orders[high]

        for j in range(low, high):
            if self.orders[j].urgency > pivot.urgency:
                i = i + 1
                self.orders[i], self.orders[j] = self.orders[j], self.orders[i]

        self.orders[i + 1], self.orders[high] = self.orders[high], self.orders[i + 1]
        return (i + 1)

    def delete_order(self, item_id):
        for i, order in enumerate(self.orders):
            if order.item_id == item_id:
                del self.orders[i]
                return True
        return False

    def display_orders(self):
        for order in self.orders:
            print(order)

# Recursive Search Function
def recursive_search(head, item_id):
    if not head:
        return None
    if head.order.item_id == item_id:
        return head.order
    return recursive_search(head.next, item_id)

# GUI Class for Cake Customization System
class CakeCustomizationSystemGUI:
    def __init__(self, root):
        self.ccs = CakeCustomizationSystem()
        self.order_queue = OrderQueue()
        self.root = root
        self.root.title("Cake Customization System")

        # Main Menu
        tk.Button(self.root, text="Place a New Order", command=self.place_order).pack(pady=10)
        tk.Button(self.root, text="Process and Display Orders", command=self.process_display_orders).pack(pady=10)
        tk.Button(self.root, text="Delete an Order", command=self.delete_order_ui).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=10)

    def place_order(self):
        self.order_window = tk.Toplevel(self.root)
        self.order_window.title("Place New Order")

        tk.Label(self.order_window, text="Customer Name:").pack()
        self.customer_name_entry = tk.Entry(self.order_window)
        self.customer_name_entry.pack()

        tk.Label(self.order_window, text="Customer Contact:").pack()
        self.contact_entry = tk.Entry(self.order_window)
        self.contact_entry.pack()

        tk.Label(self.order_window, text="Cake Type:").pack()
        self.cake_type_entry = tk.Entry(self.order_window)
        self.cake_type_entry.pack()

        tk.Label(self.order_window, text="Design Preferences:").pack()
        self.design_preferences_entry = tk.Entry(self.order_window)
        self.design_preferences_entry.pack()

        tk.Label(self.order_window, text="Cake Size:").pack()
        self.size_entry = tk.Entry(self.order_window)
        self.size_entry.pack()

        tk.Label(self.order_window, text="Special Instructions:").pack()
        self.special_instructions_entry = tk.Entry(self.order_window)
        self.special_instructions_entry.pack()

        tk.Label(self.order_window, text="Urgency Level (1-5):").pack()
        self.urgency_entry = tk.Entry(self.order_window)
        self.urgency_entry.pack()

        tk.Button(self.order_window, text="Submit Order", command=self.submit_order).pack(pady=10)

    def submit_order(self):
        customer_name = self.customer_name_entry.get()
        contact = self.contact_entry.get()
        cake_type = self.cake_type_entry.get()
        design_preferences = self.design_preferences_entry.get()
        size = self.size_entry.get()
        special_instructions = self.special_instructions_entry.get()
        urgency = int(self.urgency_entry.get())

        self.ccs.customer_manager.add_customer(customer_name, contact)
        order_id = len(self.ccs.orders) + 1
        new_order = CakeOrder(order_id, customer_name, cake_type, design_preferences, size, special_instructions, urgency)
        self.order_queue.enqueue(new_order)

        self.order_window.destroy()
        messagebox.showinfo("Success", "Order placed successfully")

    def process_display_orders(self):
        while not self.order_queue.priority_queue == []:
            current_order = self.order_queue.dequeue()
            self.ccs.orders.append(current_order)
        self.ccs.quick_sort_orders(0, len(self.ccs.orders) - 1)

        orders_text = "\n".join(str(order) for order in self.ccs.orders)
        messagebox.showinfo("Sorted Orders by Urgency", orders_text)

    def delete_order_ui(self):
        # UI for deleting an order
        self.delete_window = tk.Toplevel(self.root)
        self.delete_window.title("Delete Order")

        tk.Label(self.delete_window, text="Enter Order ID to Delete:").pack()
        self.order_id_entry = tk.Entry(self.delete_window)
        self.order_id_entry.pack()

        tk.Button(self.delete_window, text="Delete Order", command=self.delete_order).pack(pady=10)

    def delete_order(self):
        # Function to delete an order
        order_id = int(self.order_id_entry.get())
        if self.ccs.delete_order(order_id):
            messagebox.showinfo("Success", f"Order {order_id} deleted successfully")
        else:
            messagebox.showinfo("Error", f"Order {order_id} not found")
        self.delete_window.destroy()

# Main Function to Run the Application
def main():
    root = tk.Tk()
    app = CakeCustomizationSystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
