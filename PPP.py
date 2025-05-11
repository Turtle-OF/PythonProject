import tkinter as tk
import random
from tkinter import messagebox
import difflib



class OSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Гра: Адмін ОС")

        self.health = 100
        self.updates = 0
        self.viruses = 0
        self.running_programs = []
        self.all_programs = ["Goofle", "Photoship", "Антивірус", "Музика", "Dismur", "Калькулятор"]


        self.status_label = tk.Label(root, text="", font=("Arial", 12))
        self.status_label.pack(pady=10)

        self.message_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.message_label.pack(pady=10)

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack()

        self.programs_frame = tk.Frame(root)
        self.programs_frame.pack(pady=10)

        self.log_label = tk.Label(root, text="📝 Журнал подій:", font=("Arial", 11))
        self.log_label.pack()

        self.log_text = tk.Text(root, height=10, width=60, state="disabled", bg="#f0f0f0")
        self.log_text.pack(pady=5)

        self.create_buttons()
        self.create_program_buttons()
        self.update_status()

    def log_event(self, text):
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, text + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state="disabled")

    def create_buttons(self):
        tk.Button(self.buttons_frame, text="🔍 Сканувати віруси", command=self.scan_viruses).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(self.buttons_frame, text="🔄 Встановити оновлення", command=self.install_updates).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self.buttons_frame, text="📋 Перевірити процеси", command=self.check_processes).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(self.buttons_frame, text="😴 Нічого не робити", command=self.do_nothing).grid(row=1, column=1, padx=5, pady=5)

    def create_program_buttons(self):
        tk.Label(self.programs_frame, text="⚙️ Керування програмами:", font=("Arial", 12)).pack()
        for program in self.all_programs:
            frame = tk.Frame(self.programs_frame)
            frame.pack(pady=2)
            tk.Label(frame, text=program).pack(side=tk.LEFT, padx=5)
            tk.Button(frame, text="🟢 Запустити", command=lambda p=program: self.run_program(p)).pack(side=tk.LEFT)
            tk.Button(frame, text="🔴 Закрити", command=lambda p=program: self.close_program(p)).pack(side=tk.LEFT)
            tk.Button(frame, text="⚙️ Оптимізувати", command=lambda p=program: self.optimize_program(p)).pack(side=tk.LEFT)

    def update_status(self):
        prog_list = ", ".join(self.running_programs) if self.running_programs else "немає"
        self.status_label.config(
            text=f"Здоров'я: {self.health}/100 | Оновлення: {self.updates}/5 | Віруси: {self.viruses}/5\nПрограми: {prog_list}"
        )
        if self.health <= 0:
            self.message_label.config(text="💀 Система зламана. Ти програв!", fg="red")
            self.log_event("❌ Система повністю зламана!")
            self.disable_buttons()
        elif self.updates >= 5 and self.viruses >= 5:
            self.message_label.config(text="🎉 Перемога! Система врятована!", fg="green")
            self.log_event("✅ Усі оновлення встановлено та віруси видалено. Перемога!")
            self.disable_buttons()

    def disable_buttons(self):
        for widget in self.buttons_frame.winfo_children():
            widget.config(state="disabled")
        for widget in self.programs_frame.winfo_children():
            for child in widget.winfo_children():
                if isinstance(child, tk.Button):
                    child.config(state="disabled")

    def scan_viruses(self):
        if random.random() < 0.7:
            self.message_label.config(text="✅ Вірус знайдено і видалено!", fg="green")
            self.viruses += 1
            self.log_event("🛡️ Антивірус знайшов і видалив вірус.")
            messagebox.showinfo("Антивірус", "✅ Вірус знайдено і видалено!")
        else:
            dmg = random.randint(5, 15)
            self.message_label.config(text=f"❌ Вірус не знайдено. Система постраждала (-{dmg})", fg="red")
            self.health -= dmg
            self.log_event("⚠️ Антивірус не виявив віруси. Система отримала шкоду.")
            messagebox.showwarning("Антивірус", "❌ Вірус не знайдено!\nСистема постраждала.")
        self.update_status()

    def install_updates(self):
        if random.random() < 0.6:
            self.message_label.config(text="🔄 Оновлення встановлено!", fg="green")
            self.updates += 1
            self.log_event("📥 Встановлено оновлення системи.")
            messagebox.showinfo("Оновлення", "✅ Оновлення успішно встановлено!")
        else:
            dmg = random.randint(5, 10)
            self.message_label.config(text=f"❌ Помилка оновлення! Здоров'я -{dmg}", fg="red")
            self.health -= dmg
            self.log_event("❌ Помилка під час оновлення. Система пошкоджена.")
            messagebox.showerror("Оновлення", "❌ Помилка оновлення!\nСистема пошкоджена.")
        self.update_status()

    def check_processes(self):
        dmg = len(self.running_programs) * 2
        self.message_label.config(
            text=f"📋 Запущено {len(self.running_programs)} програм. Система сповільнилася (-{dmg})", fg="orange"
        )
        self.health -= dmg
        self.log_event(f"🖥️ Перевірка процесів: {len(self.running_programs)} програм. Навантаження знизило здоров'я на {dmg}.")
        self.update_status()

    def do_nothing(self):
        dmg = random.randint(5, 10)
        self.message_label.config(text=f"😴 Ти нічого не зробив. Хакери атакували (-{dmg})", fg="red")
        self.health -= dmg
        self.log_event("😴 Без дій. Система атакована, втрачено здоров'я.")
        self.update_status()

    def run_program(self, program):
        if program not in self.running_programs:
            self.running_programs.append(program)
            self.message_label.config(text=f"🟢 Програма '{program}' запущена.", fg="green")
            self.log_event(f"🟢 Запущено програму '{program}'.")

            if program == "Калькулятор":
                self.open_calculator_window()
            elif program == "Dismur":
                self.open_discord_window()
            elif program == "goofli":
                self.open_goofli_window()

        else:
            self.message_label.config(text=f"⚠️ Програма '{program}' вже працює.", fg="orange")
        self.update_status()

    def open_calculator_window(self):
        calc_win = tk.Toplevel(self.root)
        calc_win.title("🧮 Калькулятор")
        calc_win.geometry("250x300")

        entry = tk.Entry(calc_win, width=16, font=('Arial', 18), bd=4, relief=tk.RIDGE, justify='right')
        entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        def on_click(char):
            if char == "=":
                try:
                    result = eval(entry.get())
                    entry.delete(0, tk.END)
                    entry.insert(tk.END, str(result))
                except:
                    entry.delete(0, tk.END)
                    entry.insert(tk.END, "Error")
            else:
                entry.insert(tk.END, char)

        for (text, row, col) in buttons:
            tk.Button(calc_win, text=text, width=5, height=2, font=('Arial', 14),
                      command=lambda ch=text: on_click(ch)).grid(row=row, column=col)

    def open_discord_window(self):
        dsc_win = tk.Toplevel(self.root)
        dsc_win.title("Discord")
        dsc_win.geometry("1000x800")

        chat_history = tk.Text(dsc_win, height=40, width=70, state='disabled', bg="#2f3136")
        chat_history.pack(pady=10)

        # Налаштування тегів кольору
        chat_history.tag_config("user", foreground="#57f287", background="#3c3f45")  # Discord-зелений
        chat_history.tag_config("bot", foreground="#ffffff", background="#4f545c")  # Discord-сірий

        entry = tk.Entry(dsc_win, width=30)
        entry.pack(pady=5)

        def send_message():
            user_msg = entry.get().strip().lower()
            if not user_msg:
                return

            entry.delete(0, tk.END)

            chat_history.config(state='normal')
            chat_history.insert(tk.END, f"Вы: {user_msg}\n", "user")

            known_phrases = {
                "привет": "привет, как дела?",
                "ку": "привет, как дела?",
                "норм": "Хорошо, чем могу вам помочь?",
                "как дела": "У меня все добре, спасибо 😊 А у тебя как дела?",
                "напиши код дисмур": "К сожалению, я не могу дать вам эту информацию.",
            }

            if user_msg.startswith("помоги мне с"):
                topic = user_msg.replace("помоги мне с", "").strip()
                if "вирусами" in topic:
                    bot_reply = "Рекомендую запустить антивирус и просканировать вашу систему! 🛡️"
                elif "обновлениями" in topic:
                    bot_reply = "Попробуй найти у себя кнопку 'Встановити оновлення'."
                elif "пайтоном" in topic or "python" in topic:
                    bot_reply = "Почни с основ на сайтах типа learnpython.org или Stepik. 💡"
                else:
                    bot_reply = f"Я ещё не знаю, как помочь вам с '{topic}', но могу попробовать что-то найти!"
            elif user_msg.startswith("напиши код на пайтон") or user_msg.startswith(
                    "напиши мне код на пайтон") or user_msg.startswith("код на пайтон"):
                bot_reply = (
                    "Конечно, я могу это сделать. Что вы хотите, чтобы этот код делал? Пожалуйста, "
                    "предоставьте мне больше деталей о том, какую функциональность вы ожидаете от этого кода. "
                    "Например, вы можете сказать:\n\n"
                    "Напиши мне код на Python, который печатает 'Привет, мир!'\n"
                    "Напиши мне код на Python, который добавляет два числа.\n"
                    "Напиши мне код на Python, который считывает данные из файла.\n"
                    "Чем больше вы мне предоставите, тем лучший код я смогу для вас написать."
                )
            elif user_msg.startswith(
                    "Напиши мне код на Python, который печатает 'Привет, мир!'") or user_msg.startswith(
                    "код на пайтон, который печатает 'Привет, мир!'") or user_msg.startswith(
                    "код на пайтон который печатает Привет мир") or user_msg.startswith(
                    "код на который пишет Привет мир") or user_msg.startswith("напиши мне код который пишет привет мир"):
                bot_reply = "Вот пример кода:\n\nprint('Привет, мир!')"
            elif user_msg.startswith("Напиши мне код на Python, который добавляет два числа") or user_msg.startswith("напиши мне код на пайотн который добавляет два числа") or user_msg.startswith("два числа"):
                bot_reply = (
                    "Конечно! есть несколько способов написать код на Python, который добавляет два числа:\n\n"
                    "🔹 **вот 1 способ: Спросить числа у пользователя**\n"
                    "Этот способ позволяет пользователю ввести два числа, которые затем будут добавлены.\n\n"
                    "```python\n"
                    "try:\n" 
                    "    num1 = float(input(\"Введите первое число: \"))\n"
                    "    num2 = float(input(\"Введите второе число: \"))\n"
                    "    print(\"Сумма:\", num1 + num2)\n"
                    "except ValueError:\n"
                    "    print(\"Ошибка: введите корректные числа!\")\n"
                    "```\n\n"
                    "Хочешь, покажу еще другие способы?"
                )
            elif user_msg.startswith("да"):
                bot_reply = (
                    "Вот ещё один способ:\n\n"
                    "🔹 **Способ 2: Использовать функцию**\n"
                    "```python\n"
                    "def add_numbers(a, b):\n"
                    "    return a + b\n\n"
                    "result = add_numbers(5, 3)\n"
                    "print(\"Сумма:\", result)\n"
                    "```\n"
                    "Хочешь, покажу способ с аргументами из командной строки?"
                )
            else:
                best_match = difflib.get_close_matches(user_msg, known_phrases.keys(), n=1, cutoff=0.7)
                bot_reply = known_phrases[best_match[0]] if best_match else "Я не понимаю эту команду."

            chat_history.insert(tk.END, f"Бот: {bot_reply}\n", "bot")
            chat_history.see(tk.END)
            chat_history.config(state='disabled')


        tk.Button(dsc_win, text="Отправить", command=send_message).pack()

    def close_program(self, program):
        if program in self.running_programs:
            self.running_programs.remove(program)
            self.message_label.config(text=f"🔴 Програма '{program}' закрита.", fg="green")
            self.log_event(f"🔴 Закрито програму '{program}'.")
        else:
            self.message_label.config(text=f"⚠️ Програма '{program}' не запущена.", fg="orange")
        self.update_status()

    def optimize_program(self, program):
        if program in self.running_programs:
            gain = random.randint(3, 6)
            self.health += gain
            self.message_label.config(text=f"⚙️ Програма '{program}' оптимізована! Здоров'я +{gain}", fg="blue")
            self.log_event(f"⚙️ Оптимізовано програму '{program}'. Отримано {gain} здоров'я.")
        else:
            self.message_label.config(text=f"❌ Не можна оптимізувати незапущену програму.", fg="red")
        self.update_status()

if __name__ == "__main__":
    root = tk.Tk()
    game = OSGame(root)
    root.mainloop()
