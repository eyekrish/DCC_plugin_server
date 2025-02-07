import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QInputDialog, QMessageBox

class InventoryApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Inventory Management")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.inventory_list = QListWidget()
        layout.addWidget(self.inventory_list)

        self.refresh_button = QPushButton("Refresh Inventory")
        self.refresh_button.clicked.connect(self.load_inventory)
        layout.addWidget(self.refresh_button)

        self.add_button = QPushButton("Add Item")
        self.add_button.clicked.connect(self.add_item)
        layout.addWidget(self.add_button)

        self.remove_button = QPushButton("Remove Item")
        self.remove_button.clicked.connect(self.remove_item)
        layout.addWidget(self.remove_button)

        self.setLayout(layout)
        self.load_inventory()

    def load_inventory(self):
        try:
            response = requests.get("http://127.0.0.1:8000/inventory")
            data = response.json()
            self.inventory_list.clear()
            for item in data["inventory"]:
                self.inventory_list.addItem(f"{item['name']} - {item['quantity']}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load inventory: {str(e)}")

    def add_item(self):
        name, ok = QInputDialog.getText(self, "Add Item", "Enter item name:")
        if not ok or not name:
            return

        quantity, ok = QInputDialog.getInt(self, "Add Item", "Enter quantity:")
        if not ok:
            return

        try:
            requests.post(f"http://127.0.0.1:8000/add-item?name={name}&quantity={quantity}")
            self.load_inventory()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to add item: {str(e)}")

    def remove_item(self):
        selected_item = self.inventory_list.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "Warning", "Select an item to remove.")
            return

        name = selected_item.text().split(" - ")[0]

        try:
            requests.delete(f"http://127.0.0.1:8000/remove-item?name={name}")
            self.load_inventory()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to remove item: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryApp()
    window.show()
    sys.exit(app.exec_())
