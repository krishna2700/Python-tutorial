class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected=True
        
    def __str__(self):
        return f"{self.name} ({self.connected_by})"
    
    def disconnect(self): 
        self.connected = False 
        return f"{self.name} is disconnected" 
    

printer = Device("Printer", "USB")
print(printer)  # This will print the device object using the __str__ method
print(printer.disconnect())  # This will print the disconnect message    


class Printer(Device):
    def __init__(self, name, connected_by,capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity


    def __str__(self):
        return f"{super().__str__()}  ({self.remaining_pages} pages remaining)"    
    
    def print(self,pages):
        if not self.connected:
            print (f"{self.name} is not connected. Please connect the printer first.")
            return
        print(f"printing {pages} pages")
        self.remaining_pages -= pages


printer = Printer("Printer", "USB", 100) # Create a Printer instance
print(printer)  # This will print the printer object using the __str__ method
printer.print(10)  # This will print the print message
print(printer)  # This will print the printer object again to show remaining pages   
printer.disconnect()  # Disconnect the printer
print(printer)  # This will print the printer object again to show that it is disconnected     
printer.print(10)  # This will print a message indicating that the printer is not connected