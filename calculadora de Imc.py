import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de IMC")
        self.create_widgets()
    
    def create_widgets(self):
        self.height_label = tk.Label(self.root, text="Altura (m):")
        self.height_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.height_entry = tk.Entry(self.root)
        self.height_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.weight_label = tk.Label(self.root, text="Peso (kg):")
        self.weight_label.grid(row=1, column=0, padx=10, pady=10)
        
        self.weight_entry = tk.Entry(self.root)
        self.weight_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.calculate_button = tk.Button(self.root, text="Calcular IMC", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
        self.result_label = tk.Label(self.root, text="IMC:")
        self.result_label.grid(row=3, column=0, padx=10, pady=10)
        
        self.result_value = tk.Label(self.root, text="")
        self.result_value.grid(row=3, column=1, padx=10, pady=10)
    
    def calculate_bmi(self):
        try:
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            
            if height <= 0 or weight <= 0:
                raise ValueError("Altura e peso devem ser positivos.")
            
            bmi = weight / (height ** 2)
            self.result_value.config(text=f"{bmi:.2f}")
            self.show_bmi_category(bmi)
        except ValueError as e:
            messagebox.showerror("Erro de entrada", f"Insira valores válidos para altura e peso.\n{e}")
    
    def show_bmi_category(self, bmi):
        if bmi < 18.5:
            category = "Abaixo do peso"
        elif 18.5 <= bmi < 24.9:
            category = "Peso ideal"
        elif 25 <= bmi < 29.9:
            category = "Sobrepeso"
        else:
            category = "Obesidade"
        
        messagebox.showinfo("Categoria de IMC", f"Seu IMC é {bmi:.2f}, que está na categoria: {category}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
