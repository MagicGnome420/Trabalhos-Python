import tkinter as tk

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronômetro")
        self.running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

        self.time_label = tk.Label(self.root, text=self.format_time(), font=('Helvetica', 48))
        self.time_label.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Iniciar", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(self.root, text="Parar", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(self.root, text="Resetar", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def format_time(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def update_time(self):
        if self.running:
            self.seconds += 1
            if self.seconds == 60:
                self.seconds = 0
                self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
            self.time_label.config(text=self.format_time())
            self.root.after(1000, self.update_time)

    def start(self):
        if not self.running:
            self.running = True
            self.update_time()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.time_label.config(text=self.format_time())

if __name__ == "__main__":
    root = tk.Tk()
    app = Stopwatch(root)
    root.mainloop()
